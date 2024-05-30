from trip_processing import *
from static.interface import *
from realtime_interface import *
from datetime import datetime

def time_converter(foo):
    time_new = datetime.fromtimestamp(foo).strftime('%H:%M:%S')
    return time_new


def current_stop(trip, tdata, city):
    stops = static_fetcher(city, "stops")
    if trip in tdata.entity:
        current_trip = tdata.entity[trip]
        current_stop = current_trip.trip_update.stop_time_update[0]
        current_stop_name = stops[current_stop.stop_id].stop_name
        if current_stop.arrival != None and current_stop.departure != None:
            time_a = time_converter(int(current_stop.arrival.time))
            time_d = time_converter(int(current_stop.departure.time))
            string = f"Arrives at {current_stop_name} at {time_a}. Departs at {time_d}."
            return string
        elif current_stop.arrival != None and current_stop.departure == None:
            time = time_converter(int(current_stop.arrival.time))
            string = f"Arrives at {current_stop_name} at {time}."
            return string
        elif current_stop.arrival == None and current_stop.departure != None:
            time = time_converter(int(current_stop.departure.time))
            string = f"Departs from {current_stop_name} at {time}."
            return string


def bus_trip(foo, trip, vdata, tdata, city):
    end = current_stop(trip, tdata, city)
    bus = vdata.entity[foo]
    route = bus.vehicle.trip.route_id
    trips = static_fetcher(city, "trips")
    headsign = trips[trip].trip_headsign
    print(f"#{foo} {route} {headsign} {end}")


def bus_no_trip(foo, vdata):
    pass


def bus_information_printer(foo, bus_route_dict, vdata, tdata, city):
    if foo in bus_route_dict:
        if bus_route_dict[foo] != None:
            trip = bus_route_dict[foo]
            bus_trip(foo, trip, vdata, tdata, city)
        else:
            bus_no_trip(foo, vdata)


def bus_list_grabber(vdata):
    buses = dict()
    iterable = vdata.entity
    for i in iterable:
        vehicle_id = iterable[i].vehicle.vehicle.id
        if iterable[i].vehicle.trip != None:
            trip_id = iterable[i].vehicle.trip.trip_id
        else:
            trip_id = None
        buses[vehicle_id] = trip_id
    return buses


def buses_in_range(foo, bar, vdata, tdata, city):
    min_int = int(foo)
    max_int = int(bar)
    bus_route_dict = bus_list_grabber(vdata)
    for i in range(min_int, max_int+1):
        if str(i) in bus_route_dict:
            bus_information_printer(str(i), bus_route_dict, vdata, tdata, city)
