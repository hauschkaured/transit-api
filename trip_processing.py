from realtime_interface import *


def trip_update_processing(foo):


def vehicle_position_processing(foo):
    print(foo)


def trip_processing(foo):
    # Entity
    entity = foo["entity"]
    for entity in entity:
        id = entity["id"]
        if "isDeleted" in entity:
            is_deleted = entity["isDeleted"]
        if "tripUpdate" in entity:
            trip_update = trip_update_processing(entity["tripUpdate"])
        elif "vehiclePosition" in entity:
            vehicle_position = vehicle_position_processing(entity["vehiclePosition"])



    # Header
    gtfs_realtime_version = foo["header"]["gtfsRealtimeVersion"]
    incrementality = foo["header"]["incrementality"]
    timestamp = foo["header"]["timestamp"]
    header = FeedHeader(gtfs_realtime_version, incrementality, timestamp)
    # Dataset



