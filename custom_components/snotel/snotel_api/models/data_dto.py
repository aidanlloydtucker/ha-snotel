from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .data_value_dto import DataValueDTO
    from .station_element_dto import StationElementDTO
    from .timing_central_tendencies_dto import TimingCentralTendenciesDTO


T = TypeVar("T", bound="DataDTO")


@_attrs_define
class DataDTO:
    """Data for a given station and element

    Attributes:
        station_element (Union[Unset, StationElementDTO]): Contains information about a station element
        timing_central_tendencies (Union[Unset, TimingCentralTendenciesDTO]):
        values (Union[Unset, list['DataValueDTO']]):
        error (Union[Unset, str]):  Example: Unsupported operation - the insertOrUpdateBeginDate parameter is not
            supported for derived data (NOTE: Only included when there is an error)..
    """

    station_element: Unset | StationElementDTO = UNSET
    timing_central_tendencies: Unset | TimingCentralTendenciesDTO = UNSET
    values: Unset | list[DataValueDTO] = UNSET
    error: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        station_element: Unset | dict[str, Any] = UNSET
        if not isinstance(self.station_element, Unset):
            station_element = self.station_element.to_dict()

        timing_central_tendencies: Unset | dict[str, Any] = UNSET
        if not isinstance(self.timing_central_tendencies, Unset):
            timing_central_tendencies = self.timing_central_tendencies.to_dict()

        values: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if station_element is not UNSET:
            field_dict["stationElement"] = station_element
        if timing_central_tendencies is not UNSET:
            field_dict["timingCentralTendencies"] = timing_central_tendencies
        if values is not UNSET:
            field_dict["values"] = values
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from .data_value_dto import DataValueDTO
        from .station_element_dto import StationElementDTO
        from .timing_central_tendencies_dto import TimingCentralTendenciesDTO

        d = dict(src_dict)
        _station_element = d.pop("stationElement", UNSET)
        station_element: Unset | StationElementDTO
        if isinstance(_station_element, Unset):
            station_element = UNSET
        else:
            station_element = StationElementDTO.from_dict(_station_element)

        _timing_central_tendencies = d.pop("timingCentralTendencies", UNSET)
        timing_central_tendencies: Unset | TimingCentralTendenciesDTO
        if isinstance(_timing_central_tendencies, Unset):
            timing_central_tendencies = UNSET
        else:
            timing_central_tendencies = TimingCentralTendenciesDTO.from_dict(_timing_central_tendencies)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = DataValueDTO.from_dict(values_item_data)

            values.append(values_item)

        error = d.pop("error", UNSET)

        data_dto = cls(
            station_element=station_element,
            timing_central_tendencies=timing_central_tendencies,
            values=values,
            error=error,
        )

        data_dto.additional_properties = d
        return data_dto

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
