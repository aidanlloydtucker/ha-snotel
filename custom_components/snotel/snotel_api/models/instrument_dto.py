from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstrumentDTO")


@_attrs_define
class InstrumentDTO:
    """Contains instrument reference data.

    Attributes:
        name (Union[Unset, str]): The instrument name Example: 150" transducer - unknown.
        transducer_length (Union[Unset, int]): The transducer length Example: 150.
        data_precision_adjustment (Union[Unset, int]): The data precision adjustment
        manufacturer (Union[Unset, str]): The manufacturer Example: Sensotec/Druck/Edcliff.
        model (Union[Unset, str]): The model Example: unknown.
        active (Union[Unset, bool]): Is this instrument active
    """

    name: Unset | str = UNSET
    transducer_length: Unset | int = UNSET
    data_precision_adjustment: Unset | int = UNSET
    manufacturer: Unset | str = UNSET
    model: Unset | str = UNSET
    active: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transducer_length = self.transducer_length

        data_precision_adjustment = self.data_precision_adjustment

        manufacturer = self.manufacturer

        model = self.model

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if transducer_length is not UNSET:
            field_dict["transducerLength"] = transducer_length
        if data_precision_adjustment is not UNSET:
            field_dict["dataPrecisionAdjustment"] = data_precision_adjustment
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        transducer_length = d.pop("transducerLength", UNSET)

        data_precision_adjustment = d.pop("dataPrecisionAdjustment", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        active = d.pop("active", UNSET)

        instrument_dto = cls(
            name=name,
            transducer_length=transducer_length,
            data_precision_adjustment=data_precision_adjustment,
            manufacturer=manufacturer,
            model=model,
            active=active,
        )

        instrument_dto.additional_properties = d
        return instrument_dto

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
