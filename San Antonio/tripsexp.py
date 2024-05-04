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
import pprint as PP

## Configured Pretty Printing

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

class Data:
    def __init__(self, header, entity):
        self.header = header
        self.entity = entity

    def __repr___(self):
        return f"Data: {self.header}, {self.entity}"

class Header(Data):
    def __init__(self, version, incrementality, timestamp):
        self.version = version
        self.incrementality = incrementality
        self.timestamp = timestamp

    def __repr__(self):
        return f"Header: {self.version}, {self.incrementality}, {self.timestamp}\n"

class Entity(Data):
    def __init__(self, id, tripupdate):
        self.id = id
        self.tripupdate = tripupdate

    def __repr__(self):
        return f"Entity: {self.id} {self.tripupdate}\n"

class Tripupdate:
    def __init__(self, trip, vehicle, stoptimeupdate, timestamp):
        self.trip = trip
        self.vehicle = vehicle
        self.stoptimeupdate = stoptimeupdate
        self.timestamp = timestamp
    
    def __repr__(self):
        return f"Tripupdate: {self.trip} {self.vehicle} {self.stoptimeupdate} {self.timestamp}"

class Trip(Tripupdate):
    def __init__(self, direction, routeId, scheduledRelationship, startDate, 
                 startTime, tripId):
        self.direction = direction
        self.routeId = routeId
        self.scheduledRelationship = scheduledRelationship
        self.startDate = startDate
        self.startTime = startTime
        self.tripId = tripId

    def __repr__(self):
        return f'''Trip: {self.direction}, {self.routeId}, {self.scheduledRelationship},
            {self.startDate}, {self.startTime}, {self.tripId}\n'''

class Stopseq:
    def __init__(self, x):
        self.x = x







tripdata = main_2()

head = tripdata["header"]
ver = head["gtfsRealtimeVersion"]
inc = head["incrementality"]
time = head["timestamp"]

header = Header(ver, inc, time)

print(header)
busList = []
for i in tripdata["entity"]:
    j = i["id"]
    kOne = i["tripUpdate"]

    trip = kOne["trip"]
    dir = trip["directionId"]
    route = trip["routeId"]
    rel = trip["scheduleRelationship"]
    date = trip["startDate"]
    time = trip["startTime"]
    tripid = trip["tripId"]
    trippy = Trip(dir, route, rel, date, time, tripid)

    stopList = []
    stop = kOne["stopTimeUpdate"]
    for i in stop:
        print(i.keys())
        if "departure" not in i.keys():
            departure = 0
        else:
            departure = i["departure"]



    vehi = kOne["vehicle"]

    time = kOne["timestamp"]

    item = Entity(j,trippy)
    busList.append(item)


data = Data(header, busList)


