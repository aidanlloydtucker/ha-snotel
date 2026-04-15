from enum import Enum


class StationElementDTODurationName(str, Enum):
    CALENDAR_YEAR = "CALENDAR_YEAR"
    DAILY = "DAILY"
    HOURLY = "HOURLY"
    MONTHLY = "MONTHLY"
    SEMIMONTHLY = "SEMIMONTHLY"
    WATER_YEAR = "WATER_YEAR"

    def __str__(self) -> str:
        return str(self.value)
