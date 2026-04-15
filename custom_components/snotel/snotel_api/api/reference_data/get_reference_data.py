from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, SnotelAPIClient
from ...models.reference_data_dto import ReferenceDataDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    reference_lists: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["referenceLists"] = reference_lists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/v1/reference-data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | SnotelAPIClient, response: httpx.Response
) -> Any | ReferenceDataDTO | None:
    if response.status_code == 200:
        response_200 = ReferenceDataDTO.from_dict(response.json())

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
) -> Response[Any | ReferenceDataDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    reference_lists: Unset | str = UNSET,
) -> Response[Any | ReferenceDataDTO]:
    """Gets reference data

     Retrieves one or more types of reference data

    Args:
        reference_lists (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReferenceDataDTO]]
    """

    kwargs = _get_kwargs(
        reference_lists=reference_lists,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    reference_lists: Unset | str = UNSET,
) -> Any | ReferenceDataDTO | None:
    """Gets reference data

     Retrieves one or more types of reference data

    Args:
        reference_lists (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReferenceDataDTO]
    """

    return sync_detailed(
        client=client,
        reference_lists=reference_lists,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    reference_lists: Unset | str = UNSET,
) -> Response[Any | ReferenceDataDTO]:
    """Gets reference data

     Retrieves one or more types of reference data

    Args:
        reference_lists (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReferenceDataDTO]]
    """

    kwargs = _get_kwargs(
        reference_lists=reference_lists,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | SnotelAPIClient,
    reference_lists: Unset | str = UNSET,
) -> Any | ReferenceDataDTO | None:
    """Gets reference data

     Retrieves one or more types of reference data

    Args:
        reference_lists (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReferenceDataDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            reference_lists=reference_lists,
        )
    ).parsed
