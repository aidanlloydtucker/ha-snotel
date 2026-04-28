# SNOTEL

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

Home Assistant custom integration for USDA NRCS SNOTEL station data.

The integration polls the public AWDB REST API and creates Home Assistant sensors for the latest hourly snow and weather measurements at a configured SNOTEL station.

## Features

- UI-only setup; no YAML configuration required
- Configure a station by searching, entering a station triplet, or choosing the nearest station to a latitude/longitude
- Hourly polling from the USDA NRCS AWDB REST API
- One Home Assistant device per configured SNOTEL station
- Sensor entities for precipitation, snow depth, snow water equivalent, observed temperature, and last update time

## Platforms

| Platform | Description                                                  |
| -------- | ------------------------------------------------------------ |
| `sensor` | Latest hourly SNOTEL measurements for the configured station |

## Installation

### HACS

1. Open HACS in Home Assistant.
2. Go to **Integrations**.
3. Open the three-dot menu and choose **Custom repositories**.
4. Add `https://github.com/aidanlloydtucker/ha-snotel` as an **Integration** repository.
5. Download **SNOTEL**.
6. Restart Home Assistant.

### Manual

1. Download this repository.
2. Copy `custom_components/snotel/` into the `custom_components/` directory in your Home Assistant configuration folder.
3. Restart Home Assistant.

## Setup

After installation and restart:

1. Go to **Settings** → **Devices & Services**.
2. Select **Add Integration**.
3. Search for **SNOTEL**.
4. Choose one setup method:
   - **Search for a station**: Select a station from the AWDB station list.
   - **Closest station to a given latitude/longitude**: Enter coordinates and the integration selects the nearest station.
   - **Manually specified station triplet**: Enter a station triplet such as `539:CO:SNTL`.

The station triplet is used as the config entry unique ID, so the same station cannot be added twice.

## Entities

Each configured station creates these sensors:

| Entity                           | Unit      | Description                                                |
| -------------------------------- | --------- | ---------------------------------------------------------- |
| Precip Accumulation (Water Year) | in        | Hourly `PREC` value, water-year accumulated precipitation  |
| Snow Depth                       | in        | Hourly `SNWD` snow depth                                   |
| Temperature                      | °F        | Hourly `TOBS` observed air temperature                     |
| Snow Water Equivalent            | in        | Hourly `WTEQ` snow water equivalent                        |
| Last Updated                     | timestamp | Most recent timestamp returned by the station data payload |

All sensors use the configured station as a service device named `SNOTEL: <station title>`.

## Data Source

Data is provided by the USDA NRCS AWDB REST API:

`https://wcc.sc.egov.usda.gov/awdbRestApi`

The integration currently requests hourly `PREC`, `SNWD`, `TOBS`, and `WTEQ` values for the configured station and refreshes once per hour.

## Troubleshooting

If setup fails, verify the station triplet exists in AWDB and that Home Assistant can reach `wcc.sc.egov.usda.gov`.

If entities are unavailable, check **Settings** → **System** → **Logs** for `custom_components.snotel` messages. You can enable debug logging with:

```yaml
logger:
  default: info
  logs:
    custom_components.snotel: debug
```

## Development

Use the project scripts for local development. They manage the Home Assistant environment and validation tooling:

```bash
./script/develop
script/lint
script/type-check
script/test
```

More project documentation is available in [`docs/user`](docs/user) and [`docs/development`](docs/development).

## Contributing

Contributions are welcome. Please open an issue or pull request if you find a station edge case, API behavior change, or Home Assistant compatibility issue.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

[commits-shield]: https://img.shields.io/github/commit-activity/y/aidanlloydtucker/ha-snotel.svg?style=for-the-badge
[commits]: https://github.com/aidanlloydtucker/ha-snotel/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/aidanlloydtucker/ha-snotel.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40aidanlloydtucker-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/aidanlloydtucker/ha-snotel.svg?style=for-the-badge
[releases]: https://github.com/aidanlloydtucker/ha-snotel/releases
