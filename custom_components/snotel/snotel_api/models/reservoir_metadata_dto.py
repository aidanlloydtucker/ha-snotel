from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReservoirMetadataDTO")


@_attrs_define
class ReservoirMetadataDTO:
    """Contains reservoir metadata

    Attributes:
        capacity (Union[Unset, float]): The capacity of the reservoir in acre-feet Example: 153000.0.
        elevation_at_capacity (Union[Unset, float]): The elevation of the reservoir (in feet) when it is at capacity
            Example: 350.0.
        usable_capacity (Union[Unset, float]): The usable capacity of the reservoir in acre-feet Example: 148640.0.
    """

    capacity: Unset | float = UNSET
    elevation_at_capacity: Unset | float = UNSET
    usable_capacity: Unset | float = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacity = self.capacity

        elevation_at_capacity = self.elevation_at_capacity

        usable_capacity = self.usable_capacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if elevation_at_capacity is not UNSET:
            field_dict["elevationAtCapacity"] = elevation_at_capacity
        if usable_capacity is not UNSET:
            field_dict["usableCapacity"] = usable_capacity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        capacity = d.pop("capacity", UNSET)

        elevation_at_capacity = d.pop("elevationAtCapacity", UNSET)

        usable_capacity = d.pop("usableCapacity", UNSET)

        reservoir_metadata_dto = cls(
            capacity=capacity,
            elevation_at_capacity=elevation_at_capacity,
            usable_capacity=usable_capacity,
        )

        reservoir_metadata_dto.additional_properties = d
        return reservoir_metadata_dto

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
