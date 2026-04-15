from enum import Enum


class GetDataPeriodRef(str, Enum):
    END = "END"
    START = "START"

    def __str__(self) -> str:
        return str(self.value)
