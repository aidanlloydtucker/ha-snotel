from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .dco_dto import DcoDTO
    from .duration_dto import DurationDTO
    from .element_dto import ElementDTO
    from .forecast_period_dto import ForecastPeriodDTO
    from .function_dto import FunctionDTO
    from .instrument_dto import InstrumentDTO
    from .network_dto import NetworkDTO
    from .physical_element_dto import PhysicalElementDTO
    from .state_dto import StateDTO
    from .unit_dto import UnitDTO


T = TypeVar("T", bound="ReferenceDataDTO")


@_attrs_define
class ReferenceDataDTO:
    """Contains one or more types of reference data.

    Attributes:
        dcos (Union[Unset, list['DcoDTO']]): Contains DCO reference data.
        durations (Union[Unset, list['DurationDTO']]): Contains duration reference data.
        elements (Union[Unset, list['ElementDTO']]): Contains element reference data.
        forecast_periods (Union[Unset, list['ForecastPeriodDTO']]): Contains forecast period reference data.
        functions (Union[Unset, list['FunctionDTO']]): Contains function reference data.
        instruments (Union[Unset, list['InstrumentDTO']]): Contains instrument reference data.
        networks (Union[Unset, list['NetworkDTO']]): Contains network reference data.
        physical_elements (Union[Unset, list['PhysicalElementDTO']]): Contains physical element reference data.
        states (Union[Unset, list['StateDTO']]): Contains State reference data.
        units (Union[Unset, list['UnitDTO']]): Contains unit reference data.
    """

    dcos: Unset | list[DcoDTO] = UNSET
    durations: Unset | list[DurationDTO] = UNSET
    elements: Unset | list[ElementDTO] = UNSET
    forecast_periods: Unset | list[ForecastPeriodDTO] = UNSET
    functions: Unset | list[FunctionDTO] = UNSET
    instruments: Unset | list[InstrumentDTO] = UNSET
    networks: Unset | list[NetworkDTO] = UNSET
    physical_elements: Unset | list[PhysicalElementDTO] = UNSET
    states: Unset | list[StateDTO] = UNSET
    units: Unset | list[UnitDTO] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dcos: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.dcos, Unset):
            dcos = []
            for dcos_item_data in self.dcos:
                dcos_item = dcos_item_data.to_dict()
                dcos.append(dcos_item)

        durations: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.durations, Unset):
            durations = []
            for durations_item_data in self.durations:
                durations_item = durations_item_data.to_dict()
                durations.append(durations_item)

        elements: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        forecast_periods: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.forecast_periods, Unset):
            forecast_periods = []
            for forecast_periods_item_data in self.forecast_periods:
                forecast_periods_item = forecast_periods_item_data.to_dict()
                forecast_periods.append(forecast_periods_item)

        functions: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.functions, Unset):
            functions = []
            for functions_item_data in self.functions:
                functions_item = functions_item_data.to_dict()
                functions.append(functions_item)

        instruments: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.instruments, Unset):
            instruments = []
            for instruments_item_data in self.instruments:
                instruments_item = instruments_item_data.to_dict()
                instruments.append(instruments_item)

        networks: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        physical_elements: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.physical_elements, Unset):
            physical_elements = []
            for physical_elements_item_data in self.physical_elements:
                physical_elements_item = physical_elements_item_data.to_dict()
                physical_elements.append(physical_elements_item)

        states: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item = states_item_data.to_dict()
                states.append(states_item)

        units: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dcos is not UNSET:
            field_dict["dcos"] = dcos
        if durations is not UNSET:
            field_dict["durations"] = durations
        if elements is not UNSET:
            field_dict["elements"] = elements
        if forecast_periods is not UNSET:
            field_dict["forecastPeriods"] = forecast_periods
        if functions is not UNSET:
            field_dict["functions"] = functions
        if instruments is not UNSET:
            field_dict["instruments"] = instruments
        if networks is not UNSET:
            field_dict["networks"] = networks
        if physical_elements is not UNSET:
            field_dict["physicalElements"] = physical_elements
        if states is not UNSET:
            field_dict["states"] = states
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from .dco_dto import DcoDTO
        from .duration_dto import DurationDTO
        from .element_dto import ElementDTO
        from .forecast_period_dto import ForecastPeriodDTO
        from .function_dto import FunctionDTO
        from .instrument_dto import InstrumentDTO
        from .network_dto import NetworkDTO
        from .physical_element_dto import PhysicalElementDTO
        from .state_dto import StateDTO
        from .unit_dto import UnitDTO

        d = dict(src_dict)
        dcos = []
        _dcos = d.pop("dcos", UNSET)
        for dcos_item_data in _dcos or []:
            dcos_item = DcoDTO.from_dict(dcos_item_data)

            dcos.append(dcos_item)

        durations = []
        _durations = d.pop("durations", UNSET)
        for durations_item_data in _durations or []:
            durations_item = DurationDTO.from_dict(durations_item_data)

            durations.append(durations_item)

        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in _elements or []:
            elements_item = ElementDTO.from_dict(elements_item_data)

            elements.append(elements_item)

        forecast_periods = []
        _forecast_periods = d.pop("forecastPeriods", UNSET)
        for forecast_periods_item_data in _forecast_periods or []:
            forecast_periods_item = ForecastPeriodDTO.from_dict(forecast_periods_item_data)

            forecast_periods.append(forecast_periods_item)

        functions = []
        _functions = d.pop("functions", UNSET)
        for functions_item_data in _functions or []:
            functions_item = FunctionDTO.from_dict(functions_item_data)

            functions.append(functions_item)

        instruments = []
        _instruments = d.pop("instruments", UNSET)
        for instruments_item_data in _instruments or []:
            instruments_item = InstrumentDTO.from_dict(instruments_item_data)

            instruments.append(instruments_item)

        networks = []
        _networks = d.pop("networks", UNSET)
        for networks_item_data in _networks or []:
            networks_item = NetworkDTO.from_dict(networks_item_data)

            networks.append(networks_item)

        physical_elements = []
        _physical_elements = d.pop("physicalElements", UNSET)
        for physical_elements_item_data in _physical_elements or []:
            physical_elements_item = PhysicalElementDTO.from_dict(physical_elements_item_data)

            physical_elements.append(physical_elements_item)

        states = []
        _states = d.pop("states", UNSET)
        for states_item_data in _states or []:
            states_item = StateDTO.from_dict(states_item_data)

            states.append(states_item)

        units = []
        _units = d.pop("units", UNSET)
        for units_item_data in _units or []:
            units_item = UnitDTO.from_dict(units_item_data)

            units.append(units_item)

        reference_data_dto = cls(
            dcos=dcos,
            durations=durations,
            elements=elements,
            forecast_periods=forecast_periods,
            functions=functions,
            instruments=instruments,
            networks=networks,
            physical_elements=physical_elements,
            states=states,
            units=units,
        )

        reference_data_dto.additional_properties = d
        return reference_data_dto

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
