# Extending SNOTEL

This document describes practical extension points for the current SNOTEL integration.

## Add More Station Measurements

The current coordinator requests hourly `PREC`, `SNWD`, `TOBS`, and `WTEQ` values.

To add another AWDB element:

1. Add the element code to the `elements` argument in `coordinator/base.py`.
2. Map the AWDB element code in `coordinator/data_processing.py`.
3. Add a sensor description in `sensor/hourly.py` or split sensors into a new module if the file grows.
4. Add the entity translation in `translations/en.json`.
5. Update user documentation with the new entity.

## Add Daily Data

Daily data should be modeled deliberately instead of mixing unrelated durations into the current hourly transform.

Recommended approach:

1. Add a new coordinator transform for daily data.
2. Decide whether hourly and daily values belong in the same coordinator payload or separate keys.
3. Add daily sensor descriptions in a dedicated module such as `sensor/daily.py`.
4. Keep entity unique IDs stable once released.

## Add an Options Flow

Useful future options could include:

- Polling interval
- Enabled AWDB elements
- Hourly vs daily data selection

If implemented, add an options flow under `config_flow_handler/`, wire it from the config flow handler, and make sure changes reload the config entry.

## Add More Station Metadata

Station metadata is loaded during coordinator setup. If additional metadata is useful:

- Store it on the coordinator.
- Expose stable values through device info or entity attributes.
- Avoid exposing location data in diagnostics unless it is intentionally redacted or safe to share.

## Generated AWDB Client

The `snotel_api/` package is generated and excluded from lint/type checks. Keep hand-written Home Assistant logic outside that package when possible. If the AWDB API schema changes, regenerate or update the client separately from integration behavior changes.

## Local Hooks

The repository supports optional `script/hooks/` and `.devcontainer/hooks/` shell hooks around development scripts. Use them for local-only workflow customizations, not core integration behavior.
