class FeedMessage:
    def __init__(self, header, entity):
        self.header = header
        self.entity = entity

    def __repr__(self):
        return f"FEEDMESSAGE {self.header} {self.entity}"


class FeedHeader:
    def __init__(self, gtfs_realtime_version, incrementality, timestamp):
        self.gtfs_realtime_version = gtfs_realtime_version
        self.incrementality = incrementality
        self.timestamp = timestamp

    def __repr__(self):
        return f"FEEDHEADER {self.gtfs_realtime_version} {self.incrementality} {self.timestamp} END"


class FeedEntity:
    def __init__(self, id, is_deleted, trip_update, vehicle, alert, shape):
        self.id = id
        self.is_deleted = is_deleted
        self.trip_update = trip_update
        self.vehicle = vehicle
        self.alert = alert
        self.shape = shape

    def __repr__(self):
        return f'''FEEDENTITY {self.id} {self.is_deleted} {self.trip_update} {self.vehicle} 
                   {self.alert} {self.shape} END'''
    
    def fields(self):
        if self.trip_update != None:
            return f"ID and Trip Update"
        elif self.vehicle != None:
            return f"ID and Vehicle"


class TripUpdate:
    def __init__(self, trip, vehicle, stop_time_update, timestamp, delay, trip_properties):
        self.trip = trip
        self.vehicle = vehicle
        self.stop_time_update = stop_time_update
        self.timestamp = timestamp
        self.delay = delay
        self.trip_properties = trip_properties

    def __repr__(self):
        return f'''TRIPUPDATE {self.trip} {self.vehicle} {self.stop_time_update} {self.timestamp} {self.delay} 
                   {self.trip_properties} END'''


class TripDescriptor:
    def __init__(self, trip_id, route_id, direction_id, start_time, start_date, schedule_relationship):
        self.trip_id = trip_id
        self.route_id = route_id
        self.direction_id = direction_id
        self.start_time = start_time
        self.start_date = start_date
        self.schedule_relationship = schedule_relationship

    def __repr__(self):
        return f'''TRIPDESCRIPTOR {self.trip_id} {self.route_id} {self.direction_id} {self.start_time} 
                   {self.start_date} {self.schedule_relationship} END'''


class VehiclePosition:
    def __init__(self, trip, vehicle, position, current_stop_sequence, stop_id,
                 current_status, timestamp, congestion_level, occupancy_status,
                 occupancy_percentage, multi_carriage_details):
        self.trip = trip
        self.vehicle = vehicle
        self.position = position
        self.current_stop_sequence = current_stop_sequence
        self.stop_id = stop_id
        self.current_status = current_status
        self.timestamp = timestamp
        self.congestion_level = congestion_level
        self.occupancy_status = occupancy_status
        self.occupancy_percentage = occupancy_percentage
        self.multi_carriage_details = multi_carriage_details

    def __repr__(self):
        return f'''VEHICLEPOSITION {self.trip} {self.vehicle} {self.position} {self.current_stop_sequence} 
        {self.stop_id} {self.current_status} {self.timestamp} END'''


class VehicleDescriptor:
    def __init__(self, id, label, license_plate, wheelchair_accessible):
        self.id = id
        self.label = label
        self.license_plate = license_plate
        self.wheelchair_accessible = wheelchair_accessible

    def __repr__(self):
        return f"VEHICLEDESCRIPTOR {self.id} END"


class StopTimeUpdate:
    def __init__(self, stop_sequence, stop_id, arrival, departure, departure_occupancy_status, 
                 schedule_relationship, stop_time_properties):
        self.stop_sequence = stop_sequence
        self.stop_id = stop_id
        self.arrival = arrival
        self.departure = departure
        self.departure_occupancy_status = departure_occupancy_status
        self.schedule_relationship = schedule_relationship
        self.stop_time_properties = stop_time_properties

    def __repr__(self):
        return f'''STOPTIMEUPDATE {self.stop_sequence} {self.stop_id} {self.arrival} {self.departure}
                   {self.departure_occupancy_status} {self.schedule_relationship} {self.stop_time_properties} END'''


class StopTimeEvent:
    def __init__(self, delay, time, uncertainty):
        self.delay = delay
        self.time = time
        self.uncertainty = uncertainty

    def __repr__(self):
        return f"STOPTIMEEVENT {self.delay} {self.time} {self.uncertainty} END"


class Position:
    def __init__(self, latitude, longitude, bearing, odometer, speed):
        self.latitude = latitude
        self.longitude = longitude
        self.bearing = bearing
        self.odometer = odometer
        self.speed = speed

    def __repr__(self):
        return f"POSITION {self.latitude} {self.longitude} {self.bearing} {self.odometer} {self.speed} END"
