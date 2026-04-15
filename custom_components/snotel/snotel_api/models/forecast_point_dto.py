from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForecastPointDTO")


@_attrs_define
class ForecastPointDTO:
    """Contains information about a forecast point

    Attributes:
        name (Union[Unset, str]): The name of the forecast point Example: Alamosa Ck ab Terrace Reservoir.
        forecaster (Union[Unset, str]): The user name of the forecaster who forecasts for this station Example:
            agoodbody.
        exceedence_probabilities (Union[Unset, list[int]]): The name to display in the UI for the profile type Example:
            [10, 30, 50, 70, 90].
    """

    name: Unset | str = UNSET
    forecaster: Unset | str = UNSET
    exceedence_probabilities: Unset | list[int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        forecaster = self.forecaster

        exceedence_probabilities: Unset | list[int] = UNSET
        if not isinstance(self.exceedence_probabilities, Unset):
            exceedence_probabilities = self.exceedence_probabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if forecaster is not UNSET:
            field_dict["forecaster"] = forecaster
        if exceedence_probabilities is not UNSET:
            field_dict["exceedenceProbabilities"] = exceedence_probabilities

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        forecaster = d.pop("forecaster", UNSET)

        exceedence_probabilities = cast(list[int], d.pop("exceedenceProbabilities", UNSET))

        forecast_point_dto = cls(
            name=name,
            forecaster=forecaster,
            exceedence_probabilities=exceedence_probabilities,
        )

        forecast_point_dto.additional_properties = d
        return forecast_point_dto

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
