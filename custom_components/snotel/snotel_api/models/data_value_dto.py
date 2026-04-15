from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataValueDTO")


@_attrs_define
class DataValueDTO:
    """A data value

    Attributes:
        date (Union[Unset, str]): The timestamp of the data. Used only for DAILY and HOURLY durations. Example:
            2022-01-01.
        month (Union[Unset, int]): The month of the data value (1-12). Used only for MONTHLY and SEMIMONTHLY durations.
            Example: 1.
        month_part (Union[Unset, str]): The half of month of the data value ('1' for first half, '2' for second half).
            Used only for SEMIMONTHLY durations. Example: 1.
        year (Union[Unset, int]): The year of the data value. Used only for WATER_YEAR, CALENDAR_YEAR, MONTHLY, and
            SEMIMONTHLY durations. Example: 2022.
        collection_date (Union[Unset, str]): The date the data value was collected. Used only for SEMIMONTHLY durations.
            Example: 2021-12-31.
        value (Union[Unset, float]): The data value Example: 1.2.
        qc_flag (Union[Unset, str]): The qc flag of the data value Example: E.
        qa_flag (Union[Unset, str]): The qa flag of the data value Example: A.
        orig_value (Union[Unset, float]): The original data value Example: 1.3.
        orig_qc_flag (Union[Unset, str]): The original qc flag of the data value Example: V.
        average (Union[Unset, float]): The 30-year average Example: 1.4.
        median (Union[Unset, float]): The 30-year median Example: 1.0.
    """

    date: Unset | str = UNSET
    month: Unset | int = UNSET
    month_part: Unset | str = UNSET
    year: Unset | int = UNSET
    collection_date: Unset | str = UNSET
    value: Unset | float = UNSET
    qc_flag: Unset | str = UNSET
    qa_flag: Unset | str = UNSET
    orig_value: Unset | float = UNSET
    orig_qc_flag: Unset | str = UNSET
    average: Unset | float = UNSET
    median: Unset | float = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        month = self.month

        month_part = self.month_part

        year = self.year

        collection_date = self.collection_date

        value = self.value

        qc_flag = self.qc_flag

        qa_flag = self.qa_flag

        orig_value = self.orig_value

        orig_qc_flag = self.orig_qc_flag

        average = self.average

        median = self.median

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if month is not UNSET:
            field_dict["month"] = month
        if month_part is not UNSET:
            field_dict["monthPart"] = month_part
        if year is not UNSET:
            field_dict["year"] = year
        if collection_date is not UNSET:
            field_dict["collectionDate"] = collection_date
        if value is not UNSET:
            field_dict["value"] = value
        if qc_flag is not UNSET:
            field_dict["qcFlag"] = qc_flag
        if qa_flag is not UNSET:
            field_dict["qaFlag"] = qa_flag
        if orig_value is not UNSET:
            field_dict["origValue"] = orig_value
        if orig_qc_flag is not UNSET:
            field_dict["origQcFlag"] = orig_qc_flag
        if average is not UNSET:
            field_dict["average"] = average
        if median is not UNSET:
            field_dict["median"] = median

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        month = d.pop("month", UNSET)

        month_part = d.pop("monthPart", UNSET)

        year = d.pop("year", UNSET)

        collection_date = d.pop("collectionDate", UNSET)

        value = d.pop("value", UNSET)

        qc_flag = d.pop("qcFlag", UNSET)

        qa_flag = d.pop("qaFlag", UNSET)

        orig_value = d.pop("origValue", UNSET)

        orig_qc_flag = d.pop("origQcFlag", UNSET)

        average = d.pop("average", UNSET)

        median = d.pop("median", UNSET)

        data_value_dto = cls(
            date=date,
            month=month,
            month_part=month_part,
            year=year,
            collection_date=collection_date,
            value=value,
            qc_flag=qc_flag,
            qa_flag=qa_flag,
            orig_value=orig_value,
            orig_qc_flag=orig_qc_flag,
            average=average,
            median=median,
        )

        data_value_dto.additional_properties = d
        return data_value_dto

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
