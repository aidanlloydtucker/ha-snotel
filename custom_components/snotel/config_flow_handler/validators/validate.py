"""
Credential validators.

Validation functions for user credentials and authentication.

When this file grows, consider splitting into:
- credentials.py: Basic credential validation
- oauth.py: OAuth-specific validation
- api_auth.py: API authentication methods
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.snotel.api_helper import create_new_client
from custom_components.snotel.snotel_api.api.station_metadata import get_stations
from custom_components.snotel.snotel_api.errors import SnotelApiClientError
from custom_components.snotel.snotel_api.models.station_dto import StationDTO

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant


async def validate_station(hass: HomeAssistant, station_code: str) -> StationDTO:
    """
    Validate user credentials by testing API connection.

    Args:
        hass: Home Assistant instance.
        station_code: The station code to validate.

    Raises:
        SnotelApiClientAuthenticationError: If credentials are invalid.
        SnotelApiClientCommunicationError: If communication fails.
        SnotelApiClientError: For other API errors.

    """

    client = create_new_client(hass)
    async with client as client:
        stations = await get_stations.asyncio(client=client, station_triplets=station_code)
    if stations is None or len(stations) != 1:
        raise SnotelApiClientError("unknown station code")
    return stations[0]


__all__ = [
    "validate_station",
]
