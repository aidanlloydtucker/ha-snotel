from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhysicalElementDTO")


@_attrs_define
class PhysicalElementDTO:
    """Contains physical element reference data.

    Attributes:
        name (Union[Unset, str]): The physical element name Example: snow depth.
        shef_physical_element_code (Union[Unset, str]): The SHEF physical element code Example: SD.
    """

    name: Unset | str = UNSET
    shef_physical_element_code: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        shef_physical_element_code = self.shef_physical_element_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if shef_physical_element_code is not UNSET:
            field_dict["shefPhysicalElementCode"] = shef_physical_element_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        shef_physical_element_code = d.pop("shefPhysicalElementCode", UNSET)

        physical_element_dto = cls(
            name=name,
            shef_physical_element_code=shef_physical_element_code,
        )

        physical_element_dto.additional_properties = d
        return physical_element_dto

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
