from fetcher import *
from datetime import datetime
# from San_Antonio.gtfs_stops import via_stops
# from San_Antonio.gtfs_agency import via_agency
# from San_Antonio.gtfs_calendar_dates import via_calendar_dates
# from San_Antonio.gtfs_calendar import via_calendar
# from San_Antonio.gtfs_feed import via_feed
# from San_Antonio.gtfs_routes import via_routes
# from San_Antonio.gtfs_shapes import via_shapes
# from San_Antonio.gtfs_stop_times import via_stoptimes
from San_Antonio.gtfs_stops import via_stops
# from San_Antonio.gtfs_transfers import via_transfers
# from San_Antonio.gtfs_trips import via_trips


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


def buses_on_route(input):
    for bus in busDict:
        busInfo = busDict[bus]
        if "tripRoute" in busInfo:
            busRoute = busInfo["tripRoute"]
            if busRoute == input:
                status = status_converter(busInfo["status"])
                print(f"\x1b[33mRoute \x1b[34m{busRoute} #{busInfo["vid"]} \x1b[0mis {status} {busInfo["stopId"]}")


def buses_in_range_via(low, high):
    print(f"The following buses are in the range {low}-{high}")
    for i in range(low, high + 1):
        if str(i) in busDict:
            busInfo = busDict[str(i)]
            if "status" in busInfo:
                status = status_converter(busInfo["status"])
                stopId = busInfo["stopId"]
                stop = via_stops[stopId].name
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


def status_converter(status):
    if status == "IN_TRANSIT_TO":
        return "in transit to"
    if status == "STOPPED_AT":
        return "stopped at"


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


print("Welcome to TransitFoamer!")
x = input("What city would you like to select? ")

if x == "San Antonio":
    busData = main(via_bus_vehicles, "./via_bus_vehicles.out")
    busTripData = main(via_bus_trips, "./via_bus_trips.out")
    busDict = vehicle_processing_via(busData)
    busTripDict = trip_processing_via(busTripData)
    print("There are two options, route and bus")
    print("For route, enter Route or route followed by a comma separated list of routes.")
    print("For bus, enter bus followed by either the bus in question or a range of buses.")
    print("Format a range thus: 387--405")
    y = input("What would you like to do? ")


elif x == "Pittsburgh":
    busData = main(prt_bus_vehicles, "./prt_bus_vehicles.out")
    busTripData = main(prt_bus_trips, "./prt_bus_trips.out")
    trainData = main(prt_train_vehicles, "./prt_train_vehicles.out")
    trainTripData = main(prt_train_trips, "./prt_train_trips.out")
