text = open("Pittsburgh/gtfs_static_feed/stops.txt", "r")


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
    obj = Stops(stop_id, stop_code, stop_name, None, stop_desc, stop_lat, stop_lon,
                zone_id, stop_url, location_type, parent_station, stop_timezone, 
                wheelchair_boarding)
    prt_stops[stop_id] = obj