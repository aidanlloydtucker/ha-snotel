from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .forecast_data_dto import ForecastDataDTO


T = TypeVar("T", bound="ForecastDTO")


@_attrs_define
class ForecastDTO:
    """Contains one or more forecasts for a forecast point.

    Attributes:
        station_triplet (Union[Unset, str]): The station triplet of the forecast point. Example: 09430500:CO:USGS.
        forecast_point_name (Union[Unset, str]): The name of the forecast point. Example: Gila R at Gila.
        data (Union[Unset, list['ForecastDataDTO']]): Contains forecast data for a forecast point.
    """

    station_triplet: Unset | str = UNSET
    forecast_point_name: Unset | str = UNSET
    data: Unset | list[ForecastDataDTO] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        station_triplet = self.station_triplet

        forecast_point_name = self.forecast_point_name

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
        if forecast_point_name is not UNSET:
            field_dict["forecastPointName"] = forecast_point_name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from .forecast_data_dto import ForecastDataDTO

        d = dict(src_dict)
        station_triplet = d.pop("stationTriplet", UNSET)

        forecast_point_name = d.pop("forecastPointName", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ForecastDataDTO.from_dict(data_item_data)

            data.append(data_item)

        forecast_dto = cls(
            station_triplet=station_triplet,
            forecast_point_name=forecast_point_name,
            data=data,
        )

        forecast_dto.additional_properties = d
        return forecast_dto

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
