"""
Data processing utilities for the coordinator.

This module provides functions for processing, transforming, and validating
data received from the API before distributing it to entities.

Use cases:
- Data normalization and validation
- Caching strategies for expensive computations
- Data transformation for entity consumption
- Aggregation of multiple API responses
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from custom_components.snotel.const import LOGGER


def validate_api_response(data: Any) -> bool:
    """
    Validate the structure and content of API response data.

    Args:
        data: The raw data received from the API.

    Returns:
        True if the data is valid, False otherwise.

    Example:
        >>> data = {"userId": 1, "id": 1, "title": "Test"}
        >>> validate_api_response(data)
        True
    """
    if not isinstance(data, list):
        LOGGER.warning("Invalid API response: expected list, got %s", type(data).__name__)
        return False
    if len(data) != 1:
        LOGGER.warning("Invalid API response: expected list of length 1, got %d", len(data))
        return False
    if not isinstance(data[0].data, list):
        LOGGER.warning("Invalid API response: expected data[0].data list, got %s", type(data).__name__)
        return False
    if len(data[0].data) <= 0:
        LOGGER.warning("Invalid API response: expected data[0].data list of length non zero, got %v", len(data))
        return False

    # Add validation logic based on your API structure
    # This is a placeholder for future implementation
    return True


def transform_api_data(raw_data: Any, station_tz: float) -> dict[str, Any]:
    """
    Transform raw API data into a standardized format for entities.

    This function can be used to:
    - Normalize field names
    - Convert units
    - Calculate derived values
    - Restructure nested data

    Args:
        raw_data: The raw data from the API.

    Returns:
        A dictionary with transformed data ready for entity consumption.

    Example:
        >>> raw = {"temp_c": 25.5}
        >>> transform_api_data(raw)
        {"temperature": 25.5, "temperature_f": 77.9}
    """
    if not validate_api_response(raw_data):
        LOGGER.warning("Skipping transformation of invalid data")
        return {}

    data_map = {}
    timestamp = ""
    for datum in raw_data[0].data or []:
        if datum.station_element and datum.values and len(datum.values) > 0:
            data_map[element_code_to_entity_key(datum.station_element.element_code)] = datum.values[0].value
            if datum.values[0].date:
                if timestamp == "" or datum.values[0].date > timestamp:
                    timestamp = datum.values[0].date
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    data_map["last_updated"] = dt.replace(tzinfo=timezone(timedelta(hours=station_tz)))
    return data_map


def cache_computed_values(data: dict[str, Any]) -> dict[str, Any]:
    """
    Add computed or cached values to the coordinator data.

    This is useful for expensive calculations that should only be done once
    per update cycle rather than in each entity.

    Args:
        data: The base data dictionary.

    Returns:
        The data dictionary with additional computed values.

    Example:
        >>> data = {"power": 1000, "runtime": 3600}
        >>> cache_computed_values(data)
        {"power": 1000, "runtime": 3600, "energy_kwh": 1.0}
    """
    # Add computed values as needed
    # This is a placeholder for future implementation
    return data


def element_code_to_entity_key(element_code) -> str:
    """Converts element codes from API into entity keys."""
    codes = {
        "PREC": "precip_accumulation",
        "SNWD": "snow_depth",
        "TOBS": "temperature",
        "WTEQ": "snow_water_equivalent",
    }
    return codes.get(element_code, "")
