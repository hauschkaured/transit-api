import os

# These vals are for determining the path of the src directory
# This is so we don't encounter issues with relative pathing
_MOD_ROOT: str = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT: str = _MOD_ROOT[:_MOD_ROOT.rfind('/')]

# GTFS
GTFS_STATIC_AGENCY: str = "agency.txt"
GTFS_STATIC_CALENDAR_DATES: str = "calendar_dates.txt"
GTFS_STATIC_CALENDAR: str = "calendar.txt"
GTFS_STATIC_FARE_ATTR: str = "fare_attributes.txt"
GTFS_STATIC_FARE_RULES: str = "fare_rules.txt"
GTFS_STATIC_FEED_INFO: str = "feed_info.txt"
GTFS_STATIC_ROUTES: str = "routes.txt"
GTFS_STATIC_SHAPES: str = "shapes.txt"
GTFS_STATIC_STOP_TIMES: str = "stop_times.txt"
GTFS_STATIC_STOPS: str = "stops.txt"
GTFS_STATIC_TRANSFERS: str = "transfers.txt"
GTFS_STATIC_TRIPS: str = "trips.txt"


# PITTSBURGH: values and constants
PITTSBURGH_DIR: str = 'pittsburgh'
PITTSBURGH_GTFS: str = os.path.join(SRC_ROOT, PITTSBURGH_DIR, 'gtfs_static_feed')
PITTSBURGH_RT_BUS_VEHICLEPOSITION: str = "https://truetime.portauthority.org/gtfsrt-bus/vehicles"
PITTSBURGH_RT_BUS_TRIPUPDATE: str = "https://truetime.portauthority.org/gtfsrt-bus/trips"
PITTSBURGH_RT_BUS_ALERTS: str = "https://truetime.portauthority.org/gtfsrt-bus/alerts"
PITTSBURGH_RT_TRAIN_VEHICLEPOSITION: str = "https://truetime.portauthority.org/gtfsrt-train/vehicles"
PITTSBURGH_RT_TRAIN_TRIPUPDATE: str = "https://truetime.portauthority.org/gtfsrt-train/trips"
PITTSBURGH_RT_TRAIN_ALERTS: str = "https://truetime.portauthority.org/gtfsrt-train/alerts"

# SAN ANTONIO: values and constants
SAN_ANTONIO_DIR: str = 'san_antonio'
SAN_ANTONIO_GTFS: str = os.path.join(SRC_ROOT, SAN_ANTONIO_DIR, 'gtfs_static_feed')
SAN_ANTONIO_RT_VEHICLEPOSITION: str = "http://gtfs.viainfo.net/vehicle/vehiclepositions.pb"
SAN_ANTONIO_RT_TRIPUPDATE: str = "http://gtfs.viainfo.net/tripupdate/tripupdates.pb"
SAN_ANTONIO_RT_ALERTS: str = "http://gtfs.viainfo.net/alert/alerts.pb"

