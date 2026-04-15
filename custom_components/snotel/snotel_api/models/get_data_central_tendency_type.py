from enum import Enum


class GetDataCentralTendencyType(str, Enum):
    ALL = "ALL"
    AVERAGE = "AVERAGE"
    MEDIAN = "MEDIAN"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
