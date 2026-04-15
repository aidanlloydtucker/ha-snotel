from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .timing_dto import TimingDTO
    from .timing_with_value_dto import TimingWithValueDTO


T = TypeVar("T", bound="TimingCentralTendenciesDTO")


@_attrs_define
class TimingCentralTendenciesDTO:
    """
    Attributes:
        median_peak (Union[Unset, TimingWithValueDTO]):
        median_onset (Union[Unset, TimingDTO]):
        median_meltout (Union[Unset, TimingDTO]):
        average_peak (Union[Unset, TimingWithValueDTO]):
        average_onset (Union[Unset, TimingDTO]):
        average_meltout (Union[Unset, TimingDTO]):
    """

    median_peak: Unset | TimingWithValueDTO = UNSET
    median_onset: Unset | TimingDTO = UNSET
    median_meltout: Unset | TimingDTO = UNSET
    average_peak: Unset | TimingWithValueDTO = UNSET
    average_onset: Unset | TimingDTO = UNSET
    average_meltout: Unset | TimingDTO = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        median_peak: Unset | dict[str, Any] = UNSET
        if not isinstance(self.median_peak, Unset):
            median_peak = self.median_peak.to_dict()

        median_onset: Unset | dict[str, Any] = UNSET
        if not isinstance(self.median_onset, Unset):
            median_onset = self.median_onset.to_dict()

        median_meltout: Unset | dict[str, Any] = UNSET
        if not isinstance(self.median_meltout, Unset):
            median_meltout = self.median_meltout.to_dict()

        average_peak: Unset | dict[str, Any] = UNSET
        if not isinstance(self.average_peak, Unset):
            average_peak = self.average_peak.to_dict()

        average_onset: Unset | dict[str, Any] = UNSET
        if not isinstance(self.average_onset, Unset):
            average_onset = self.average_onset.to_dict()

        average_meltout: Unset | dict[str, Any] = UNSET
        if not isinstance(self.average_meltout, Unset):
            average_meltout = self.average_meltout.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if median_peak is not UNSET:
            field_dict["medianPeak"] = median_peak
        if median_onset is not UNSET:
            field_dict["medianOnset"] = median_onset
        if median_meltout is not UNSET:
            field_dict["medianMeltout"] = median_meltout
        if average_peak is not UNSET:
            field_dict["averagePeak"] = average_peak
        if average_onset is not UNSET:
            field_dict["averageOnset"] = average_onset
        if average_meltout is not UNSET:
            field_dict["averageMeltout"] = average_meltout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from .timing_dto import TimingDTO
        from .timing_with_value_dto import TimingWithValueDTO

        d = dict(src_dict)
        _median_peak = d.pop("medianPeak", UNSET)
        median_peak: Unset | TimingWithValueDTO
        if isinstance(_median_peak, Unset):
            median_peak = UNSET
        else:
            median_peak = TimingWithValueDTO.from_dict(_median_peak)

        _median_onset = d.pop("medianOnset", UNSET)
        median_onset: Unset | TimingDTO
        if isinstance(_median_onset, Unset):
            median_onset = UNSET
        else:
            median_onset = TimingDTO.from_dict(_median_onset)

        _median_meltout = d.pop("medianMeltout", UNSET)
        median_meltout: Unset | TimingDTO
        if isinstance(_median_meltout, Unset):
            median_meltout = UNSET
        else:
            median_meltout = TimingDTO.from_dict(_median_meltout)

        _average_peak = d.pop("averagePeak", UNSET)
        average_peak: Unset | TimingWithValueDTO
        if isinstance(_average_peak, Unset):
            average_peak = UNSET
        else:
            average_peak = TimingWithValueDTO.from_dict(_average_peak)

        _average_onset = d.pop("averageOnset", UNSET)
        average_onset: Unset | TimingDTO
        if isinstance(_average_onset, Unset):
            average_onset = UNSET
        else:
            average_onset = TimingDTO.from_dict(_average_onset)

        _average_meltout = d.pop("averageMeltout", UNSET)
        average_meltout: Unset | TimingDTO
        if isinstance(_average_meltout, Unset):
            average_meltout = UNSET
        else:
            average_meltout = TimingDTO.from_dict(_average_meltout)

        timing_central_tendencies_dto = cls(
            median_peak=median_peak,
            median_onset=median_onset,
            median_meltout=median_meltout,
            average_peak=average_peak,
            average_onset=average_onset,
            average_meltout=average_meltout,
        )

        timing_central_tendencies_dto.additional_properties = d
        return timing_central_tendencies_dto

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
