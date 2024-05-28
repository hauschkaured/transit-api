from fetcher import *
from datetime import datetime

from static.gtfs_agency import *
from static.gtfs_calendar_dates import *

# from Pittsburgh.gtfs_stops import prt_stops
# from Pittsburgh.gtfs_agency import prt_agency
# from Pittsburgh.gtfs_calendar_dates import prt_calendar_dates
# from Pittsburgh.gtfs_calendar import prt_calendar
from Pittsburgh.gtfs_feed_info import prt_feed
# from Pittsburgh.gtfs_routes import prt_routes
# from Pittsburgh.gtfs_shapes import prt_shapes
# from Pittsburgh.gtfs_stop_times import prt_stoptimes
from Pittsburgh.gtfs_stops import prt_stops
# from Pittsburgh.gtfs_transfers import prt_transfers
# from Pittsburgh.gtfs_trips import prt_trips

# from San_Antonio.gtfs_stops import via_stops
from San_Antonio.gtfs_agency import via_agency
# from San_Antonio.gtfs_calendar_dates import via_calendar_dates
# from San_Antonio.gtfs_calendar import via_calendar
from San_Antonio.gtfs_feed_info import via_feed
from San_Antonio.gtfs_routes import via_routes
# from San_Antonio.gtfs_shapes import via_shapes
# from San_Antonio.gtfs_stop_times import via_stoptimes
from San_Antonio.gtfs_stops import via_stops
# from San_Antonio.gtfs_transfers import via_transfers
# from San_Antonio.gtfs_trips import via_trips

from api_key import key

import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

BASE_PARAMS = {
    'key': key,
    'format': 'json',
    'rtpidatafeed': 'Port Authority Bus',
}

prediction_params = {
    **BASE_PARAMS
    }

# Constants for supported cities

def supported_cities():
    list = ["Pittsburgh", "San Antonio"]
    return list


def supported_functions_by_city():
    dict = {
        "satx" : ["bus", "route"],
        "pgh" : ["bus", "route", "stop"]
    }
    return dict


def routeCall(input):
    URL = "https://truetime.portauthority.org/bustime/api/v3/"
    prediction_params["stpid"] = input
    predictions = requests.get(URL + "getpredictions", params=prediction_params)
    bustime = predictions.json()
    busList = bustime["bustime-response"]["prd"]
    return busList


def static_feed_validity():
    print(f"PRT: {prt_feed[0].start} to {prt_feed[0].end}")
    print(f"VIA: {via_feed[0].start} to {via_feed[0].end}")


# Main Processing Functions
def api_stop_processing_prt(data):
    pass

def vehicle_processing_via(data):
    via_vid_dict = {}
    for bus in data["entity"]:
        # make dictionary with name of bus model.
        busId = bus["id"]
        id = {}
        # Searching through data to populate the bus dictionary.
        data = bus["vehicle"]
        # Position data
        posdata = data["position"] # Heading field
        # ID
        vid = data["vehicle"]["id"]
        id["vid"] = vid
        # Subfields
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
        # Time data
        time = data["timestamp"]
        id["time"] = time
        # Stop data
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
            startdate = tripdata["startDate"]
            triproute = tripdata["routeId"]
            id["tripId"] = tripid
            id["startDate"] = startdate
            id["tripRoute"] = triproute
        if "currentStatus" in data:
            status = data["currentStatus"]
            id["status"] = status
        via_vid_dict[busId] = id
    return via_vid_dict


def vehicle_processing_prt(input):
    vid_dict = {}
    for bus in input["entity"]:
        # make dictionary with name of bus model.
        busId = bus["vehicle"]["vehicle"]["id"]
        id = {}

        # Searching through data to populate the bus dictionary.
        data = bus["vehicle"]

        # Position data
        posdata = data["position"] # Heading field

        # ID
        vid = data["vehicle"]["id"]
        id["vid"] = vid

        # Subfields
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

        # Time data
        time = data["timestamp"]
        id["time"] = time

        # Stop data
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


def trip_processing_via(tripdata):
    via_trip_dict = {}
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

        via_trip_dict[id] = trip
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
    return via_trip_dict


def trip_processing_prt(bustripdata):
    trip_dict = {}
    for i in bustripdata["entity"]:
        update = i["tripUpdate"]
        # Populating data
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


# Main analysis functions
def buses_on_route_via(input):
    for bus in busDict:
        busInfo = busDict[bus]
        if "tripRoute" in busInfo:
            busRoute = busInfo["tripRoute"]
            if busRoute == input:
                status = status_converter(busInfo["status"])
                stopId = busInfo["stopId"]
                stop = via_stops[stopId]
                print(f"\x1b[33mRoute \x1b[34m{busRoute} #{busInfo["vid"]} \x1b[0mis {status} {stop.stop_name}")
                print(f"{stop.lat}, {stop.lon}")


def buses_on_route_prt(input):
    for bus in busDict:
        busInfo = busDict[bus]
        if "tripRoute" in busInfo:
            busRoute = busInfo["tripRoute"]
            if busRoute == input:
                pass
                # stopId = busInfo["stopId"]
                # stopName = prt_stops[stopId]
                # print(f"\x1b[33mRoute \x1b[34m{busRoute} #{busInfo["vid"]} \x1b[0mis {status} {stopName}")


def buses_in_range_via(low, high):
    low_int = int(low)
    high_int = int(high)
    print(f"The following buses are in the range {low}-{high}")
    for i in range(low_int, high_int + 1):
        if str(i) in busDict:
            busInfo = busDict[str(i)]
            if "status" in busInfo:
                status = status_converter(busInfo["status"])
                stopId = busInfo["stopId"]
                stop = via_stops[stopId].stop_name
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


def buses_in_range_prt(low, high):
    print(f"The following buses are in the range {low}-{high}")
    low_int = int(low)
    high_int = int(high)
    for i in range(low_int, high_int + 1):
        if str(i) in busDict:
            busInfo = busDict[str(i)]
            if "tripId" in busInfo:
                trip = busInfo["tripId"]
                stopId = busTripDict[trip]["timeUpdateList"][0]["stopId"]
                stop = prt_stops[stopId].stop_name
                print(f"\x1b[33mRoute \x1b[34m{busInfo["tripRoute"]} #{busInfo["vid"]} \x1b[0mis at {stop}")
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


def soonest_departure(trip):
    for i in busTripDict:
        if i == trip:
            stop = busTripDict[i]["timeUpdateList"][0]
            if "depTime" in stop:
                stopTime = int(stop["depTime"])
                time = datetime.fromtimestamp(stopTime).strftime('%H:%M:%S')
                return time


def soonest_arrival(trip):
    for i in busTripDict:
        if i == trip:
            stop = busTripDict[i]["timeUpdateList"][0]
            if "arrTime" in stop:
                stopTime = int(stop["arrTime"])
                time = datetime.fromtimestamp(stopTime).strftime('%H:%M:%S')
                return time


def buses_at_stop_prt(routeCall, input):
    if input.count(',') == 0:
        stopName = prt_stops[input].stop_name
        print(f"You selected {stopName}")
        for bus in routeCall:
            vehicle = bus["vid"]
            route = bus["rt"]
            direction = bus["rtdir"]
            trip = bus["origtatripno"]
            time = bus["prdctdn"]
            passengers = bus["psgld"]
            print(f"\x1b[33m #{vehicle} \x1b[34m{route} ({passengers}) {direction} arrival: {time}")
            if trip in busTripDict:
                currentStop = busTripDict[trip]["timeUpdateList"][0]["stopId"].name
                print(f"\x1b[34m Bus is currently at {currentStop}")


def buses_at_stop_via(input):
    pass


def status_converter(status):
    if status == "IN_TRANSIT_TO": # This is for VIA only
        return "in transit to"
    if status == "STOPPED_AT":
        return "stopped at"


# These functions are for parsing the interactivity.
def mode_select(input):
    spaceIndex = input.find(' ')
    if spaceIndex == 3:
        str = input[:3]
        if str == "bus" or str == "Bus":
            return "bus"
    elif spaceIndex == 5:
        str = input[:5]
        if str == "route" or str == "Route":
            return "route"
    elif spaceIndex == 4:
        str = input[:4]
        if str == "stop" or str == "Stop":
            return "stop"



def range_returner(input):
    listDummy = []
    string = input[4:]
    index = string.find('-')
    minimum = string[:index]
    maximum = string[index+1:]
    listDummy.append(minimum)
    listDummy.append(maximum)
    return listDummy


def route_returner(input):
    listDummy = []
    string = input[6:]
    for bus in string.split(','):
        listDummy.append(bus)
    return listDummy


def model_returner(input):
    return input[4:]


print("Welcome to TransitFoamer!")
x = input("What city would you like to select? ")

if x == "San Antonio":
    busData = main(via_bus_vehicles, "./via_bus_vehicles.out")
    busTripData = main(via_bus_trips, "./via_bus_trips.out")
    busDict = vehicle_processing_via(busData)
    busTripDict = trip_processing_via(busTripData)
    print('''There are two options, route and bus. For route, enter Route or route followed by a 
    comma separated list of routes. For bus, enter bus followed by either the bus in question or
     a range of buses.''')
    y = input("What would you like to do? ")
    mode = mode_select(y)
    if mode == "bus":
        if y.count('-') > 0:
            input = range_returner(y)
            minimum = input[0]
            maximum = input[1]
            buses_in_range_via(minimum, maximum)
        else:
            input = model_returner(y)
            buses_in_range_via(input, input)
    if mode == "route":
        if y.count(',') > 0:
            listDummy = route_returner(y)
            for i in listDummy:
                buses_on_route_via(i)
        else:
            string = y[6:]
            buses_on_route_via(string)

elif x == "Pittsburgh":
    busData = main(prt_bus_vehicles, "./prt_bus_vehicles.out")
    busTripData = main(prt_bus_trips, "./prt_bus_trips.out")
    trainData = main(prt_train_vehicles, "./prt_train_vehicles.out")
    trainTripData = main(prt_train_trips, "./prt_train_trips.out")
    busDict = vehicle_processing_prt(busData)
    busTripDict = trip_processing_prt(busTripData)
    print('''There are three options: route, bus, stop. For route, enter route followed by a 
    comma separated list of routes.For bus, enter bus followed by either the bus in question 
    or a range of buses. For stop, enter stop followed by a stop or comma separated list of stops.''')
    y = input("What would you like to do? ")
    mode = mode_select(y)
    if mode == "bus":
        if y.count('-') > 0:
            input = range_returner(y)
            minimum = input[0]
            maximum = input[1]
            buses_in_range_prt(minimum, maximum)
        else:
            input = model_returner(y)
            buses_in_range_prt(input, input)
    if mode == "route":
        if y.count(',') > 0:
            listDummy = route_returner(y)
            for i in listDummy:
                buses_on_route_prt(i)
        else:
            string = y[6:]
            buses_on_route_prt(string)
    if mode == "stop":
        input = y[5:]
        stopInfo = routeCall(input)
        if y.count(',') > 0:
            buses_at_stop_prt(stopInfo, input)
        else:
            buses_at_stop_prt(stopInfo, input)

elif x == "Debug":
    pprint(via_agency)
    pprint(via_routes)

# def listed_features(features, input):
#     available_features = features[input]
#     print(f"Features: {available_features}")


# def list_of_values(input):
#     dash_index = input.find('-')
#     value_1 = input[:dash_index]
#     value_2 = input[dash_index+1:]
#     values = [value_1, value_2]
#     return values


# def data_select(input, function, city):
#     print(city)
#     print(function)
#     length = len(function)
#     raw_data = input[length+1:]
#     print(raw_data)
#     info = []
#     if city == "satx":
#         busData = main(via_bus_vehicles, "./via_bus_vehicles.out")
#         busTripData = main(via_bus_trips, "./via_bus_trips.out")
#         busDict = vehicle_processing_via(busData)
#         busTripDict = trip_processing_via(busTripData)
#         info += busDict 
#         info += busTripDict 
#     elif city == "pgh":
#         busData = main(prt_bus_vehicles, "./prt_bus_vehicles.out")
#         busTripData = main(prt_bus_trips, "./prt_bus_trips.out")
#         trainData = main(prt_train_vehicles, "./prt_train_vehicles.out")
#         trainTripData = main(prt_train_trips, "./prt_train_trips.out")
#         busDict = vehicle_processing_prt(busData)
#         busTripDict = trip_processing_prt(busTripData)
#         trainDict = vehicle_processing_prt(trainData)
#         trainTripDict = trip_processing_prt(trainTripData)
#         info += busDict
#         info += busTripDict 
#     for item in raw_data.split(','):
#         print(item.strip())
#         if function == "Bus":
#             if item.count('-') < 0:
#                 values = list_of_values()
#                 min_val = values[0]
#                 max_val = values[1]
#             else:
#                 pass
#                 # buses_in_range(item, item)
#         elif function == "Stop":
#             pass
#         elif function == "Route":
#             pass


# def mode_select(input):
#     if len(input) >= 5:
#         if (input[0:5] == "route" or input[0:5] == "Route"):
#             return "Route"
#         elif (input[0:4] == "stop" or input[0:4] == "Stop"):
#             return "Stop"
#         elif (input[0:3] == "bus" or input[0:3] == "Bus"):
#             return "Bus"
#     if len(input) >= 4:
#         if (input[0:4] == "stop" or input[0:4] == "Stop"):
#             return "Stop"
#         elif (input[0:3] == "bus" or input[0:3] == "Bus"):
#             return "Bus"
#     if len(input) >= 3:
#         if (input[0:3] == "bus" or input[0:3] == "Bus"):
#             return "Bus"
#     else:
#         return None


# def input_processing_level3(input, city):
#     if input == "help":
#         print("The following inputs are legitimate queries:")
#         print(">>> Bus 387-405, 406-420")
#         print(">>> Route 61D, 61C, 64")
#         print(">>> Stop 4405, 7117")
#         main_call(city)
#     else:
#         function = mode_select(input)
#         if function != None:
#             data_select(input, function, city)
#         else: 
#             print("Error: invalid input. Please try again!")
#             main_call(input, city)


# def main_call(city):
#     z = input("Make your selection now: ")
#     input_processing_level3(z, city)


# def input_processing_level2(input):
#     features = supported_functions_by_city()
#     if input == "satx":
#         city_name = "satx"
#         listed_features(features, input)
#         main_call(city_name)
#     elif input == "pgh":
#         city_name = "pgh"
#         listed_features(features, input)
#         main_call(city_name)
#     else:
#         print("Error: invalid input. Please try again!")
#         body_second_pass()


# def input_processing_level1(input):
#     if input == "help":
#         print("Type one of the following cities:")
#         for i in supported_cities():
#             print(i)
#         print("For debug mode, type 'debug'.")
#         body_second_pass()
#     elif input == "Pittsburgh" or input == "pittsburgh":
#         input_processing_level2("pgh")
#     elif (input == "San Antonio" or input == "san antonio" 
#         or input == "San antonio"):
#         input_processing_level2("satx")
#     else: 
#         print("Error: invalid input. Please try again!")
#         body_second_pass()
        

# def body_second_pass():
#     x = input("Select a city or type 'help' below. ")
#     input_processing_level1(x)


# def body():
#     print("Welcome to TransitFoamer!")
#     x = input("Select a city or type 'help' below. ")
#     input_processing_level1(x)


# body()


