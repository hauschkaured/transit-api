from fetcher import fetch_tripupdate
from common import utils, defs
import os

from via_busfleet import models 
from via_busfleet import model_list 
import pprint as PP

## Configured Pretty Printing

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint


agency, dates, calendar, feed, routes, shapes, times, stops, transfers, trips = \
    utils.gen_static_structs(os.path.join(defs.SRC_ROOT, defs.SAN_ANTONIO_DIR, "gtfs_static_feed"))


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







tripdata = fetch_tripupdate()

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


