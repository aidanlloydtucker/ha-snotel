from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .forecast_data_dto_forecast_values import ForecastDataDTOForecastValues


T = TypeVar("T", bound="ForecastDataDTO")


@_attrs_define
class ForecastDataDTO:
    """Contains forecast data for a forecast point.

    Attributes:
        element_code (Union[Unset, str]): The element code related to the forecast record. Example: SRVO.
        forecast_period (Union[Unset, list[str]]): The start (MM-DD) and end (MM-DD) of the forecast period that the
            forecast is for. Example: ['04-01', '07-31'].
        forecast_status (Union[Unset, str]): Indicates the status of the Forecast. Example: final.
        issue_date (Union[Unset, str]): The issue date of the forecast. Example: 2023-10-02 07:45:52.
        period_normal (Union[Unset, float]): The forecast period normal. Example: 13.6.
        publication_date (Union[Unset, str]): The publication date of the forecast value. Example: 2023-04-01.
        unit_code (Union[Unset, str]): The unit code of a forecast. Example: kac_ft.
        forecast_values (Union[Unset, ForecastDataDTOForecastValues]): A dictionary of forecast values where the key is
            the exceedence probability and the value is the corresponding forecast value. Example: {'10': 36.5, '30': 28.3,
            '50': 24.1}.
    """

    element_code: Unset | str = UNSET
    forecast_period: Unset | list[str] = UNSET
    forecast_status: Unset | str = UNSET
    issue_date: Unset | str = UNSET
    period_normal: Unset | float = UNSET
    publication_date: Unset | str = UNSET
    unit_code: Unset | str = UNSET
    forecast_values: Unset | ForecastDataDTOForecastValues = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_code = self.element_code

        forecast_period: Unset | list[str] = UNSET
        if not isinstance(self.forecast_period, Unset):
            forecast_period = self.forecast_period

        forecast_status = self.forecast_status

        issue_date = self.issue_date

        period_normal = self.period_normal

        publication_date = self.publication_date

        unit_code = self.unit_code

        forecast_values: Unset | dict[str, Any] = UNSET
        if not isinstance(self.forecast_values, Unset):
            forecast_values = self.forecast_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_code is not UNSET:
            field_dict["elementCode"] = element_code
        if forecast_period is not UNSET:
            field_dict["forecastPeriod"] = forecast_period
        if forecast_status is not UNSET:
            field_dict["forecastStatus"] = forecast_status
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if period_normal is not UNSET:
            field_dict["periodNormal"] = period_normal
        if publication_date is not UNSET:
            field_dict["publicationDate"] = publication_date
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if forecast_values is not UNSET:
            field_dict["forecastValues"] = forecast_values

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from .forecast_data_dto_forecast_values import ForecastDataDTOForecastValues

        d = dict(src_dict)
        element_code = d.pop("elementCode", UNSET)

        forecast_period = cast(list[str], d.pop("forecastPeriod", UNSET))

        forecast_status = d.pop("forecastStatus", UNSET)

        issue_date = d.pop("issueDate", UNSET)

        period_normal = d.pop("periodNormal", UNSET)

        publication_date = d.pop("publicationDate", UNSET)

        unit_code = d.pop("unitCode", UNSET)

        _forecast_values = d.pop("forecastValues", UNSET)
        forecast_values: Unset | ForecastDataDTOForecastValues
        if isinstance(_forecast_values, Unset):
            forecast_values = UNSET
        else:
            forecast_values = ForecastDataDTOForecastValues.from_dict(_forecast_values)

        forecast_data_dto = cls(
            element_code=element_code,
            forecast_period=forecast_period,
            forecast_status=forecast_status,
            issue_date=issue_date,
            period_normal=period_normal,
            publication_date=publication_date,
            unit_code=unit_code,
            forecast_values=forecast_values,
        )

        forecast_data_dto.additional_properties = d
        return forecast_data_dto

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
