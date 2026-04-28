"""Constants for snotel."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

# Integration metadata
DOMAIN = "snotel"
ATTRIBUTION = "Data provided by https://wcc.sc.egov.usda.gov/awdbRestApi"

# Platform parallel updates - applied to all platforms
PARALLEL_UPDATES = 1

# Default configuration values
DEFAULT_UPDATE_INTERVAL_HOURS = 1
DEFAULT_ENABLE_DEBUGGING = False

# setup type and values
CONF_SETUP_TYPE = "setup_type"
CONF_SETUP_TYPE_STATION_SEARCH = "station_search"
CONF_SETUP_TYPE_LAT_LONG = "lat_long"
CONF_SETUP_TYPE_STATION_TRIPLET = "station_triplet"

# the station code that everything uses
CONF_STATION_CODE = "station_code"
# station search result (a code, but in the form of a select)
CONF_STATION_SEARCH = "station_search"
