import datetime
from fetcher import *
from datetime import datetime

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

import pprint as PP

## Configured Pretty Printing

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

## Importing data from fetcher.py 

busdata = main_1()
bustripdata = main_2()
traindata = main_3()
traintripdata = main_4()

def vehicle_processing(busdata):
    vid_dict = {}
    for bus in busdata["entity"]:
        ## make dictionary with name of bus model. 
        busId = bus["vehicle"]["vehicle"]["id"]
        id = {}

        ## Searching through data to populate the bus dictionary.
        data = bus["vehicle"]

        ## Position data
        posdata = data["position"] ## Heading field

        ## ID
        vid = data["vehicle"]["id"]
        id["vid"] = vid

        ## Subfields 
        lat = posdata["latitude"]
        id["lat"] = lat
        lon = posdata["longitude"]
        id["lon"] = lon
        if "bearing" in posdata:
            hdg = posdata["bearing"]
            id["hdg"] = hdg
        if "speed" in posdata:
            speed = posdata["speed"]
            id["speed"] = speed

        ## Time data
        time = data["timestamp"]
        id["time"] = time

        ## Stop data     
        if "stopId" in data:
            stopId = data["stopId"]
            id["stopId"] = stopId

        if "currentStopSequence" in data:
            currStop = data["currentStopSequence"]
            id["currStop"] = currStop

        if "trip" in data:
            # header
            tripdata = data["trip"]
            tripid = tripdata["tripId"]
            triproute = tripdata["routeId"]
            id["tripId"] = tripid
            id["tripRoute"] = triproute

        if "currentStatus" in data:
            status = data["currentStatus"]
            id["status"] = status

        vid_dict[busId] = id
    return vid_dict       

busDict = vehicle_processing(busdata)
trainDict = vehicle_processing(traindata)

def trip_processing(bustripdata):
    trip_dict = {}
    for i in bustripdata["entity"]:
        update = i["tripUpdate"]    
        ## Populating data
        id = update["trip"]["tripId"]
        trip = {}
        trip["id"] = id

        # Header
        tripdata = update["trip"]
        # Subfields       
        relationship = tripdata["scheduleRelationship"]
        trip["relationship"] = relationship
        route = tripdata["routeId"]
        trip["route"] = route

        timedata = update["timestamp"]
        trip["timedata"] = timedata

        trip_dict[id] = trip

        # Stop time update data
        if "stopTimeUpdate" in update:
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

tripDict = trip_processing(bustripdata)
trainTripDict = trip_processing(traintripdata)

## MAIN FUNCTIONS

def buses_on_route(input):
    for bus in busDict:
        busInfo = busDict[bus]
        if "tripRoute" in busInfo:
            busRoute = busInfo["tripRoute"]
            if busRoute == input:
                print(f"\x1b[33mRoute \x1b[34m{busRoute} #{busInfo["vid"]} \x1b[0mis at {busInfo["stopId"]}")

def buses_in_range(low, high):
    print(f"The following buses are in the range {low}-{high}")
    for i in range(low, high+1):
        if str(i) in busDict:
            busInfo = busDict[str(i)]
            if "tripId" in busInfo:
                tripId = busInfo["tripId"]
                if tripId in tripDict:
                    trip_information = tripDict[tripId]
                    trip = trip_information
                    nearestStop = trip_information["timeUpdateList"][0]
                    nearestStopID = nearestStop["stopId"]
                    name = stops[nearestStopID].name
                    headsign = trips[tripId].headsign
                    print(f"\x1b[33mRoute \x1b[34m{busInfo["tripRoute"]} #{busInfo["vid"]} {headsign} \x1b[0mis at {name}")
                    time1 = soonest_departure(trip)
                    time2 = soonest_arrival(trip)
                    if ((time1 != None) and (time2 != None)):
                        print(f"Arriving at {time2}, departing at {time1}")
                    elif time2 != None:
                        print(f"Arriving at {time2}")
                    elif time1 != None:
                        print(f"Departing at {time1}")
            else:
                latitude = busInfo["lat"]
                longitude = busInfo["lon"]
                print(f"{i} is at lat, lon {latitude}, {longitude}")

def print_running_buses():
    busList = []
    for i in busDict:
        busList.append(i)
    busList.sort()
    print(busList)

def show_trip_information(trip):
    for i in tripDict:
        if i == trip:
            stopsList = tripDict[i]["timeUpdateList"]
            for j in stopsList:
                if 'depTime' in j:
                    stopTime = int(j['depTime'])
                    string = 'departs from'
                if 'arrTime' in j:
                    stopTime = int(j['arrTime'])
                    string = 'arrives at'
                stopId = j['stopId']
                stopName = stops[stopId].name
                Time = datetime.fromtimestamp(stopTime).strftime('%H:%M:%S')
                print(f"Bus {string} {stopName} at {Time}")

## HELPERS

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
            
