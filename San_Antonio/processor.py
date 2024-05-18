from gtfs_agency import via_agency
from gtfs_calendar_dates import via_calendar_dates
from gtfs_calendar import via_calendar
from gtfs_feed import via_feed
from gtfs_routes import via_routes
from gtfs_shapes import via_shapes
from gtfs_stop_times import via_stoptimes
from gtfs_stops import via_stops
from gtfs_transfers import via_transfers
from gtfs_trips import via_trips

import pprint as PP
from datetime import datetime

## Configured Pretty Printing

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint


def trip_processing(tripdata):
    trip_dict = {}
    for i in tripdata["entity"]:
        update = i["tripUpdate"]    
        ## Populating data
        id = update["trip"]["tripId"]
        trip = {}
        trip["id"] = id

        # Header
        tripdata = update["trip"]
        # Subfields       
        directionId = tripdata["directionId"]
        trip["directionId"] = directionId
        relationship = tripdata["scheduleRelationship"]
        trip["relationship"] = relationship
        route = tripdata["routeId"]
        trip["route"] = route
        startDate = tripdata["startDate"]
        trip["startDate"] = startDate
        startTime = tripdata["startTime"]
        trip["startTime"] = startTime

        timedata = update["timestamp"]
        trip["timedata"] = timedata

        trip_dict[id] = trip

        # Stop time update data
        timeUpdate = update["stopTimeUpdate"]
        
        timeUpdateList = []

        for i in timeUpdate:
            timeUpd = {}
            stopSequence = i["stopSequence"]
            timeUpd["stopSequence"] = stopSequence
            stopId = i["stopId"]
            timeUpd["stopId"] = stopId
            relationship = i["scheduleRelationship"]
            timeUpd["relationship"] = relationship

            if "departure" in i:
                departure = i["departure"]
                if "time" in departure:
                    time = departure["time"]
                    timeUpd["depTime"] = time
                if "uncertainty" in departure:
                    uncertainty = departure["uncertainty"]
                    timeUpd["depUncertainty"] = uncertainty
            if "arrival" in i:
                arrival = i["arrival"]
                if "time" in arrival:
                    time = arrival["time"]
                    timeUpd["arrTime"] = time
                if "uncertainty" in arrival:
                    uncertainty = arrival["uncertainty"]
                    timeUpd["arrUncertainty"] = uncertainty
            timeUpdateList.append(timeUpd)

        trip["timeUpdateList"] = timeUpdateList
    return trip_dict

tripDict = trip_processing(tripdata)

## MAIN FUNCTIONS

def buses_on_route(input):
    for bus in busDict:
        busInfo = busDict[bus]
        if "tripRoute" in busInfo:
            busRoute = busInfo["tripRoute"]
            if busRoute == input:
                status = status_converter(busInfo["status"])
                print(f"\x1b[33mRoute \x1b[34m{busRoute} #{busInfo["vid"]} \x1b[0mis {status} {busInfo["stopId"]}")

def buses_in_range(low, high):
    print(f"The following buses are in the range {low}-{high}")
    for i in range(low, high+1):
        if str(i) in busDict:
            busInfo = busDict[str(i)]
            if "status" in busInfo:
                status = status_converter(busInfo["status"])
                stopId = busInfo["stopId"]
                stop = stops[stopId].name
                trip = busInfo["tripId"]
                print(f"\x1b[33mRoute \x1b[34m{busInfo["tripRoute"]} #{busInfo["vid"]} \x1b[0mis {status} {stop}")
                time1 = soonest_departure(trip)
                time2 = soonest_arrival(trip)
                if ((time1 != None) and (time2 != None)):
                    print(f"Arriving at {time2}, departing at {time1}")
                elif time2 != None:
                    print(f"Arriving at {time2}")
                elif time1 != None:
                    print(f"Departing at {time1}")
## HELPERS

def status_converter(status):
    if status == "IN_TRANSIT_TO":
        return "in transit to"
    if status == "STOPPED_AT":
        return "stopped at"

def soonest_departure(trip):
    for i in tripDict:
        if i == trip:
            stop = tripDict[i]["timeUpdateList"][0]
            if "depTime" in stop:
                stopTime = int(stop["depTime"])
                time = datetime.fromtimestamp(stopTime).strftime('%H:%M:%S')           
                return time
        
def soonest_arrival(trip):
    for i in tripDict:
        if i == trip:
            stop = tripDict[i]["timeUpdateList"][0]
            if "arrTime" in stop:
                stopTime = int(stop["arrTime"])
                time = datetime.fromtimestamp(stopTime).strftime('%H:%M:%S')           
                return time        

buses_in_range(387,405) ## NFI DE40LFR
buses_in_range(406,420) ## NFI XN40