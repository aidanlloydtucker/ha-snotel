from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, SnotelAPIClient
from ...models.forecast_dto import ForecastDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    station_triplets: str,
    element_codes: Unset | str = UNSET,
    begin_publication_date: Unset | str = UNSET,
    end_publication_date: Unset | str = UNSET,
    exceedence_probabilities: Unset | str = UNSET,
    forecast_periods: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["stationTriplets"] = station_triplets

    params["elementCodes"] = element_codes

    params["beginPublicationDate"] = begin_publication_date

    params["endPublicationDate"] = end_publication_date

    params["exceedenceProbabilities"] = exceedence_probabilities

    params["forecastPeriods"] = forecast_periods

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/v1/forecasts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | SnotelAPIClient, response: httpx.Response
) -> Any | list[ForecastDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ForecastDTO.from_dict(response_200_item_data)

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
) -> Response[Any | list[ForecastDTO]]:
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
    element_codes: Unset | str = UNSET,
    begin_publication_date: Unset | str = UNSET,
    end_publication_date: Unset | str = UNSET,
    exceedence_probabilities: Unset | str = UNSET,
    forecast_periods: Unset | str = UNSET,
) -> Response[Any | list[ForecastDTO]]:
    """Gets forecast data for one or more stations

     Retrieves forecast data for one or more stations

    Args:
        station_triplets (str):
        element_codes (Union[Unset, str]):
        begin_publication_date (Union[Unset, str]):
        end_publication_date (Union[Unset, str]):
        exceedence_probabilities (Union[Unset, str]):
        forecast_periods (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ForecastDTO']]]
    """

    kwargs = _get_kwargs(
        station_triplets=station_triplets,
        element_codes=element_codes,
        begin_publication_date=begin_publication_date,
        end_publication_date=end_publication_date,
        exceedence_probabilities=exceedence_probabilities,
        forecast_periods=forecast_periods,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: str,
    element_codes: Unset | str = UNSET,
    begin_publication_date: Unset | str = UNSET,
    end_publication_date: Unset | str = UNSET,
    exceedence_probabilities: Unset | str = UNSET,
    forecast_periods: Unset | str = UNSET,
) -> Any | list[ForecastDTO] | None:
    """Gets forecast data for one or more stations

     Retrieves forecast data for one or more stations

    Args:
        station_triplets (str):
        element_codes (Union[Unset, str]):
        begin_publication_date (Union[Unset, str]):
        end_publication_date (Union[Unset, str]):
        exceedence_probabilities (Union[Unset, str]):
        forecast_periods (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ForecastDTO']]
    """

    return sync_detailed(
        client=client,
        station_triplets=station_triplets,
        element_codes=element_codes,
        begin_publication_date=begin_publication_date,
        end_publication_date=end_publication_date,
        exceedence_probabilities=exceedence_probabilities,
        forecast_periods=forecast_periods,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: str,
    element_codes: Unset | str = UNSET,
    begin_publication_date: Unset | str = UNSET,
    end_publication_date: Unset | str = UNSET,
    exceedence_probabilities: Unset | str = UNSET,
    forecast_periods: Unset | str = UNSET,
) -> Response[Any | list[ForecastDTO]]:
    """Gets forecast data for one or more stations

     Retrieves forecast data for one or more stations

    Args:
        station_triplets (str):
        element_codes (Union[Unset, str]):
        begin_publication_date (Union[Unset, str]):
        end_publication_date (Union[Unset, str]):
        exceedence_probabilities (Union[Unset, str]):
        forecast_periods (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ForecastDTO']]]
    """

    kwargs = _get_kwargs(
        station_triplets=station_triplets,
        element_codes=element_codes,
        begin_publication_date=begin_publication_date,
        end_publication_date=end_publication_date,
        exceedence_probabilities=exceedence_probabilities,
        forecast_periods=forecast_periods,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    station_triplets: str,
    element_codes: Unset | str = UNSET,
    begin_publication_date: Unset | str = UNSET,
    end_publication_date: Unset | str = UNSET,
    exceedence_probabilities: Unset | str = UNSET,
    forecast_periods: Unset | str = UNSET,
) -> Any | list[ForecastDTO] | None:
    """Gets forecast data for one or more stations

     Retrieves forecast data for one or more stations

    Args:
        station_triplets (str):
        element_codes (Union[Unset, str]):
        begin_publication_date (Union[Unset, str]):
        end_publication_date (Union[Unset, str]):
        exceedence_probabilities (Union[Unset, str]):
        forecast_periods (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ForecastDTO']]
    """

    return (
        await asyncio_detailed(
            client=client,
            station_triplets=station_triplets,
            element_codes=element_codes,
            begin_publication_date=begin_publication_date,
            end_publication_date=end_publication_date,
            exceedence_probabilities=exceedence_probabilities,
            forecast_periods=forecast_periods,
        )
    ).parsed
