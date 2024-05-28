class Agency:
    def __init__(self, agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone, agency_fare_url):
        self.agency_id = agency_id
        self.agency_name = agency_name
        self.agency_url = agency_url
        self.agency_timezone = agency_timezone
        self.agency_lang = agency_lang
        self.agency_phone = agency_phone
        self.agency_fare_url = agency_fare_url

    def __repr__(self):
        return f"""{self.agency_id} {self.agency_name} {self.agency_url}
        {self.agency_timezone} {self.agency_lang} {self.agency_phone} {self.agency_fare_url}"""


class Calendar:
    def __init__(self, service_id, monday, tuesday, wednesday, thursday, friday,
                 saturday, sunday, start_date, end_date):
        self.service_id = service_id
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"""{self.service_id} {self.monday} {self.tuesday} {self.wednesday} {self.thursday} {self.friday}
        {self.friday} {self.saturday} {self.sunday} {self.start_date} {self.end_date}"""


class Dates:
    def __init__(self, service_id, date, exception_type):
        self.service_id = service_id
        self.date = date
        self.exception_type = exception_type

    def __repr__(self):
        return f"{self.service_id} {self.date} {self.exception_type}"


class Feed:
    def __init__(self, publisher, url, lang, start, end, version):
        self.publisher = publisher
        self.url = url
        self.lang = lang
        self.start = start
        self.end = end
        self.version = version

    def __repr__(self):
        return f'''PUB {self.publisher} URL {self.url} LANG {self.lang} \n
        ST {self.start} END {self.end} VER {self.version}'''


class Routes:
    def __init__(self, route_id, agency_id, route_short_name, route_long_name, route_desc, route_type, route_url,
                 route_color, route_text_color):
        self.route_id = route_id
        self.agency_id = agency_id
        self.route_short_name = route_short_name
        self.route_long_name = route_long_name
        self.route_desc = route_desc
        self.route_type = route_type
        self.route_url = route_url
        self.route_color = route_color
        self.route_text_color = route_text_color

    def __repr__(self):
        return f'''{self.route_id} {self.agency_id} {self.route_short_name} {self.route_long_name}
        {self.route_desc} {self.route_type} {self.route_url} {self.route_color} {self.route_text_color}'''


class Shapes:
    def __init__(self, shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled):
        self.shape_id = shape_id
        self.shape_pt_lat = shape_pt_lat
        self.shape_pt_lon = shape_pt_lon
        self.shape_pt_sequence = shape_pt_sequence
        self.shape_dist_traveled = shape_dist_traveled

    def __repr__(self):
        return f'''{self.shape_id} {self.shape_pt_lat} {self.shape_pt_lon} 
        {self.shape_pt_sequence} {self.shape_dist_traveled}'''


class StopTimes:
    def __init__(self, trip_id, arrival_time, departure_time, stop_id, location_group_id, location_id, stop_sequence,
                 stop_headsign, start_pickup_drop_off_window, end_pickup_drop_off_window, pickup_type, drop_off_type,
                 continuous_pickup, continuous_drop_off, shape_dist_traveled, timepoint, pickup_booking_rule_id,
                 drop_off_booking_rule_id):
        self.trip_id = trip_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.stop_id = stop_id
        self.location_group_id = location_group_id
        self.location_id = location_id
        self.stop_sequence = stop_sequence
        self.stop_headsign = stop_headsign
        self.start_pickup_drop_off_window = start_pickup_drop_off_window
        self.end_pickup_drop_off_window = end_pickup_drop_off_window
        self.pickup_type = pickup_type
        self.drop_off_type = drop_off_type
        self.continuous_pickup = continuous_pickup
        self.continuous_drop_off = continuous_drop_off
        self.shape_dist_traveled = shape_dist_traveled
        self.timepoint = timepoint
        self.pickup_booking_rule_id = pickup_booking_rule_id
        self.drop_off_booking_rule_id = drop_off_booking_rule_id

    def __repr__(self):
        return f'''{self.trip_id}: {self.arrival_time} {self.departure_time} {self.stop_id} {self.location_group_id} 
        {self.location_id} {self.stop_sequence} {self.stop_headsign} {self.start_pickup_drop_off_window} 
        {self.end_pickup_drop_off_window} {self.pickup_type} {self.drop_off_type} {self.continuous_pickup} 
        {self.continuous_drop_off} {self.shape_dist_traveled} {self.timepoint} {self.pickup_booking_rule_id} 
        {self.drop_off_booking_rule_id}'''


class Stops:
    def __init__(self, stop_id, stop_code, stop_name, tts_stop_name, stop_desc, stop_lat, stop_lon, zone_id,
                 stop_url, location_type, parent_station, stop_timezone, wheelchair_boarding):
        self.stop_id = stop_id
        self.stop_code = stop_code
        self.stop_name = stop_name
        self.tts_stop_name = tts_stop_name
        self.stop_desc = stop_desc
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.zone_id = zone_id
        self.stop_url = stop_url
        self.location_type = location_type
        self.parent_station = parent_station
        self.stop_timezone = stop_timezone
        self.wheelchair_boarding = wheelchair_boarding

    def __repr__(self):
        return f"""{self.stop_id}: {self.stop_code} {self.stop_name} {self.tts_stop_name} {self.stop_desc}
        {self.stop_lat} {self.stop_lon} {self.zone_id} {self.stop_url} {self.location_type} {self.parent_station} 
        {self.stop_timezone} {self.wheelchair_boarding}"""


class Transfers:
    def __init__(self, from_stop_id, to_stop_id, from_route_id, to_route_id, from_trip_id, to_trip_id,
                 transfer_type, min_transfer_time):
        self.from_stop_id = from_stop_id
        self.to_stop_id = to_stop_id
        self.from_route_id = from_route_id
        self.to_route_id = to_route_id
        self.from_trip_id = from_trip_id
        self.to_trip_id = to_trip_id
        self.transfer_type = transfer_type
        self.min_transfer_time = min_transfer_time

    def __repr__(self):
        return f'''{self.from_stop_id} {self.to_stop_id} {self.from_route_id} {self.to_route_id}
        {self.from_trip_id} {self.to_trip_id} {self.transfer_type} {self.min_transfer_time}'''


class Trips:
    def __init__(self, route_id, service_id, trip_id, trip_headsign, trip_short_name,
                 direction_id, block_id, shape_id, wheelchair_accessible, bikes_allowed):
        self.route_id = route_id
        self.service_id = service_id
        self.trip_id = trip_id
        self.trip_headsign = trip_headsign
        self.trip_short_name = trip_short_name
        self.direction_id = direction_id
        self.block_id = block_id
        self.shape_id = shape_id
        self.wheelchair_accessible = wheelchair_accessible
        self.bikes_allowed = bikes_allowed

    def __repr__(self):
        return f'''{self.route_id} {self.service_id} {self.trip_id} {self.trip_headsign} 
        {self.trip_short_name} {self.direction_id} {self.block_id} {self.shape_id} 
        {self.wheelchair_accessible} {self.bikes_allowed}'''
