# Dependencies Overview

This project separates runtime, development, and test dependencies.

## Runtime Dependencies

Runtime dependencies are listed in `requirements.txt` and should also be reflected in `custom_components/snotel/manifest.json` when Home Assistant must install them for end users.

Current runtime dependencies:

| Package        | Why it is used                                                 |
| -------------- | -------------------------------------------------------------- |
| `numpy`        | Coordinate math for nearest-station setup                      |
| `pandas`       | Tabular station metadata handling during nearest-station setup |
| `scikit-learn` | `BallTree` nearest-neighbor search using haversine distance    |

Home Assistant provides the shared async HTTP client used by `api_helper.py`.

## Development Dependencies

`requirements_dev.txt` contains additional local tooling used by the repository scripts, including Pyright and helper packages. The devcontainer bootstrap also installs Home Assistant Core development and pre-commit dependencies.

## Test Dependencies

`requirements_test.txt` contains custom-component test helpers. The project scripts install the broader Home Assistant test dependency set during bootstrap.

## Node Dependencies

`package.json` contains Markdown tooling such as Prettier and markdownlint. These are used by the repository's documentation lint scripts.

## Home Assistant and HACS Metadata

`hacs.json` declares minimum Home Assistant and HACS versions for HACS users.

`custom_components/snotel/manifest.json` declares Home Assistant integration metadata:

- Domain: `snotel`
- Integration type: `service`
- IoT class: `cloud_polling`
- Config flow: enabled

## Maintenance Rule

When adding a runtime dependency:

1. Add it to `requirements.txt`.
2. Add the same constraint to `manifest.json` under `requirements` if Home Assistant needs to install it for users.
3. Do not add runtime packages to development or test requirements unless they are also needed only by those workflows.
