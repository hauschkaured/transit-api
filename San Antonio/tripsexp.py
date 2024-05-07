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

tripdata = main_2()
tripDict = {}


head = tripdata["header"]
version = head["gtfsRealtimeVersion"]
incrementality = head["incrementality"]
timestamp = head["timestamp"]

for i in tripdata["entity"]:
    id = i["id"]
    realtime = i["tripUpdate"]
    

    trip = realtime["trip"]
    directionId = trip["directionId"]
    routeId = trip["routeId"]
    rel = trip["scheduleRelationship"]
    startDate = trip["startDate"]
    startTime = trip["startTime"]
    tripid = trip["tripId"]
    
    entityTime = realtime["timestamp"]

    vehicle = realtime["vehicle"]["id"]

    for i in realtime["stopTimeUpdate"]:
        pprint(i.keys())        
        stopSeq = i["stopSequence"]
        stopId = i["stopId"]
        rel = i["scheduleRelationship"]
        if "departure" in i.keys():
            print(i["departure"]["time"])
            if "uncertainty" in i["departure"]:
                print(i["departure"]["uncertainty"])
        if "arrival" in i.keys():
            print(i["arrival"]["time"])
            if "uncertainty" in i["arrival"]:
                print(i["arrival"]["uncertainty"])

    