text = open("Pittsburgh/gtfs_static_feed/stops.txt", "r")

class Stops:
    def __init__(self, id, code, name, desc, lat, lon, zone, url, type, parent,
                 timezone, wheelchair):
        self.id = id
        self.code = code
        self.name = name
        self.desc = desc
        self.lat = lat
        self.lon = lon
        self.zone = zone
        self.url = url
        self.type = type
        self.parent = parent
        self.timezone = timezone
        self.wheelchair = wheelchair

    def __repr__(self):
        return f"ID {self.id} NAME {self.name} LAT {self.lat} LON {self.lon}\n"

    
prt_stops = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    stop_id = line[0:indexList[0]]
    stop_code = line[indexList[0]+1:indexList[1]]
    stop_name = line[indexList[1]+1:indexList[2]]
    stop_desc = line[indexList[2]+1:indexList[3]]
    stop_lat = line[indexList[3]+1:indexList[4]]
    stop_lon = line[indexList[4]+1:indexList[5]]
    zone_id = line[indexList[5]+1:indexList[6]]
    stop_url = line[indexList[6]+1:indexList[7]]
    location_type = line[indexList[7]+1:indexList[8]]
    parent_station = line[indexList[8]+1:indexList[9]]
    stop_timezone = line[indexList[9]+1:indexList[10]]
    wheelchair_boarding = line[indexList[10]+1:]
    obj = Stops(stop_id, stop_code, stop_name, stop_desc, stop_lat, stop_lon, 
                zone_id, stop_url, location_type, parent_station, stop_timezone, 
                wheelchair_boarding)
    prt_stops[stop_id] = obj