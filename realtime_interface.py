class FeedMessage:
    def __init__(self, header, entity):
        self.header = header
        self.entity = entity

    def __repr__(self):
        return f"{self.header} {self.entity}"


class FeedHeader:
    def __init__(self, gtfs_realtime_version, incrementality, timestamp):
        self.gtfs_realtime_version = gtfs_realtime_version
        self.incrementality = incrementality
        self.timestamp = timestamp

    def __repr__(self):
        return f"{self.gtfs_realtime_version} {self.incrementality} {self.timestamp}"


class FeedEntity:
    def __init__(self, id, is_deleted, trip_update, vehicle, alert, shape):
        self.id = id
        self.is_deleted = is_deleted
        self.trip_update = trip_update
        self.vehicle = vehicle
        self.alert = alert
        self.shape = shape

    def __repr__(self):
        return f'''{self.id} {self.is_deleted} {self.trip_update} {self.vehicle} 
                   {self.alert} {self.shape}'''


class TripUpdate:
    def __init__(self, trip, vehicle, stop_time_update, timestamp, delay, trip_properties):
        self.trip = trip
        self.vehicle = vehicle
        self.stop_time_update = stop_time_update
        self.timestamp = timestamp
        self.delay = delay
        self.trip_properties = trip_properties

    def __repr__(self):
        return f'''{self.trip} {self.vehicle} {self.stop_time_update} {self.timestamp} {self.delay} 
                   {self.trip_properties}'''


class TripDescriptor:
    def __init__(self, trip_id, route_id, direction_id, start_time, start_date, schedule_relationship):
        self.trip_id = trip_id
        self.route_id = route_id
        self.direction_id = direction_id
        self.start_time = start_time
        self.start_date = start_date
        self.schedule_relationship = schedule_relationship

    def __repr__(self):
        return f'''{self.trip_id} {self.route_id} {self.direction_id} {self.start_time} 
                   {self.start_date} {self.schedule_relationship}'''



class VehiclePosition:
    def __init__(self, trip, vehicle, position, current_stop_sequence, stop_id,
                 current_status, timestamp, congestion_level, occupancy_status,
                 occupancy_percentage):
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


