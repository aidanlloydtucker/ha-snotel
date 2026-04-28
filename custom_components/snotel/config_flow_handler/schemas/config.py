"""
Config flow schemas.

Schemas for the main configuration flow steps:
- User setup
- Reconfiguration
- Reauthentication

When this file grows too large (>300 lines), consider splitting into:
- user.py: User setup schemas
- reauth.py: Reauthentication schemas
- reconfigure.py: Reconfiguration schemas
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import voluptuous as vol

from custom_components.snotel.const import (
    CONF_SETUP_TYPE,
    CONF_SETUP_TYPE_LAT_LONG,
    CONF_SETUP_TYPE_STATION_SEARCH,
    CONF_SETUP_TYPE_STATION_TRIPLET,
    CONF_STATION_CODE,
    CONF_STATION_SEARCH,
)
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE
from homeassistant.helpers import config_validation as cv, selector


def get_user_schema(defaults: Mapping[str, Any] | None = None) -> vol.Schema:
    """
    Get schema for user step (initial setup).

    Args:
        defaults: Optional dictionary of default values to pre-populate the form.

    Returns:
        Voluptuous schema for user input.

    """
    defaults = defaults or {}

    return vol.Schema(
        {
            vol.Required(CONF_SETUP_TYPE): selector.SelectSelector(
                selector.SelectSelectorConfig(
                    options=[CONF_SETUP_TYPE_STATION_SEARCH, CONF_SETUP_TYPE_LAT_LONG, CONF_SETUP_TYPE_STATION_TRIPLET],
                    translation_key="setup_type_key",
                    mode=selector.SelectSelectorMode.LIST,
                ),
            ),
        },
    )


def get_station_search_schema(
    defaults: Mapping[str, Any] | None = None, stations: Mapping[str, str] | None = None
) -> vol.Schema:
    """
    Get schema for station search step (initial setup).

    Args:
        defaults: Optional dictionary of default values to pre-populate the form.
        stations: Optional dictionary of station ids to their names to pre-populate in the select list

    Returns:
        Voluptuous schema for station_search input.

    """
    defaults = defaults or {}
    stations = stations or {}

    return vol.Schema(
        {
            vol.Required(CONF_STATION_SEARCH): selector.SelectSelector(
                selector.SelectSelectorConfig(
                    options=[{"label": name, "value": stn_id} for stn_id, name in stations.items()],
                    mode=selector.SelectSelectorMode.DROPDOWN,
                ),
            ),
        },
    )


def get_lat_long_schema(defaults: Mapping[str, Any] | None = None) -> vol.Schema:
    """
    Get schema for lat/long step (initial setup).

    Args:
        defaults: Optional dictionary of default values to pre-populate the form.

    Returns:
        Voluptuous schema for lat/long input.

    """
    defaults = defaults or {}

    return vol.Schema(
        {
            vol.Required(CONF_LATITUDE, default=defaults[CONF_LATITUDE]): cv.latitude,
            vol.Required(CONF_LONGITUDE, default=defaults[CONF_LONGITUDE]): cv.longitude,
        },
    )


def get_station_triplet_schema(defaults: Mapping[str, Any] | None = None) -> vol.Schema:
    """
    Get schema for station manual triplet step (initial setup).

    Args:
        defaults: Optional dictionary of default values to pre-populate the form.

    Returns:
        Voluptuous schema for station_triplet input.

    """
    defaults = defaults or {}

    return vol.Schema(
        {
            vol.Required(CONF_STATION_CODE): str,
        },
    )


__all__ = [
    "get_lat_long_schema",
    "get_station_search_schema",
    "get_station_triplet_schema",
    "get_user_schema",
]
