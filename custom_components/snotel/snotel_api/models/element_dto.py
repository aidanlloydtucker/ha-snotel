from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementDTO")


@_attrs_define
class ElementDTO:
    """Contains element reference data.

    Attributes:
        code (Union[Unset, str]): The element code Example: PREC.
        name (Union[Unset, str]): The element name Example: PRECIPITATION ACCUMULATION.
        physical_element_name (Union[Unset, str]): The physical element name Example: precipitation accumulation.
        function_code (Union[Unset, str]): The function code Example: C.
        data_precision (Union[Unset, int]): The precision of the data Example: 2.
        description (Union[Unset, str]): The element description Example: Water Year Accumulated Precipitation.
        stored_unit_code (Union[Unset, str]): The stored unit code Example: in.
        english_unit_code (Union[Unset, str]): The english unit code Example: in.
        metric_unit_code (Union[Unset, str]): The metric unit code Example: mm.
    """

    code: Unset | str = UNSET
    name: Unset | str = UNSET
    physical_element_name: Unset | str = UNSET
    function_code: Unset | str = UNSET
    data_precision: Unset | int = UNSET
    description: Unset | str = UNSET
    stored_unit_code: Unset | str = UNSET
    english_unit_code: Unset | str = UNSET
    metric_unit_code: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        physical_element_name = self.physical_element_name

        function_code = self.function_code

        data_precision = self.data_precision

        description = self.description

        stored_unit_code = self.stored_unit_code

        english_unit_code = self.english_unit_code

        metric_unit_code = self.metric_unit_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if physical_element_name is not UNSET:
            field_dict["physicalElementName"] = physical_element_name
        if function_code is not UNSET:
            field_dict["functionCode"] = function_code
        if data_precision is not UNSET:
            field_dict["dataPrecision"] = data_precision
        if description is not UNSET:
            field_dict["description"] = description
        if stored_unit_code is not UNSET:
            field_dict["storedUnitCode"] = stored_unit_code
        if english_unit_code is not UNSET:
            field_dict["englishUnitCode"] = english_unit_code
        if metric_unit_code is not UNSET:
            field_dict["metricUnitCode"] = metric_unit_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        physical_element_name = d.pop("physicalElementName", UNSET)

        function_code = d.pop("functionCode", UNSET)

        data_precision = d.pop("dataPrecision", UNSET)

        description = d.pop("description", UNSET)

        stored_unit_code = d.pop("storedUnitCode", UNSET)

        english_unit_code = d.pop("englishUnitCode", UNSET)

        metric_unit_code = d.pop("metricUnitCode", UNSET)

        element_dto = cls(
            code=code,
            name=name,
            physical_element_name=physical_element_name,
            function_code=function_code,
            data_precision=data_precision,
            description=description,
            stored_unit_code=stored_unit_code,
            english_unit_code=english_unit_code,
            metric_unit_code=metric_unit_code,
        )

        element_dto.additional_properties = d
        return element_dto

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
