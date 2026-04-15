"""Sensor platform for snotel."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.snotel.const import PARALLEL_UPDATES as PARALLEL_UPDATES
from homeassistant.components.sensor import SensorEntityDescription

from .hourly import HOURLY_ENTITY_DESCRIPTIONS, SnotelBasicSensor

if TYPE_CHECKING:
    from custom_components.snotel.data import SnotelConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

# Combine all entity descriptions from different modules
ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (*HOURLY_ENTITY_DESCRIPTIONS,)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: SnotelConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    # Add air quality sensors
    async_add_entities(
        SnotelBasicSensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in HOURLY_ENTITY_DESCRIPTIONS
    )
