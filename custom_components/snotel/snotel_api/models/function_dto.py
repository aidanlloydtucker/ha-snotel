from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctionDTO")


@_attrs_define
class FunctionDTO:
    """Contains function reference data.

    Attributes:
        code (Union[Unset, str]): The function code Example: C.
        abbreviation (Union[Unset, str]): The abbreviation Example: OBS.
        name (Union[Unset, str]): The name Example: current observation.
    """

    code: Unset | str = UNSET
    abbreviation: Unset | str = UNSET
    name: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        abbreviation = self.abbreviation

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        name = d.pop("name", UNSET)

        function_dto = cls(
            code=code,
            abbreviation=abbreviation,
            name=name,
        )

        function_dto.additional_properties = d
        return function_dto

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
