from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .forecast_point_dto import ForecastPointDTO
    from .reservoir_metadata_dto import ReservoirMetadataDTO
    from .station_element_dto import StationElementDTO


T = TypeVar("T", bound="StationDTO")


@_attrs_define
class StationDTO:
    """Contains metadata about a station

    Attributes:
        station_id (str): The id of the station Example: 302.
        station_triplet (Union[Unset, str]): The station triplet of the station Example: 302:OR:SNTL.
        state_code (Union[Unset, str]): The 2-character state code of the station Example: OR.
        network_code (Union[Unset, str]): The network code of the station Example: SNTL.
        name (Union[Unset, str]): The name of the station Example: ANEROID LAKE #2.
        dco_code (Union[Unset, str]): The DCO code of the station Example: OR.
        county_name (Union[Unset, str]): The name of the county that the station is located in Example: Wallowa.
        huc (Union[Unset, str]): The hydrologic unit code of the station Example: 170601050101.
        elevation (Union[Unset, float]): The elevation (in feet) of the station Example: 7400.0.
        latitude (Union[Unset, float]): The latitude of the station Example: 45.21328.
        longitude (Union[Unset, float]): The longitude of the station Example: 45.21328.
        data_time_zone (Union[Unset, float]): The timezone offset from GMT of the data for the station Example: -8.0.
        pedon_code (Union[Unset, str]): The NRCS pedon code for the station
        shef_id (Union[Unset, str]): The SHEF id of the station Example: ANR03.
        operator (Union[Unset, str]): The entity in charge of the station Example: NRCS.
        begin_date (Union[Unset, str]): The date that the station was put into service Example: 1980-10-01 00:00.
        end_date (Union[Unset, str]): The date that the station was taken out of service or 2100-01-01 if still in
            service Example: 2100-01-01.
        forecast_point (Union[Unset, ForecastPointDTO]): Contains information about a forecast point
        reservoir_metadata (Union[Unset, ReservoirMetadataDTO]): Contains reservoir metadata
        station_elements (Union[Unset, list['StationElementDTO']]): The station elements of the station
        associated_hucs (Union[Unset, list[str]]): Hydrologic units within 5000m of this station Example:
            ['170501041601', '170501070301', '170501070404', '170501041603', '170501041703', '170501041304'].
    """

    station_id: str
    station_triplet: Unset | str = UNSET
    state_code: Unset | str = UNSET
    network_code: Unset | str = UNSET
    name: Unset | str = UNSET
    dco_code: Unset | str = UNSET
    county_name: Unset | str = UNSET
    huc: Unset | str = UNSET
    elevation: Unset | float = UNSET
    latitude: Unset | float = UNSET
    longitude: Unset | float = UNSET
    data_time_zone: Unset | float = UNSET
    pedon_code: Unset | str = UNSET
    shef_id: Unset | str = UNSET
    operator: Unset | str = UNSET
    begin_date: Unset | str = UNSET
    end_date: Unset | str = UNSET
    forecast_point: Unset | ForecastPointDTO = UNSET
    reservoir_metadata: Unset | ReservoirMetadataDTO = UNSET
    station_elements: Unset | list[StationElementDTO] = UNSET
    associated_hucs: Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        station_id = self.station_id

        station_triplet = self.station_triplet

        state_code = self.state_code

        network_code = self.network_code

        name = self.name

        dco_code = self.dco_code

        county_name = self.county_name

        huc = self.huc

        elevation = self.elevation

        latitude = self.latitude

        longitude = self.longitude

        data_time_zone = self.data_time_zone

        pedon_code = self.pedon_code

        shef_id = self.shef_id

        operator = self.operator

        begin_date = self.begin_date

        end_date = self.end_date

        forecast_point: Unset | dict[str, Any] = UNSET
        if not isinstance(self.forecast_point, Unset):
            forecast_point = self.forecast_point.to_dict()

        reservoir_metadata: Unset | dict[str, Any] = UNSET
        if not isinstance(self.reservoir_metadata, Unset):
            reservoir_metadata = self.reservoir_metadata.to_dict()

        station_elements: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.station_elements, Unset):
            station_elements = []
            for station_elements_item_data in self.station_elements:
                station_elements_item = station_elements_item_data.to_dict()
                station_elements.append(station_elements_item)

        associated_hucs: Unset | list[str] = UNSET
        if not isinstance(self.associated_hucs, Unset):
            associated_hucs = self.associated_hucs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stationId": station_id,
            }
        )
        if station_triplet is not UNSET:
            field_dict["stationTriplet"] = station_triplet
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if network_code is not UNSET:
            field_dict["networkCode"] = network_code
        if name is not UNSET:
            field_dict["name"] = name
        if dco_code is not UNSET:
            field_dict["dcoCode"] = dco_code
        if county_name is not UNSET:
            field_dict["countyName"] = county_name
        if huc is not UNSET:
            field_dict["huc"] = huc
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if data_time_zone is not UNSET:
            field_dict["dataTimeZone"] = data_time_zone
        if pedon_code is not UNSET:
            field_dict["pedonCode"] = pedon_code
        if shef_id is not UNSET:
            field_dict["shefId"] = shef_id
        if operator is not UNSET:
            field_dict["operator"] = operator
        if begin_date is not UNSET:
            field_dict["beginDate"] = begin_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if forecast_point is not UNSET:
            field_dict["forecastPoint"] = forecast_point
        if reservoir_metadata is not UNSET:
            field_dict["reservoirMetadata"] = reservoir_metadata
        if station_elements is not UNSET:
            field_dict["stationElements"] = station_elements
        if associated_hucs is not UNSET:
            field_dict["associatedHucs"] = associated_hucs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from .forecast_point_dto import ForecastPointDTO
        from .reservoir_metadata_dto import ReservoirMetadataDTO
        from .station_element_dto import StationElementDTO

        d = dict(src_dict)
        station_id = d.pop("stationId")

        station_triplet = d.pop("stationTriplet", UNSET)

        state_code = d.pop("stateCode", UNSET)

        network_code = d.pop("networkCode", UNSET)

        name = d.pop("name", UNSET)

        dco_code = d.pop("dcoCode", UNSET)

        county_name = d.pop("countyName", UNSET)

        huc = d.pop("huc", UNSET)

        elevation = d.pop("elevation", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        data_time_zone = d.pop("dataTimeZone", UNSET)

        pedon_code = d.pop("pedonCode", UNSET)

        shef_id = d.pop("shefId", UNSET)

        operator = d.pop("operator", UNSET)

        begin_date = d.pop("beginDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        _forecast_point = d.pop("forecastPoint", UNSET)
        forecast_point: Unset | ForecastPointDTO
        if isinstance(_forecast_point, Unset):
            forecast_point = UNSET
        else:
            forecast_point = ForecastPointDTO.from_dict(_forecast_point)

        _reservoir_metadata = d.pop("reservoirMetadata", UNSET)
        reservoir_metadata: Unset | ReservoirMetadataDTO
        if isinstance(_reservoir_metadata, Unset):
            reservoir_metadata = UNSET
        else:
            reservoir_metadata = ReservoirMetadataDTO.from_dict(_reservoir_metadata)

        station_elements = []
        _station_elements = d.pop("stationElements", UNSET)
        for station_elements_item_data in _station_elements or []:
            station_elements_item = StationElementDTO.from_dict(station_elements_item_data)

            station_elements.append(station_elements_item)

        associated_hucs = cast(list[str], d.pop("associatedHucs", UNSET))

        station_dto = cls(
            station_id=station_id,
            station_triplet=station_triplet,
            state_code=state_code,
            network_code=network_code,
            name=name,
            dco_code=dco_code,
            county_name=county_name,
            huc=huc,
            elevation=elevation,
            latitude=latitude,
            longitude=longitude,
            data_time_zone=data_time_zone,
            pedon_code=pedon_code,
            shef_id=shef_id,
            operator=operator,
            begin_date=begin_date,
            end_date=end_date,
            forecast_point=forecast_point,
            reservoir_metadata=reservoir_metadata,
            station_elements=station_elements,
            associated_hucs=associated_hucs,
        )

        station_dto.additional_properties = d
        return station_dto

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
