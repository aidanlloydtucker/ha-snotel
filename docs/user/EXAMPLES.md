# Examples

These examples use placeholder entity IDs. Replace them with the entity IDs Home Assistant created for your SNOTEL station.

## Dashboard Cards

### Station Summary

```yaml
type: entities
title: SNOTEL Station
entities:
  - entity: sensor.example_station_snow_depth
    name: Snow Depth
  - entity: sensor.example_station_snow_water_equivalent
    name: Snow Water Equivalent
  - entity: sensor.example_station_precip_accumulation_water_year
    name: Precipitation
  - entity: sensor.example_station_temperature
    name: Temperature
  - entity: sensor.example_station_last_updated
    name: Last Updated
```

### Snow Depth Graph

```yaml
type: history-graph
title: Snow Depth
entities:
  - sensor.example_station_snow_depth
hours_to_show: 72
```

### Weather Glance

```yaml
type: glance
title: Mountain Conditions
entities:
  - entity: sensor.example_station_temperature
    name: Temperature
  - entity: sensor.example_station_snow_depth
    name: Snow Depth
  - entity: sensor.example_station_snow_water_equivalent
    name: SWE
show_state: true
```

## Automations

### Notify When Snow Depth Exceeds a Threshold

```yaml
automation:
  - alias: "SNOTEL snow depth threshold"
    trigger:
      - trigger: numeric_state
        entity_id: sensor.example_station_snow_depth
        above: 24
    action:
      - action: notify.notify
        data:
          title: "SNOTEL snow depth"
          message: "Snow depth is now {{ states('sensor.example_station_snow_depth') }} inches."
```

### Notify On New Station Data

```yaml
automation:
  - alias: "SNOTEL data updated"
    trigger:
      - trigger: state
        entity_id: sensor.example_station_last_updated
    condition:
      - condition: template
        value_template: "{{ trigger.from_state is not none and trigger.to_state.state not in ['unknown', 'unavailable'] }}"
    action:
      - action: notify.notify
        data:
          title: "SNOTEL updated"
          message: >-
            Latest reading: {{ trigger.to_state.state }}.
            Snow depth is {{ states('sensor.example_station_snow_depth') }} in.
```

### Detect Freezing Observed Temperature

```yaml
automation:
  - alias: "SNOTEL observed temperature below freezing"
    trigger:
      - trigger: numeric_state
        entity_id: sensor.example_station_temperature
        below: 32
    action:
      - action: notify.notify
        data:
          title: "Freezing temperature"
          message: "Observed SNOTEL temperature is {{ states('sensor.example_station_temperature') }} °F."
```

## Template Sensor

### Snowpack Summary

```yaml
template:
  - sensor:
      - name: "SNOTEL Snowpack Summary"
        state: >-
          {{ states('sensor.example_station_snow_depth') }} in depth,
          {{ states('sensor.example_station_snow_water_equivalent') }} in SWE
```

## Related Documentation

- [Configuration Reference](./CONFIGURATION.md)
- [Getting Started](./GETTING_STARTED.md)
- [GitHub Issues](https://github.com/aidanlloydtucker/ha-snotel/issues)
