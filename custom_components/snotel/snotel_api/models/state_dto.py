from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StateDTO")


@_attrs_define
class StateDTO:
    """Contains state reference data.

    Attributes:
        code (Union[Unset, str]): The state code Example: CO.
        fips_number (Union[Unset, str]): The state FIPS number code Example: 08.
        name (Union[Unset, str]): The state name Example: COLORADO.
        country_code (Union[Unset, str]): The country code Example: US.
    """

    code: Unset | str = UNSET
    fips_number: Unset | str = UNSET
    name: Unset | str = UNSET
    country_code: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        fips_number = self.fips_number

        name = self.name

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if fips_number is not UNSET:
            field_dict["fipsNumber"] = fips_number
        if name is not UNSET:
            field_dict["name"] = name
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        fips_number = d.pop("fipsNumber", UNSET)

        name = d.pop("name", UNSET)

        country_code = d.pop("countryCode", UNSET)

        state_dto = cls(
            code=code,
            fips_number=fips_number,
            name=name,
            country_code=country_code,
        )

        state_dto.additional_properties = d
        return state_dto

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
