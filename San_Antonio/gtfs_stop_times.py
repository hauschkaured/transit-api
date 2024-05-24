text = open("gtfs_static_feed/stop_times.txt", "r")


class Stoptimes:
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


via_stoptimes = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    id = line[0:indexList[0]]
    arrival = line[indexList[0]+1:indexList[1]]
    departure = line[indexList[1]+1:indexList[2]]
    stop_id = line[indexList[2]+1:indexList[3]]
    stopseq = line[indexList[3]+1:indexList[4]]
    headsign = line[indexList[4]+1:indexList[5]]
    pickup_type = line[indexList[5]+1:indexList[6]]
    dropoff_type = line[indexList[6]+1:indexList[7]]
    shape_dist_traveled = line[indexList[7]+1:indexList[8]]
    timepoint = line[indexList[8]+1:]

    obj = Stoptimes(id, arrival, departure, stop_id, None, None, stopseq, headsign,
                    None, None, pickup_type, dropoff_type,
                    None, None, shape_dist_traveled, timepoint,
                    None, None)
    via_stoptimes[stop_id] = obj