"""
API package for snotel.

Architecture:
    Three-layer data flow: Entities → Coordinator → API Client.
    Only the coordinator should call the API client. Entities must never
    import or call the API client directly.

Exception hierarchy:
    SnotelApiClientError (base)
    ├── SnotelApiClientCommunicationError (network/timeout)
    └── SnotelApiClientAuthenticationError (401/403)

Coordinator exception mapping:
    ApiClientAuthenticationError → ConfigEntryAuthFailed (triggers reauth)
    ApiClientCommunicationError → UpdateFailed (auto-retry)
    ApiClientError             → UpdateFailed (auto-retry)
"""

from .client import (
    SnotelApiClient,
    SnotelApiClientAuthenticationError,
    SnotelApiClientCommunicationError,
    SnotelApiClientError,
)

__all__ = [
    "SnotelApiClient",
    "SnotelApiClientAuthenticationError",
    "SnotelApiClientCommunicationError",
    "SnotelApiClientError",
]
