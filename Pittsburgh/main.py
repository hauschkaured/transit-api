import datetime
from fetcher import *
from datetime import datetime

# from gtfs_agency import agency
# from gtfs_calendar_dates import calendar_dates
# from gtfs_calendar import gtfscalendar
# from gtfs_feed import feed
# from gtfs_routes import routes
# from gtfs_shapes import shapes
# from gtfs_stop_times import stoptimes
from gtfs_stops import stops
# from gtfs_transfers import transfers
from gtfs_trips import trips 

import pprint as PP

## Configured Pretty Printing

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

## Importing data from fetcher.py 

busdata = main(rt1_endpoint, output_path1)
bustripdata = main(rt2_endpoint, output_path2)
traindata = main(rt3_endpoint, output_path3)
traintripdata = main(rt4_endpoint, output_path4)



busDict = vehicle_processing(busdata)
trainDict = vehicle_processing(traindata)



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
                newtime = datetime.fromtimestamp(stopTime).strftime('%H:%M:%S')
                print(f"Bus {string} {stopName} at {newtime}")


# HELPERS
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


buses_in_range(3500,3510)