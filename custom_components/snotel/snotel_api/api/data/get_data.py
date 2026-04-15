from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, SnotelAPIClient
from ...models.get_data_central_tendency_type import GetDataCentralTendencyType
from ...models.get_data_duration import GetDataDuration
from ...models.get_data_period_ref import GetDataPeriodRef
from ...models.station_data_dto import StationDataDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    station_triplets: str,
    elements: str,
    duration: Unset | GetDataDuration = UNSET,
    begin_date: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    insert_or_update_begin_date: Unset | str = UNSET,
    period_ref: Unset | GetDataPeriodRef = UNSET,
    central_tendency_type: Unset | GetDataCentralTendencyType = UNSET,
    return_flags: Unset | bool = False,
    return_original_values: Unset | bool = False,
    return_suspect_data: Unset | bool = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["stationTriplets"] = station_triplets

    params["elements"] = elements

    json_duration: Unset | str = UNSET
    if not isinstance(duration, Unset):
        json_duration = duration.value

    params["duration"] = json_duration

    params["beginDate"] = begin_date

    params["endDate"] = end_date

    params["insertOrUpdateBeginDate"] = insert_or_update_begin_date

    json_period_ref: Unset | str = UNSET
    if not isinstance(period_ref, Unset):
        json_period_ref = period_ref.value

    params["periodRef"] = json_period_ref

    json_central_tendency_type: Unset | str = UNSET
    if not isinstance(central_tendency_type, Unset):
        json_central_tendency_type = central_tendency_type.value

    params["centralTendencyType"] = json_central_tendency_type

    params["returnFlags"] = return_flags

    params["returnOriginalValues"] = return_original_values

    params["returnSuspectData"] = return_suspect_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/v1/data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | SnotelAPIClient, response: httpx.Response
) -> Any | list[StationDataDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StationDataDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | SnotelAPIClient, response: httpx.Response
) -> Response[Any | list[StationDataDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: str,
    elements: str,
    duration: Unset | GetDataDuration = UNSET,
    begin_date: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    insert_or_update_begin_date: Unset | str = UNSET,
    period_ref: Unset | GetDataPeriodRef = UNSET,
    central_tendency_type: Unset | GetDataCentralTendencyType = UNSET,
    return_flags: Unset | bool = False,
    return_original_values: Unset | bool = False,
    return_suspect_data: Unset | bool = False,
) -> Response[Any | list[StationDataDTO]]:
    """Gets data for one or more stations

     Retrieves data for one or more stations

    Args:
        station_triplets (str):
        elements (str):
        duration (Union[Unset, GetDataDuration]):
        begin_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        insert_or_update_begin_date (Union[Unset, str]):
        period_ref (Union[Unset, GetDataPeriodRef]):
        central_tendency_type (Union[Unset, GetDataCentralTendencyType]):
        return_flags (Union[Unset, bool]):  Default: False.
        return_original_values (Union[Unset, bool]):  Default: False.
        return_suspect_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['StationDataDTO']]]
    """

    kwargs = _get_kwargs(
        station_triplets=station_triplets,
        elements=elements,
        duration=duration,
        begin_date=begin_date,
        end_date=end_date,
        insert_or_update_begin_date=insert_or_update_begin_date,
        period_ref=period_ref,
        central_tendency_type=central_tendency_type,
        return_flags=return_flags,
        return_original_values=return_original_values,
        return_suspect_data=return_suspect_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: str,
    elements: str,
    duration: Unset | GetDataDuration = UNSET,
    begin_date: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    insert_or_update_begin_date: Unset | str = UNSET,
    period_ref: Unset | GetDataPeriodRef = UNSET,
    central_tendency_type: Unset | GetDataCentralTendencyType = UNSET,
    return_flags: Unset | bool = False,
    return_original_values: Unset | bool = False,
    return_suspect_data: Unset | bool = False,
) -> Any | list[StationDataDTO] | None:
    """Gets data for one or more stations

     Retrieves data for one or more stations

    Args:
        station_triplets (str):
        elements (str):
        duration (Union[Unset, GetDataDuration]):
        begin_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        insert_or_update_begin_date (Union[Unset, str]):
        period_ref (Union[Unset, GetDataPeriodRef]):
        central_tendency_type (Union[Unset, GetDataCentralTendencyType]):
        return_flags (Union[Unset, bool]):  Default: False.
        return_original_values (Union[Unset, bool]):  Default: False.
        return_suspect_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['StationDataDTO']]
    """

    return sync_detailed(
        client=client,
        station_triplets=station_triplets,
        elements=elements,
        duration=duration,
        begin_date=begin_date,
        end_date=end_date,
        insert_or_update_begin_date=insert_or_update_begin_date,
        period_ref=period_ref,
        central_tendency_type=central_tendency_type,
        return_flags=return_flags,
        return_original_values=return_original_values,
        return_suspect_data=return_suspect_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: str,
    elements: str,
    duration: Unset | GetDataDuration = UNSET,
    begin_date: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    insert_or_update_begin_date: Unset | str = UNSET,
    period_ref: Unset | GetDataPeriodRef = UNSET,
    central_tendency_type: Unset | GetDataCentralTendencyType = UNSET,
    return_flags: Unset | bool = False,
    return_original_values: Unset | bool = False,
    return_suspect_data: Unset | bool = False,
) -> Response[Any | list[StationDataDTO]]:
    """Gets data for one or more stations

     Retrieves data for one or more stations

    Args:
        station_triplets (str):
        elements (str):
        duration (Union[Unset, GetDataDuration]):
        begin_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        insert_or_update_begin_date (Union[Unset, str]):
        period_ref (Union[Unset, GetDataPeriodRef]):
        central_tendency_type (Union[Unset, GetDataCentralTendencyType]):
        return_flags (Union[Unset, bool]):  Default: False.
        return_original_values (Union[Unset, bool]):  Default: False.
        return_suspect_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['StationDataDTO']]]
    """

    kwargs = _get_kwargs(
        station_triplets=station_triplets,
        elements=elements,
        duration=duration,
        begin_date=begin_date,
        end_date=end_date,
        insert_or_update_begin_date=insert_or_update_begin_date,
        period_ref=period_ref,
        central_tendency_type=central_tendency_type,
        return_flags=return_flags,
        return_original_values=return_original_values,
        return_suspect_data=return_suspect_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: str,
    elements: str,
    duration: Unset | GetDataDuration = UNSET,
    begin_date: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    insert_or_update_begin_date: Unset | str = UNSET,
    period_ref: Unset | GetDataPeriodRef = UNSET,
    central_tendency_type: Unset | GetDataCentralTendencyType = UNSET,
    return_flags: Unset | bool = False,
    return_original_values: Unset | bool = False,
    return_suspect_data: Unset | bool = False,
) -> Any | list[StationDataDTO] | None:
    """Gets data for one or more stations

     Retrieves data for one or more stations

    Args:
        station_triplets (str):
        elements (str):
        duration (Union[Unset, GetDataDuration]):
        begin_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        insert_or_update_begin_date (Union[Unset, str]):
        period_ref (Union[Unset, GetDataPeriodRef]):
        central_tendency_type (Union[Unset, GetDataCentralTendencyType]):
        return_flags (Union[Unset, bool]):  Default: False.
        return_original_values (Union[Unset, bool]):  Default: False.
        return_suspect_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['StationDataDTO']]
    """

    return (
        await asyncio_detailed(
            client=client,
            station_triplets=station_triplets,
            elements=elements,
            duration=duration,
            begin_date=begin_date,
            end_date=end_date,
            insert_or_update_begin_date=insert_or_update_begin_date,
            period_ref=period_ref,
            central_tendency_type=central_tendency_type,
            return_flags=return_flags,
            return_original_values=return_original_values,
            return_suspect_data=return_suspect_data,
        )
    ).parsed
