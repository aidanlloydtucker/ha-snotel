# Configuration Reference

SNOTEL is configured entirely through the Home Assistant UI. YAML configuration is not supported.

## Setup Methods

### Search for a Station

The integration fetches AWDB station metadata and shows available stations in a dropdown. The selected station triplet is stored in the config entry as `station_code`.

### Closest Station to Latitude/Longitude

The integration fetches AWDB station metadata, filters stations with coordinates, and uses a haversine nearest-neighbor search to find the closest station.

| Field     | Type   | Required | Default                  |
| --------- | ------ | -------- | ------------------------ |
| Latitude  | number | Yes      | Home Assistant latitude  |
| Longitude | number | Yes      | Home Assistant longitude |

The original coordinates are stored in the config entry for reference, but polling uses the selected station triplet.

### Manual Station Triplet

Use this when you already know the AWDB station triplet.

| Field           | Type   | Required | Example       |
| --------------- | ------ | -------- | ------------- |
| Station Triplet | string | Yes      | `539:CO:SNTL` |

The integration validates the station with AWDB before saving the entry.

## Config Entry Data

The current config entry data contains:

| Key            | Description                                               |
| -------------- | --------------------------------------------------------- |
| `setup_type`   | One of `station_search`, `lat_long`, or `station_triplet` |
| `station_code` | AWDB station triplet used for all API calls               |
| `latitude`     | Stored only for latitude/longitude setup                  |
| `longitude`    | Stored only for latitude/longitude setup                  |

The station triplet is slugified and used as the config entry unique ID to prevent duplicate entries for the same station.

## Polling

The integration polls once per hour. The coordinator requests hourly data with:

- Station triplet: configured `station_code`
- Elements: `PREC,SNWD,TOBS,WTEQ`
- Duration: hourly
- Begin date: `0`, which asks AWDB for the latest available values

## Entities

| Sensor                           | Source element            | Unit      | State class | Device class  |
| -------------------------------- | ------------------------- | --------- | ----------- | ------------- |
| Precip Accumulation (Water Year) | `PREC`                    | in        | total       | precipitation |
| Snow Depth                       | `SNWD`                    | in        | measurement | precipitation |
| Temperature                      | `TOBS`                    | °F        | measurement | temperature   |
| Snow Water Equivalent            | `WTEQ`                    | in        | measurement | precipitation |
| Last Updated                     | latest returned timestamp | timestamp | none        | timestamp     |

The measurement sensors expose a `last_updated` attribute with the coordinator timestamp.

## Device

All entities for a station are grouped under one Home Assistant device:

| Field        | Value                                  |
| ------------ | -------------------------------------- |
| Name         | `SNOTEL: <station title>`              |
| Manufacturer | Natural Resources Conservation Service |
| Entry type   | Service                                |

## Services

This integration does not currently register custom services.

## Diagnostics

Diagnostics support is present in the integration. Download diagnostics from **Settings** → **Devices & Services** → **SNOTEL** when reporting issues. Review diagnostics before sharing publicly.

## Related Documentation

- [Getting Started](./GETTING_STARTED.md)
- [Examples](./EXAMPLES.md)
- [GitHub Issues](https://github.com/aidanlloydtucker/ha-snotel/issues)
