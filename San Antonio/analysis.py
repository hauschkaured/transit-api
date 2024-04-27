import gtfsrt_pb2
import requests
from google.protobuf import json_format
import pprint as PP
import json

## GTFS Static Feed Definitions
from routes import routes 
from stops import stops
from agency import agency

feedmsg1 = open("vehiclepositions.out", "r")
feedmsg2 = open("tripupdates.out", "r")

feeder = json.loads(feedmsg1)

pprint(feeder)


def write_to_file(path: str, content: str) -> None:
    """
    Writes the content string to the specified path
    """
    with open(path, 'w') as f:
        f.write(content)

def data_process(data):
    busRoute = {}
    busStatus = {}
    busStopSeq = {}
    busLat = {}
    busLong = {}
    busTime = {}
    busTripId = {}
    busDate = {}
    busStopId = {}
    vid_list = []

    for entry in data["entity"]:
        pprint(entry)

    checkList = ["currentStatus", "currentStopSequence", "trip", "position", "vehicle"]
    for entry in data["entity"]:
        vid = entry["id"]
        ## Layer 2 dictionary
        attributes = entry["vehicle"]
        ticker = 0
        for i in checkList:
            if i in attributes:
                ticker += 1
        if ticker == 5:
            full_process(attributes, vid, busRoute, busStatus, busStopSeq, busStopId,
                         busLat, busLong, busTime, busTripId, busDate)
        else:
            partial_process(attributes)
    vid_list.sort()

def partial_process(attributes):
    pass

def full_process(attributes, vid, busRoute, busStatus, busStopSeq, busStopId, 
                 busLat, busLong, busTime, busTripId, busDate):
    ## Dictionaries to probe and other data
    status = attributes["currentStatus"]
    stopseq = attributes["currentStopSequence"]
    position = attributes["position"]
    stopId = attributes["stopId"]
    time = attributes["timestamp"]
    trip = attributes["trip"]
    vid = attributes["vehicle"]["id"]

    route = trip["routeId"]
    date = trip["startDate"]
    tripId = trip["tripId"]

    lat = position["latitude"]
    long = position["longitude"]

    busRoute[vid] = route
    busStatus[vid] = status
    busStopSeq[vid] = stopseq
    busStopId[vid] = stopId
    busLat[vid] = lat
    busLong[vid] = long
    busTime[vid] = time
    busTripId[vid] = tripId
    busDate[vid] = date

    busesOnRoute("93", busRoute, busStopId, busStatus, busLat, busLong)
    busesOnRoute("17", busRoute, busStopId, busStatus, busLat, busLong)
    busesOnRoute("64", busRoute, busStopId, busStatus, busLat, busLong)
    busesOnRoute("7", busRoute, busStopId, busStatus, busLat, busLong)



    # hdg = position["bearing"]
    # spd = position["speed"]

def busesOnRoute(rte, busRoute, busStopId, busStatus, busLat, busLong): ## FUNCTION 1
    busList = []
    for bus in busRoute:
        if busRoute[bus] == rte:
            busList.append(bus)
            stop = busStopId[bus]
            if stop in stops:
                name = stops[stop] 
            status = busStatus[bus]
            lat = busLat[bus]
            long = busLong[bus]
            if status == "IN_TRANSIT_TO":
                status = "in transit to"
            elif status == "STOPPED_AT":
                status = "stopped at"
            if stop in stops:
                print(f"\x1b[33mRoute \x1b[34m{rte} #{bus} \x1b[0m is {status} {name}")    
            if status == "in transit to":
                print(f"    lat {lat} long {long}")



