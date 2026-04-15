from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .data_dto import DataDTO


T = TypeVar("T", bound="StationDataDTO")


@_attrs_define
class StationDataDTO:
    """Contains data for a station and one or more station elements

    Attributes:
        station_triplet (Union[Unset, str]): The station triplet of the station Example: 302:OR:SNTL.
        data (Union[Unset, list['DataDTO']]):
    """

    station_triplet: Unset | str = UNSET
    data: Unset | list[DataDTO] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        station_triplet = self.station_triplet

        data: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if station_triplet is not UNSET:
            field_dict["stationTriplet"] = station_triplet
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from .data_dto import DataDTO

        d = dict(src_dict)
        station_triplet = d.pop("stationTriplet", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = DataDTO.from_dict(data_item_data)

            data.append(data_item)

        station_data_dto = cls(
            station_triplet=station_triplet,
            data=data,
        )

        station_data_dto.additional_properties = d
        return station_data_dto

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
