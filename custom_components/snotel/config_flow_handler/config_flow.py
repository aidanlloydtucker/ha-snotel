"""
Config flow for snotel.

This module implements the main configuration flow including:
- Initial user setup
- Reconfiguration of existing entries
- Reauthentication flow

For more information:
https://developers.home-assistant.io/docs/config_entries_config_flow_handler
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree
from slugify import slugify

from custom_components.snotel.api_helper import create_new_client
from custom_components.snotel.config_flow_handler.schemas import get_user_schema
from custom_components.snotel.config_flow_handler.schemas.config import (
    get_lat_long_schema,
    get_station_search_schema,
    get_station_triplet_schema,
)
from custom_components.snotel.config_flow_handler.validators.validate import validate_station
from custom_components.snotel.const import (
    CONF_SETUP_TYPE,
    CONF_SETUP_TYPE_LAT_LONG,
    CONF_SETUP_TYPE_STATION_SEARCH,
    CONF_SETUP_TYPE_STATION_TRIPLET,
    CONF_STATION_CODE,
    CONF_STATION_SEARCH,
    DOMAIN,
    LOGGER,
)
from custom_components.snotel.snotel_api.api.station_metadata import get_stations
from custom_components.snotel.snotel_api.types import Unset
from homeassistant import config_entries
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE

# Map exception types to error keys for user-facing messages
ERROR_MAP = {
    "SnotelApiClientAuthenticationError": "auth",
    "SnotelApiClientCommunicationError": "connection",
    "SnotelConfigError": "config",
}


class SnotelConfigFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """
    Handle a config flow for snotel.

    This class manages the configuration flow for the integration, including
    initial setup, reconfiguration, and reauthentication.

    Supported flows:
    - user: Initial setup via UI

    For more details:
    https://developers.home-assistant.io/docs/config_entries_config_flow_handler
    """

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """
        Handle a flow initialized by the user.

        This is the entry point when a user adds the integration from the UI. This asks the user to set up via latlong or stations

        Args:
            user_input: The user input from the config flow form, or None for initial display.

        Returns:
            The config flow result, either showing a form or creating an entry.

        """
        errors: dict[str, str] = {}

        if user_input is not None:
            if user_input[CONF_SETUP_TYPE] == CONF_SETUP_TYPE_STATION_SEARCH:
                return await self.async_step_station_search()
            if user_input[CONF_SETUP_TYPE] == CONF_SETUP_TYPE_LAT_LONG:
                return await self.async_step_lat_long()
            if user_input[CONF_SETUP_TYPE] == CONF_SETUP_TYPE_STATION_TRIPLET:
                return await self.async_step_station_triplet()
            errors[CONF_SETUP_TYPE] = "unknown_setup_type"

        return self.async_show_form(
            step_id="user",
            data_schema=get_user_schema(
                user_input,
            ),
            errors=errors,
            description_placeholders={
                "documentation_url": "https://github.com/aidanlloydtucker/ha-snotel",
            },
        )

    async def async_step_station_search(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """
        Handle the user searching for a station to set it up.

        Args:
            user_input: The user input from the config flow form, or None for initial display.

        Returns:
            The config flow result, either showing a form or creating an entry.

        """
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                station = await validate_station(
                    self.hass,
                    station_code=user_input[CONF_STATION_SEARCH],
                )
            except Exception as exception:  # noqa: BLE001
                errors["base"] = self._map_exception_to_error(exception)
            else:
                await self.async_set_unique_id(slugify(user_input[CONF_STATION_SEARCH].lower()))
                self._abort_if_unique_id_configured()

                new_config = {}
                new_config[CONF_SETUP_TYPE] = CONF_SETUP_TYPE_STATION_SEARCH
                new_config[CONF_STATION_CODE] = user_input[CONF_STATION_SEARCH]

                return self.async_create_entry(
                    title=f"{station.name}, {station.state_code or station.county_name}"
                    or user_input[CONF_STATION_SEARCH],
                    data=new_config,
                )

        client = create_new_client(self.hass)
        try:
            async with client as client:
                stations = await get_stations.asyncio(client=client)
        except Exception as exception:  # noqa: BLE001
            errors["base"] = self._map_exception_to_error(exception)
            stations = []

        stations = stations or []

        return self.async_show_form(
            step_id="station_search",
            data_schema=get_station_search_schema(
                user_input,
                stations={
                    station.station_triplet: f"{station.name}, {station.state_code or station.county_name}"
                    for station in stations
                    if not isinstance(station.station_triplet, Unset)
                    and not isinstance(station.name, Unset)
                    and station is not None
                },
            ),
            errors=errors,
            description_placeholders={
                "documentation_url": "https://github.com/aidanlloydtucker/ha-snotel",
            },
        )

    async def async_step_lat_long(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """
        Handle the user giving lat long to get the closest station.

        Args:
            user_input: The user input from the config flow form, or None for initial display.

        Returns:
            The config flow result, either showing a form or creating an entry.

        """
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                station_triplet = await self._closest_station_from_lat_long(
                    lat=user_input[CONF_LATITUDE],
                    long=user_input[CONF_LONGITUDE],
                )
                station = await validate_station(
                    self.hass,
                    station_code=station_triplet,
                )

            except Exception as exception:  # noqa: BLE001
                errors["base"] = self._map_exception_to_error(exception)
            else:
                await self.async_set_unique_id(slugify(station_triplet.lower()))
                self._abort_if_unique_id_configured()

                new_config = {}
                new_config[CONF_SETUP_TYPE] = CONF_SETUP_TYPE_LAT_LONG
                new_config[CONF_STATION_CODE] = station_triplet
                new_config[CONF_LATITUDE] = user_input[CONF_LATITUDE]
                new_config[CONF_LONGITUDE] = user_input[CONF_LONGITUDE]

                return self.async_create_entry(
                    title=f"{station.name}, {station.state_code or station.county_name}" or station_triplet,
                    data=new_config,
                )

        defaults = {}
        defaults[CONF_LATITUDE] = self.hass.config.latitude
        defaults[CONF_LONGITUDE] = self.hass.config.longitude
        return self.async_show_form(
            step_id="lat_long",
            data_schema=get_lat_long_schema(
                defaults,
            ),
            errors=errors,
            description_placeholders={
                "documentation_url": "https://github.com/aidanlloydtucker/ha-snotel",
            },
        )

    async def _closest_station_from_lat_long(
        self,
        lat: float,
        long: float,
    ) -> str:
        """
        Get the closest station from lat and long.

        Args:
            lat: latitude
            long: longetude

        Returns:
            The closest station code

        """
        client = create_new_client(self.hass)
        async with client as client:
            stations = await get_stations.asyncio(client=client)

        stations = stations or []
        stations = [x for x in stations if x.latitude and x.longitude and x.state_code]
        if len(stations) == 0:
            raise SnotelConfigError("no stations")

        df = pd.DataFrame(
            {
                "lat": [x.latitude for x in stations],
                "lon": [x.longitude for x in stations],
                "code": [x.station_triplet for x in stations],
            }
        )
        coords = np.radians(df[["lat", "lon"]])
        tree = BallTree(coords, metric="haversine")

        target = np.radians([[lat, long]])

        # k=1 for the single nearest neighbor
        _, ind = tree.query(target, k=1)
        if len(ind) == 0 or len(ind[0]) == 0:
            raise SnotelConfigError("no closest station")

        closest_entry = df.iloc[ind[0][0]]
        return closest_entry["code"]

    async def async_step_station_triplet(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """
        Handle the user giving a custom station triplet code.

        Args:
            user_input: The user input from the config flow form, or None for initial display.

        Returns:
            The config flow result, either showing a form or creating an entry.

        """
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                station = await validate_station(
                    self.hass,
                    station_code=user_input[CONF_STATION_CODE],
                )
            except Exception as exception:  # noqa: BLE001
                errors["base"] = self._map_exception_to_error(exception)
            else:
                await self.async_set_unique_id(slugify(user_input[CONF_STATION_CODE].lower()))
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=f"{station.name}, {station.state_code or station.county_name}"
                    or user_input[CONF_STATION_CODE],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="station_triplet",
            data_schema=get_station_triplet_schema(
                user_input,
            ),
            errors=errors,
            description_placeholders={
                "documentation_url": "https://github.com/aidanlloydtucker/ha-snotel",
            },
        )

    def _map_exception_to_error(self, exception: Exception) -> str:
        """
        Map API exceptions to user-facing error keys.

        Args:
            exception: The exception that was raised.

        Returns:
            The error key for display in the config flow form.

        """
        LOGGER.warning("Error in config flow: %s", exception)
        exception_name = type(exception).__name__
        return ERROR_MAP.get(exception_name, "unknown")


__all__ = ["SnotelConfigFlowHandler"]


class SnotelConfigError(Exception):
    """Base exception to indicate a general config error."""
