from realtime_interface import *
import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

def get(foo, attr):
    if attr in foo:
        return foo[attr]
    else:
        return None


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
        route_id = get(foo["trip"], "routeId")
        trip_id = get(foo["trip"], "tripId")
        schedule_relationship = get(foo["trip"], "scheduleRelationship")
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
        trip_update = TripUpdate(trip, vehicle, stop_time_update, timestamp, None, None)
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


def entity_get(foo, function):
    id_dict = dict()
    for entity in foo["entity"]:
        id = get(entity, "id")
        if function == "vehicle_position":
            vehicle_position = vehicle_position_get(entity)
            vehicle_id = vehicle_position.vehicle.id
            item = FeedEntity(id, None, None, vehicle_position, None, None)
            id_dict[vehicle_id] = item
        elif function == "trip_update":
            trip_update = trip_update_get(entity)
            trip_id = trip_update.trip.trip_id
            item = FeedEntity(id, None, trip_update, None, None, None)
            id_dict[trip_id] = item
    return id_dict


def header_get(foo):
    gtfs_realtime_version = foo["header"]["gtfsRealtimeVersion"]
    incrementality = foo["header"]["incrementality"]
    timestamp = foo["header"]["timestamp"]
    header = FeedHeader(gtfs_realtime_version, incrementality, timestamp)
    return header


def processing(foo, function):
    header = header_get(foo)
    entities = entity_get(foo, function)
    data = FeedMessage(header, entities)
    return data
