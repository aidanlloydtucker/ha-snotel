from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForecastPeriodDTO")


@_attrs_define
class ForecastPeriodDTO:
    """Contains forecast period reference data.

    Attributes:
        code (Union[Unset, str]): The forecast period code Example: D1.
        name (Union[Unset, str]): The forecast period name Example: J15-JAN.
        description (Union[Unset, str]): The forecast period description Example: Jan 15 through Jan.
        begin_month_day (Union[Unset, str]): The beginning month and day for the forecast period Example: 01-15.
        end_month_day (Union[Unset, str]): The ending month and day for the forecast period Example: 01-31.
    """

    code: Unset | str = UNSET
    name: Unset | str = UNSET
    description: Unset | str = UNSET
    begin_month_day: Unset | str = UNSET
    end_month_day: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        description = self.description

        begin_month_day = self.begin_month_day

        end_month_day = self.end_month_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if begin_month_day is not UNSET:
            field_dict["beginMonthDay"] = begin_month_day
        if end_month_day is not UNSET:
            field_dict["endMonthDay"] = end_month_day

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        begin_month_day = d.pop("beginMonthDay", UNSET)

        end_month_day = d.pop("endMonthDay", UNSET)

        forecast_period_dto = cls(
            code=code,
            name=name,
            description=description,
            begin_month_day=begin_month_day,
            end_month_day=end_month_day,
        )

        forecast_period_dto.additional_properties = d
        return forecast_period_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
