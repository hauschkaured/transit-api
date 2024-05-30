from realtime_interface import *

def get(foo, attr):
    if attr in foo:
        return foo[attr]
    else:
        return "None"


def arrival_get(foo):
    if "arrival" in foo:
        time = get(foo["arrival"], "time")
        arrival = StopTimeEvent(None, time, None)
        return arrival
    else:
        return None


def departure_get(foo):
    if "departure" in foo:
        time = get(foo["departure"], "time")
        departure = StopTimeEvent(None, time, None)
        return departure
    else:
        return None


def position_get(foo):
    if "position" in foo:
        bearing = get(foo["position"], "bearing")
        latitude = get(foo["position"], "latitude")
        longitude = get(foo["position"], "longitude")
        speed = get(foo["position"], "speed")
        position = Position(bearing, latitude, longitude, None, speed)
        return position
    else:
        return None


def vehicle_get(foo):
    if "vehicle" in foo:
        id = get(foo["vehicle"], "id")
        vehicle = VehicleDescriptor(id, None, None, None)
        return vehicle
    else:
        return None


def stop_time_update_get(foo):
    if "stopTimeUpdate" in foo:
        stop_time_list = []
        for i in foo["stopTimeUpdate"]:
            arrival = arrival_get(i)
            departure = departure_get(i)
            schedule_relationship = get(i, "scheduleRelationship")
            stop_id = get(i, "stopId")
            stop_sequence = get(i, "stopSequence")
            obj = StopTimeUpdate(stop_sequence, stop_id, arrival, departure,
                                 None, schedule_relationship,
                                 None)
            stop_time_list.append(obj)
        return stop_time_list
    else:
        return None


def trip_get(foo):
    if "trip" in foo:
        route_id = get(foo["trip"], "route_id")
        trip_id = get(foo["trip"], "trip_id")
        schedule_relationship = get(foo["trip"], "schedule_relationship")
        trip = TripDescriptor(trip_id, route_id, None, None, None, schedule_relationship)
        return trip
    else:
        return None


def trip_update_get(foo):
    if "tripUpdate" in foo:
        stop_time_update = stop_time_update_get(foo["tripUpdate"])
        timestamp = get(foo["tripUpdate"], "timestamp")
        trip = trip_get(foo["tripUpdate"])
        vehicle = vehicle_get(foo["tripUpdate"])
        trip_update = TripUpdate(stop_time_update, trip, timestamp, vehicle, None, None)
        return trip_update
    else:
        return None


def vehicle_position_get(foo):
    if "vehicle" in foo:
        position = position_get(foo["vehicle"])
        timestamp = get(foo["vehicle"], "timestamp")
        trip = trip_get(foo["vehicle"])
        vehicle = vehicle_get(foo["vehicle"])
        current_stop_sequence = get(foo["vehicle"], "currentStopSequence")
        stop_id = get(foo["vehicle"], "stopId")
        current_status = get(foo["vehicle"], "currentStatus")
        vehicle_position = VehiclePosition(trip, vehicle, position, current_stop_sequence, stop_id, current_status,
                                           timestamp, None, None, None, None)
        return vehicle_position
    else:
        return None


def entity_get(foo):
    id_dict = dict()
    for entity in foo["entity"]:
        id = get(entity, "id")
        vehicle_position = vehicle_position_get(entity)
        trip_update = trip_update_get(entity)
        item = FeedEntity(id, None, vehicle_position, trip_update, None, None)
        id_dict[id] = item
    return id_dict


def header_get(foo):
    gtfs_realtime_version = foo["header"]["gtfsRealtimeVersion"]
    incrementality = foo["header"]["incrementality"]
    timestamp = foo["header"]["timestamp"]
    header = FeedHeader(gtfs_realtime_version, incrementality, timestamp)
    return header


def processing(foo):
    header = header_get(foo)
    entities = entity_get(foo)

    data = FeedMessage(header, entities)
    return data

    # Dataset
