# Architectural and Design Decisions

This document records significant architectural and design decisions made during development.

## Decision Log

### Use the Public AWDB REST API Directly

**Date:** 2026-04-28

**Context:** SNOTEL data is exposed through the USDA NRCS AWDB REST API. The integration needs station metadata and recent station observations.

**Decision:** Use the AWDB REST API directly through a generated async client stored in `custom_components/snotel/snotel_api/`.

**Rationale:**

- AWDB already exposes the data needed by the integration.
- A generated client gives typed models for a large API surface.
- The generated client can be isolated from hand-written Home Assistant integration code.

**Consequences:**

- Generated code is excluded from lint and type-checking.
- Integration code should keep AWDB-specific transformation in coordinator/data processing modules.
- API model changes may require regenerating or updating the generated client.

---

### One Config Entry per Station

**Date:** 2026-04-28

**Context:** Users may want to monitor one or more SNOTEL stations. AWDB station triplets are stable station identifiers.

**Decision:** Each config entry represents exactly one station, and the station triplet is used as the unique ID.

**Rationale:**

- Matches Home Assistant's config entry and device model cleanly.
- Prevents duplicate setup of the same station.
- Keeps coordinator data simple: one station payload per entry.

**Consequences:**

- Monitoring multiple stations requires multiple config entries.
- A future multi-station entry model would be a breaking architectural change.

---

### Provide Three Setup Paths

**Date:** 2026-04-28

**Context:** Some users know the exact station triplet, while others know only a station name or an area.

**Decision:** Support station search, nearest station from latitude/longitude, and manual station triplet setup.

**Rationale:**

- Station search helps users who know a station name.
- Latitude/longitude setup is convenient for users who care about a location instead of a specific station.
- Manual station triplet setup keeps advanced users in control.

**Consequences:**

- Config flow setup depends on fetching AWDB station metadata.
- Latitude/longitude setup requires `numpy`, `pandas`, and `scikit-learn` at runtime.

---

### Use DataUpdateCoordinator for Polling

**Date:** 2026-04-28

**Context:** Multiple sensors share the same station data and should refresh on the same schedule.

**Decision:** Use a single `DataUpdateCoordinator` per station config entry.

**Rationale:**

- Prevents duplicate API calls for each entity.
- Follows Home Assistant's standard polling integration pattern.
- Provides shared availability and error handling behavior.

**Consequences:**

- All station entities share a one-hour refresh cadence.
- Entities must read from `coordinator.data` rather than calling AWDB directly.

---

### Start with Hourly Sensor Entities Only

**Date:** 2026-04-28

**Context:** The current implementation fetches latest hourly observation values for weather and snowpack measurements.

**Decision:** Implement only the sensor platform for `PREC`, `SNWD`, `TOBS`, `WTEQ`, and the latest timestamp.

**Rationale:**

- These entities map directly to AWDB data currently fetched by the coordinator.
- Sensors are the appropriate Home Assistant platform for read-only station measurements.
- Avoids template-generated control platforms that do not apply to SNOTEL data.

**Consequences:**

- There are no switches, buttons, selects, numbers, fans, or binary sensors.
- Adding daily values, forecasts, or additional elements should extend the coordinator mapping and sensor descriptions.

## Future Considerations

### Additional AWDB Elements

Add more sensors for daily values or other AWDB element codes once the coordinator supports fetching and transforming them.

### Configurable Polling or Elements

An options flow could let users choose update interval or enabled AWDB elements. This is not implemented today.

### Station Metadata in Device Info

The base device could expose model, configuration URL, or additional metadata if AWDB provides stable values suitable for Home Assistant device info.
