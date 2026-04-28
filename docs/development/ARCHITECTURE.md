# Architecture Overview

This document describes the current architecture of the SNOTEL custom integration.

## Directory Structure

```text
custom_components/snotel/
├── __init__.py                    # Config entry setup, coordinator creation, platform forwarding
├── api_helper.py                  # Home Assistant httpx client wiring for AWDB
├── config_flow.py                 # Home Assistant config flow entry point
├── const.py                       # Domain, config keys, defaults, attribution
├── data.py                        # Typed runtime_data dataclass
├── diagnostics.py                 # Diagnostics support
├── manifest.json                  # Integration metadata
├── config_flow_handler/
│   ├── config_flow.py             # User setup flow and station selection logic
│   ├── handler.py                 # Compatibility export for the flow handler
│   ├── schemas/config.py          # Voluptuous schemas for setup forms
│   └── validators/validate.py     # AWDB station validation
├── coordinator/
│   ├── base.py                    # SnotelDataUpdateCoordinator
│   ├── data_processing.py         # AWDB response validation and transformation
│   └── error_handling.py          # Shared coordinator error helpers
├── entity/
│   └── base.py                    # Common CoordinatorEntity base
├── sensor/
│   ├── __init__.py                # Sensor platform setup
│   └── hourly.py                  # Hourly sensor descriptions and entity class
└── snotel_api/                    # Generated AWDB REST API client and models
```

## Integration Type

SNOTEL is a `service` integration with `cloud_polling` IoT class. Each config entry represents one public USDA NRCS SNOTEL station, identified by its AWDB station triplet.

## Data Source

The integration talks to:

```text
https://wcc.sc.egov.usda.gov/awdbRestApi
```

The generated `snotel_api/` client handles endpoint models and request helpers. `api_helper.py` creates the generated client and attaches Home Assistant's shared async `httpx` client.

## Config Flow

The config flow lives in `config_flow_handler/config_flow.py` and supports three setup methods:

| Setup type        | Behavior                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------- |
| `station_search`  | Fetch all AWDB stations and present a dropdown of station names                           |
| `lat_long`        | Fetch stations with coordinates and choose the nearest station using a haversine BallTree |
| `station_triplet` | Validate a manually entered AWDB station triplet                                          |

All paths validate the station through AWDB before creating an entry. The slugified station triplet is used as the unique ID, which prevents duplicate entries for the same station.

## Runtime Data

`SnotelData` is stored on `entry.runtime_data` after setup. It contains:

- `client`: Generated `SnotelAPIClient`
- `coordinator`: `SnotelDataUpdateCoordinator`
- `integration`: Loaded Home Assistant integration metadata

## Coordinator

`SnotelDataUpdateCoordinator` is the single polling layer for a config entry.

During `_async_setup()`, it fetches station metadata for the configured station and stores the station timezone.

During `_async_update_data()`, it fetches latest hourly station data:

- Elements: `PREC,SNWD,TOBS,WTEQ`
- Duration: hourly
- Begin date: `0`

The coordinator refreshes once per hour and uses `always_update=False` so unchanged data does not force entity writes.

## Data Transformation

`coordinator/data_processing.py` validates the generated AWDB response shape, maps AWDB element codes to entity keys, and converts the latest AWDB timestamp into a timezone-aware Python `datetime`.

Current element mapping:

| AWDB code | Coordinator key         |
| --------- | ----------------------- |
| `PREC`    | `precip_accumulation`   |
| `SNWD`    | `snow_depth`            |
| `TOBS`    | `temperature`           |
| `WTEQ`    | `snow_water_equivalent` |

## Entities

Only the `sensor` platform is currently implemented.

`sensor/hourly.py` defines five entities:

- Precip Accumulation (Water Year)
- Snow Depth
- Temperature
- Snow Water Equivalent
- Last Updated

Each entity inherits from Home Assistant's `SensorEntity` and the integration `SnotelEntity` base. Entities read exclusively from `coordinator.data`.

## Device Model

`SnotelEntity` groups each station under one Home Assistant service device:

- Identifier: `(snotel, config_entry.entry_id)`
- Name: `SNOTEL: <config entry title>`
- Manufacturer: `Natural Resources Conservation Service`
- Entry type: `service`

## Data Flow

```text
Config Flow
    │
    ▼
Config Entry with station_code
    │
    ▼
SnotelDataUpdateCoordinator
    │
    ├── AWDB station metadata during setup
    └── AWDB hourly data every hour
    │
    ▼
coordinator.data
    │
    ▼
Sensor entities
```

## Development Notes

- Use project scripts for local runs and validation; do not call raw `hass`, `pip`, or `pytest` commands.
- The generated `snotel_api/` package is excluded from Ruff and Pyright checks.
- There are no custom services, options flow, repair flow, or non-sensor platforms at this time.
