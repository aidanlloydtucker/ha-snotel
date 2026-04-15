from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, SnotelAPIClient
from ...models.station_dto import StationDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    station_triplets: Unset | str = UNSET,
    station_names: Unset | str = UNSET,
    dco_codes: Unset | str = UNSET,
    county_names: Unset | str = UNSET,
    elements: Unset | str = UNSET,
    durations: Unset | str = UNSET,
    hucs: Unset | str = UNSET,
    return_forecast_point_metadata: Unset | bool = False,
    return_reservoir_metadata: Unset | bool = False,
    return_station_elements: Unset | bool = False,
    active_only: Unset | bool = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["stationTriplets"] = station_triplets

    params["stationNames"] = station_names

    params["dcoCodes"] = dco_codes

    params["countyNames"] = county_names

    params["elements"] = elements

    params["durations"] = durations

    params["hucs"] = hucs

    params["returnForecastPointMetadata"] = return_forecast_point_metadata

    params["returnReservoirMetadata"] = return_reservoir_metadata

    params["returnStationElements"] = return_station_elements

    params["activeOnly"] = active_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/v1/stations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | SnotelAPIClient, response: httpx.Response
) -> Any | list[StationDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StationDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | SnotelAPIClient, response: httpx.Response
) -> Response[Any | list[StationDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: Unset | str = UNSET,
    station_names: Unset | str = UNSET,
    dco_codes: Unset | str = UNSET,
    county_names: Unset | str = UNSET,
    elements: Unset | str = UNSET,
    durations: Unset | str = UNSET,
    hucs: Unset | str = UNSET,
    return_forecast_point_metadata: Unset | bool = False,
    return_reservoir_metadata: Unset | bool = False,
    return_station_elements: Unset | bool = False,
    active_only: Unset | bool = True,
) -> Response[Any | list[StationDTO]]:
    """Gets the metadata for one or more stations

     Retrieves the station metadata for one or more stations

    Args:
        station_triplets (Union[Unset, str]):
        station_names (Union[Unset, str]):
        dco_codes (Union[Unset, str]):
        county_names (Union[Unset, str]):
        elements (Union[Unset, str]):
        durations (Union[Unset, str]):
        hucs (Union[Unset, str]):
        return_forecast_point_metadata (Union[Unset, bool]):  Default: False.
        return_reservoir_metadata (Union[Unset, bool]):  Default: False.
        return_station_elements (Union[Unset, bool]):  Default: False.
        active_only (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['StationDTO']]]
    """

    kwargs = _get_kwargs(
        station_triplets=station_triplets,
        station_names=station_names,
        dco_codes=dco_codes,
        county_names=county_names,
        elements=elements,
        durations=durations,
        hucs=hucs,
        return_forecast_point_metadata=return_forecast_point_metadata,
        return_reservoir_metadata=return_reservoir_metadata,
        return_station_elements=return_station_elements,
        active_only=active_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: Unset | str = UNSET,
    station_names: Unset | str = UNSET,
    dco_codes: Unset | str = UNSET,
    county_names: Unset | str = UNSET,
    elements: Unset | str = UNSET,
    durations: Unset | str = UNSET,
    hucs: Unset | str = UNSET,
    return_forecast_point_metadata: Unset | bool = False,
    return_reservoir_metadata: Unset | bool = False,
    return_station_elements: Unset | bool = False,
    active_only: Unset | bool = True,
) -> Any | list[StationDTO] | None:
    """Gets the metadata for one or more stations

     Retrieves the station metadata for one or more stations

    Args:
        station_triplets (Union[Unset, str]):
        station_names (Union[Unset, str]):
        dco_codes (Union[Unset, str]):
        county_names (Union[Unset, str]):
        elements (Union[Unset, str]):
        durations (Union[Unset, str]):
        hucs (Union[Unset, str]):
        return_forecast_point_metadata (Union[Unset, bool]):  Default: False.
        return_reservoir_metadata (Union[Unset, bool]):  Default: False.
        return_station_elements (Union[Unset, bool]):  Default: False.
        active_only (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['StationDTO']]
    """

    return sync_detailed(
        client=client,
        station_triplets=station_triplets,
        station_names=station_names,
        dco_codes=dco_codes,
        county_names=county_names,
        elements=elements,
        durations=durations,
        hucs=hucs,
        return_forecast_point_metadata=return_forecast_point_metadata,
        return_reservoir_metadata=return_reservoir_metadata,
        return_station_elements=return_station_elements,
        active_only=active_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: Unset | str = UNSET,
    station_names: Unset | str = UNSET,
    dco_codes: Unset | str = UNSET,
    county_names: Unset | str = UNSET,
    elements: Unset | str = UNSET,
    durations: Unset | str = UNSET,
    hucs: Unset | str = UNSET,
    return_forecast_point_metadata: Unset | bool = False,
    return_reservoir_metadata: Unset | bool = False,
    return_station_elements: Unset | bool = False,
    active_only: Unset | bool = True,
) -> Response[Any | list[StationDTO]]:
    """Gets the metadata for one or more stations

     Retrieves the station metadata for one or more stations

    Args:
        station_triplets (Union[Unset, str]):
        station_names (Union[Unset, str]):
        dco_codes (Union[Unset, str]):
        county_names (Union[Unset, str]):
        elements (Union[Unset, str]):
        durations (Union[Unset, str]):
        hucs (Union[Unset, str]):
        return_forecast_point_metadata (Union[Unset, bool]):  Default: False.
        return_reservoir_metadata (Union[Unset, bool]):  Default: False.
        return_station_elements (Union[Unset, bool]):  Default: False.
        active_only (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['StationDTO']]]
    """

    kwargs = _get_kwargs(
        station_triplets=station_triplets,
        station_names=station_names,
        dco_codes=dco_codes,
        county_names=county_names,
        elements=elements,
        durations=durations,
        hucs=hucs,
        return_forecast_point_metadata=return_forecast_point_metadata,
        return_reservoir_metadata=return_reservoir_metadata,
        return_station_elements=return_station_elements,
        active_only=active_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: Unset | str = UNSET,
    station_names: Unset | str = UNSET,
    dco_codes: Unset | str = UNSET,
    county_names: Unset | str = UNSET,
    elements: Unset | str = UNSET,
    durations: Unset | str = UNSET,
    hucs: Unset | str = UNSET,
    return_forecast_point_metadata: Unset | bool = False,
    return_reservoir_metadata: Unset | bool = False,
    return_station_elements: Unset | bool = False,
    active_only: Unset | bool = True,
) -> Any | list[StationDTO] | None:
    """Gets the metadata for one or more stations

     Retrieves the station metadata for one or more stations

    Args:
        station_triplets (Union[Unset, str]):
        station_names (Union[Unset, str]):
        dco_codes (Union[Unset, str]):
        county_names (Union[Unset, str]):
        elements (Union[Unset, str]):
        durations (Union[Unset, str]):
        hucs (Union[Unset, str]):
        return_forecast_point_metadata (Union[Unset, bool]):  Default: False.
        return_reservoir_metadata (Union[Unset, bool]):  Default: False.
        return_station_elements (Union[Unset, bool]):  Default: False.
        active_only (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['StationDTO']]
    """

    return (
        await asyncio_detailed(
            client=client,
            station_triplets=station_triplets,
            station_names=station_names,
            dco_codes=dco_codes,
            county_names=county_names,
            elements=elements,
            durations=durations,
            hucs=hucs,
            return_forecast_point_metadata=return_forecast_point_metadata,
            return_reservoir_metadata=return_reservoir_metadata,
            return_station_elements=return_station_elements,
            active_only=active_only,
        )
    ).parsed
