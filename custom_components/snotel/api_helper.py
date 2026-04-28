"""API Client home assistant integration for SNOTEL API."""

from __future__ import annotations

from custom_components.snotel.snotel_api.client import SnotelAPIClient
from homeassistant.core import HomeAssistant
from homeassistant.helpers.httpx_client import create_async_httpx_client


def create_new_client(hass: HomeAssistant):
    """Creates new snotel api client from hass instance."""
    client = SnotelAPIClient(base_url="https://wcc.sc.egov.usda.gov/awdbRestApi")
    httpx_client = create_async_httpx_client(hass)
    httpx_client.base_url = "https://wcc.sc.egov.usda.gov/awdbRestApi"
    httpx_client.timeout = None
    client.set_async_httpx_client(httpx_client)
    return client
