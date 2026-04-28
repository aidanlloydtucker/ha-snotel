# Working with AI Coding Agents

This repository is no longer an untouched blueprint. AI agents should treat it as a working SNOTEL integration and preserve the current Home Assistant architecture.

## Current Scope

The integration:

- Configures one USDA NRCS SNOTEL station per config entry.
- Uses the public AWDB REST API at `https://wcc.sc.egov.usda.gov/awdbRestApi`.
- Supports station search, nearest station by latitude/longitude, and manual station triplet setup.
- Polls hourly station data through `SnotelDataUpdateCoordinator`.
- Exposes only sensor entities today.

## Common Tasks

### Add an AWDB Sensor

1. Confirm the AWDB element code and duration to fetch.
2. Update `coordinator/base.py` if the coordinator needs to request another element.
3. Update `coordinator/data_processing.py` to map the element code to a coordinator key.
4. Add a `SensorEntityDescription` in `sensor/hourly.py` or a new focused sensor module.
5. Update `translations/en.json` and user docs.
6. Run `script/lint` and `script/type-check`.

### Adjust Setup Behavior

Config flow code is in `config_flow_handler/config_flow.py`. Form schemas are in `config_flow_handler/schemas/config.py`, and AWDB validation is in `config_flow_handler/validators/validate.py`.

Preserve the station triplet as the stable unique ID unless a migration plan is added.

### Debug Polling

Start with:

- `coordinator/base.py` for AWDB calls and update errors
- `coordinator/data_processing.py` for response validation and element mapping
- `config/home-assistant.log` for runtime failures

Use `./script/develop` to run Home Assistant locally.

## Guardrails

- Do not add generated template platforms such as switch, fan, button, select, or number unless there is real SNOTEL functionality behind them.
- Do not call the AWDB API directly from entities; entities read from `coordinator.data`.
- Do not create new top-level packages without updating `AGENTS.md`.
- Use the project scripts instead of raw `hass`, `pip`, or `pytest` commands.

## Validation

Use the repository scripts:

```bash
script/lint
script/type-check
script/test
script/hassfest
```

For documentation-only changes, run:

```bash
script/markdown
```
