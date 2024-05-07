from fetcher import main_1
from fetcher import main_2

from gtfs_agency import agency
from gtfs_calendar_dates import calendar_dates
from gtfs_calendar import gtfscalendar
from gtfs_feed import feed
from gtfs_routes import routes 
from gtfs_shapes import shapes
from gtfs_stop_times import stoptimes
from gtfs_stops import stops
from gtfs_transfers import transfers
from gtfs_trips import trips 

from via_busfleet import models 
from via_busfleet import model_list 

data = main_1()
tripdata = main_2()

buses = {}
nonroute = {}

class Vehicle:
    def __init__(self, pos, time, vehicle, stopseq=None, status=None, 
                 stopid=None, trip=None):
        self.pos = pos
        self.time = time
        self.vehicle = vehicle
        self.stopseq = stopseq
        self.status = status
        self.stopid = stopid
        self.trip = trip
    
    def __repr__(self):
        return f"{self.pos} {self.time} {self.vehicle} {self.stopseq} {self.status} {self.stopid} {self.trip}\n"
    
    def stopName(self, stopid):
        return stops[stopid].name
    
    def indicator(self):
        if self.trip == None:
            return False
        else: return True 

    def statusClean(self):
        if self.status == "STOPPED_AT":
            return "stopped at"
        elif self.status == "IN_TRANSIT_TO":
            return "in transit to"

class Trip(Vehicle):
    def __init__(self, tripid, start_date, route_id):
        self.tripid = tripid
        self.start_date = start_date
        self.route_id = route_id

    def __repr__(self):
        return f"{self.tripid} {self.start_date} {self.route_id}"

class Position(Vehicle):
    def __init__(self, lat, lon, hdg=None, spd=None):
        self.lat = lat
        self.lon = lon
        self.hdg = hdg
        self.spd = spd

    def __repr__(self):
        return f"{self.lat} {self.lon} {self.hdg} {self.spd}"

def vehicle_processing(data):
    for bus in data["entity"]:
        id = bus["id"]
        data = bus["vehicle"]
        
        
        ## Position data
        posdata = data["position"]
        lat = posdata["latitude"]
        lon = posdata["longitude"]

        ## Time data
        time = data["timestamp"]

        ## Vehicle data
        vid = data["vehicle"]["id"]

        if (('trip' in data) and ('timestamp' in data) and ('stopId' in data)
            and ('position' in data) and ('currentStopSequence' in data) and 
            ('currentStatus' in data) and len(vid) == 3):
            stopseq = data["currentStopSequence"]
            status = data["currentStatus"]
            currentStop = data["stopId"]
            if (('bearing' in posdata) and ('speed' in posdata)):
                hdg = posdata["bearing"]
                spd = posdata["speed"]
                posobj = Position(lat, lon, hdg, spd)
            else:
                posobj = Position(lat, lon)
            tripthing = data["trip"]
            tripid = tripthing["tripId"]
            startdate = tripthing["startDate"]
            triproute = tripthing["routeId"]
            tripobj = Trip(tripid, startdate, triproute)
            obj = Vehicle(posobj, time, vid, stopseq, status, currentStop, tripobj)
            buses[vid] = obj
        else:
            if (('bearing' in posdata) and ('speed' in posdata)):
                hdg = posdata["bearing"]
                spd = posdata["speed"]
                posobj = Position(lat, lon, hdg, spd)
            else:
                posobj = Position(lat, lon)
            obj = Vehicle(posobj, time, vid)
            nonroute[vid] = obj

def buses_running():
    vid_list = []
    for bus in buses.keys():
        vid_list.append(bus)
    vid_list.sort()
    return vid_list 

def buses_on_route(rt):
    route = str(rt)
    for bus in buses.keys():
        main = buses[bus]
        if main.stopid in stops.keys():
            sec = stops[main.stopid]
        name = sec.name
        routeInfo = routes[route]
        if main.indicator:
            if main.trip.route_id == route:
                trip_id = main.trip.tripid
                if trip_id in trips:
                    headsign = trips[trip_id].headsign
                    print(f"\x1b[33m #{main.vehicle} Route {route} \x1b[34m {routeInfo.long_name} to {headsign}")
                    print(f"    \x1b[0mis {main.status} {name}")

vehicle_processing(data)
buses_on_route('93')
buses_on_route('17')
buses_on_route('64')
buses_on_route('7')
buses_on_route('82')
buses_running()