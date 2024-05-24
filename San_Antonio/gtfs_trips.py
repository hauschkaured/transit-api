text = open("gtfs_static_feed/trips.txt", "r")


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


via_trips = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    route_id = line[0:indexList[0]]
    service_id = line[indexList[0]+1:indexList[1]]
    trip_id = line[indexList[1]+1:indexList[2]]
    headsign = line[indexList[2]+1:indexList[3]]
    short_name = line[indexList[3]+1:indexList[4]]
    direction_id = line[indexList[4]+1:indexList[5]]
    block_id = line[indexList[5]+1:indexList[6]]
    shape_id = line[indexList[6]+1:indexList[7]]
    wheelchair = line[indexList[7]+1:indexList[8]]
    bikes = line[indexList[8]+1:]
    obj = Trips(route_id, service_id, trip_id, headsign, short_name, 
                direction_id, block_id, shape_id, wheelchair, bikes)
    via_trips[trip_id] = obj