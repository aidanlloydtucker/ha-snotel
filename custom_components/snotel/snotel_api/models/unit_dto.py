from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnitDTO")


@_attrs_define
class UnitDTO:
    """Contains unit reference data.

    Attributes:
        code (Union[Unset, str]): The unit code Example: bar.
        singular_name (Union[Unset, str]): The singular unit name Example: bar.
        plural_name (Union[Unset, str]): The plural unit name Example: bars.
        description (Union[Unset, str]): The unit description Example: barometric pressure.
    """

    code: Unset | str = UNSET
    singular_name: Unset | str = UNSET
    plural_name: Unset | str = UNSET
    description: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        singular_name = self.singular_name

        plural_name = self.plural_name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if singular_name is not UNSET:
            field_dict["singularName"] = singular_name
        if plural_name is not UNSET:
            field_dict["pluralName"] = plural_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        singular_name = d.pop("singularName", UNSET)

        plural_name = d.pop("pluralName", UNSET)

        description = d.pop("description", UNSET)

        unit_dto = cls(
            code=code,
            singular_name=singular_name,
            plural_name=plural_name,
            description=description,
        )

        unit_dto.additional_properties = d
        return unit_dto

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
