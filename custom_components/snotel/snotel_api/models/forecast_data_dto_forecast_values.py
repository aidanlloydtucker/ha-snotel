from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="ForecastDataDTOForecastValues")


@_attrs_define
class ForecastDataDTOForecastValues:
    """A dictionary of forecast values where the key is the exceedence probability and the value is the corresponding
    forecast value.

    Example:
            {'10': 36.5, '30': 28.3, '50': 24.1}

    """

    additional_properties: dict[str, float] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        forecast_data_dto_forecast_values = cls()

        forecast_data_dto_forecast_values.additional_properties = d
        return forecast_data_dto_forecast_values

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> float:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: float) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
