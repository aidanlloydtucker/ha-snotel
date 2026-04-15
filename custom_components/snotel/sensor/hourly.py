"""Snow depth sensor for snotel."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.snotel.entity import SnotelEntity
from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorEntityDescription, SensorStateClass

if TYPE_CHECKING:
    from custom_components.snotel.coordinator import SnotelDataUpdateCoordinator


HOURLY_ENTITY_DESCRIPTIONS = (
    # Hourly
    # PREC (PRECIPITATION ACCUMULATION, Water Year Accumulated Precipitation), SNWD (SNOW DEPTH), TOBS, WTEQ (SNOW WATER EQUIVALENT)
    SensorEntityDescription(
        key="precip_accumulation",
        translation_key="precip_accumulation",
        icon="mdi:water",
        state_class=SensorStateClass.TOTAL,
        device_class=SensorDeviceClass.PRECIPITATION,
        suggested_display_precision=0,
        has_entity_name=True,
        native_unit_of_measurement="in",
    ),
    SensorEntityDescription(
        key="snow_depth",
        translation_key="snow_depth",
        icon="mdi:snowflake",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.PRECIPITATION,
        suggested_display_precision=0,
        has_entity_name=True,
        native_unit_of_measurement="in",
    ),
    SensorEntityDescription(
        key="temperature",
        translation_key="temperature",
        icon="mdi:thermometer",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        suggested_display_precision=0,
        has_entity_name=True,
        native_unit_of_measurement="°F",
    ),
    SensorEntityDescription(
        key="snow_water_equivalent",
        translation_key="snow_water_equivalent",
        icon="mdi:snowflake-melt",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.PRECIPITATION,
        suggested_display_precision=0,
        has_entity_name=True,
        native_unit_of_measurement="in",
    ),
    SensorEntityDescription(
        key="last_updated",
        translation_key="last_updated",
        icon="mdi:clock",
        device_class=SensorDeviceClass.TIMESTAMP,
        suggested_display_precision=0,
        has_entity_name=True,
    ),
    # Daily
    # PRCP (precipitation increment), PRCPMTD (PRECIPITATION MONTH-TO-DATE), PRCPSA (PRECIPITATION INCREMENT - SNOW-ADJ), PREC, SNDN (Snow Density), SNWD, TAVG (AIR TEMPERATURE AVERAGE), TMAX, TMIN, TOBS (AIR TEMPERATURE OBSERVED), WTEQ (SNOW WATER EQUIVALENT),
)


class SnotelBasicSensor(SensorEntity, SnotelEntity):
    """Basic sensor class."""

    def __init__(
        self,
        coordinator: SnotelDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entity_description)

    @property
    def native_value(self) -> int | float | None:
        """Return the native value of the sensor."""
        if not self.coordinator.last_update_success:
            return None

        return self.coordinator.data.get(self.entity_description.key, None)

    @property
    def extra_state_attributes(self) -> dict[str, str | int | float]:
        """Return additional state attributes."""
        # Base attributes from API
        attributes: dict[str, str | int | float] = {
            "last_updated": self.coordinator.data.get("last_updated", "unknown"),
        }

        return attributes

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success
