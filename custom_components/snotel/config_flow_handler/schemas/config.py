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

from custom_components.snotel.const import CONF_STATION
from homeassistant.helpers import selector

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_STATION): str,
    }
)


def get_user_schema(defaults: Mapping[str, Any] | None = None, stations: Mapping[str, str] | None = None) -> vol.Schema:
    """
    Get schema for user step (initial setup).

    Args:
        defaults: Optional dictionary of default values to pre-populate the form.

    Returns:
        Voluptuous schema for user credentials input.

    """
    defaults = defaults or {}
    stations = stations or {}

    return vol.Schema(
        {
            vol.Required(CONF_STATION): selector.SelectSelector(
                selector.SelectSelectorConfig(
                    options=[{"label": name, "value": stn_id} for stn_id, name in stations.items()],
                    mode=selector.SelectSelectorMode.DROPDOWN,
                ),
            ),
            # vol.Optional(CONF_STATION_CODE): selector.TextSelector(
            #     selector.TextSelectorConfig(
            #         type=selector.TextSelectorType.TEXT,
            #     ),
            # ),
        },
    )
    # if len(stations.items()) > 0:
    # station_schema = selector.SelectSelector(
    #             selector.SelectSelectorConfig(
    #                 options=[{"label": id, "value": name} for id, name in stations.items()],
    #                 mode=selector.SelectSelectorMode.LIST,
    #             ),
    #         ),

    # return DATA_SCHEMA.extend({
    #     vol.Required(
    #         CONF_STATION,
    #         description={"selector": station_schema}
    #     ): str
    # })

    # return vol.Schema(
    #     {
    #         vol.Required(
    #             CONF_STATION): station_schema

    #     },
    # )


def get_reconfigure_schema(username: str) -> vol.Schema:
    """
    Get schema for reconfigure step.

    Args:
        username: Current username to pre-fill in the form.

    Returns:
        Voluptuous schema for reconfiguration.

    """
    return vol.Schema(
        {},
    )


def get_reauth_schema(username: str) -> vol.Schema:
    """
    Get schema for reauthentication step.

    Args:
        username: Current username to pre-fill in the form.

    Returns:
        Voluptuous schema for reauthentication.

    """
    return vol.Schema(
        {},
    )


__all__ = [
    "get_reauth_schema",
    "get_reconfigure_schema",
    "get_user_schema",
]
