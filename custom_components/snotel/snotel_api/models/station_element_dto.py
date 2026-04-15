from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset
from .station_element_dto_duration_name import StationElementDTODurationName

T = TypeVar("T", bound="StationElementDTO")


@_attrs_define
class StationElementDTO:
    """Contains information about a station element

    Attributes:
        element_code (Union[Unset, str]): The element code Example: WTEQ.
        ordinal (Union[Unset, int]): The ordinal of the station element Example: 1.
        height_depth (Union[Unset, int]): The height/depth of the station element in inches
        duration_name (Union[Unset, StationElementDTODurationName]): The duration name of the station element Example:
            DAILY.
        data_precision (Union[Unset, int]): The data precision of the data for the station element Example: 2.
        stored_unit_code (Union[Unset, str]): The units that the data is stored in Example: in.
        original_unit_code (Union[Unset, str]): The units that the data was collected in Example: in.
        begin_date (Union[Unset, str]): The date that the station element was put into service Example: 1980-10-30
            15:53.
        end_date (Union[Unset, str]): The date that the station element was taken out of service or 2100-01-01 if still
            in service Example: 2100-01-01.
        derived_data (Union[Unset, bool]): true/false if the station element data is derived
    """

    element_code: Unset | str = UNSET
    ordinal: Unset | int = UNSET
    height_depth: Unset | int = UNSET
    duration_name: Unset | StationElementDTODurationName = UNSET
    data_precision: Unset | int = UNSET
    stored_unit_code: Unset | str = UNSET
    original_unit_code: Unset | str = UNSET
    begin_date: Unset | str = UNSET
    end_date: Unset | str = UNSET
    derived_data: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_code = self.element_code

        ordinal = self.ordinal

        height_depth = self.height_depth

        duration_name: Unset | str = UNSET
        if not isinstance(self.duration_name, Unset):
            duration_name = self.duration_name.value

        data_precision = self.data_precision

        stored_unit_code = self.stored_unit_code

        original_unit_code = self.original_unit_code

        begin_date = self.begin_date

        end_date = self.end_date

        derived_data = self.derived_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_code is not UNSET:
            field_dict["elementCode"] = element_code
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if height_depth is not UNSET:
            field_dict["heightDepth"] = height_depth
        if duration_name is not UNSET:
            field_dict["durationName"] = duration_name
        if data_precision is not UNSET:
            field_dict["dataPrecision"] = data_precision
        if stored_unit_code is not UNSET:
            field_dict["storedUnitCode"] = stored_unit_code
        if original_unit_code is not UNSET:
            field_dict["originalUnitCode"] = original_unit_code
        if begin_date is not UNSET:
            field_dict["beginDate"] = begin_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if derived_data is not UNSET:
            field_dict["derivedData"] = derived_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        element_code = d.pop("elementCode", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        height_depth = d.pop("heightDepth", UNSET)

        _duration_name = d.pop("durationName", UNSET)
        duration_name: Unset | StationElementDTODurationName
        if isinstance(_duration_name, Unset):
            duration_name = UNSET
        else:
            duration_name = StationElementDTODurationName(_duration_name)

        data_precision = d.pop("dataPrecision", UNSET)

        stored_unit_code = d.pop("storedUnitCode", UNSET)

        original_unit_code = d.pop("originalUnitCode", UNSET)

        begin_date = d.pop("beginDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        derived_data = d.pop("derivedData", UNSET)

        station_element_dto = cls(
            element_code=element_code,
            ordinal=ordinal,
            height_depth=height_depth,
            duration_name=duration_name,
            data_precision=data_precision,
            stored_unit_code=stored_unit_code,
            original_unit_code=original_unit_code,
            begin_date=begin_date,
            end_date=end_date,
            derived_data=derived_data,
        )

        station_element_dto.additional_properties = d
        return station_element_dto

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
