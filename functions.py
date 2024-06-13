from static.interface import *
from datetime import datetime


import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint


def status_converter(status):
    if status == "IN_TRANSIT_TO": # This is for VIA only
        return "in transit to"
    if status == "STOPPED_AT":
        return "stopped at"


def time_converter(foo):
    time_new = datetime.fromtimestamp(foo).strftime('%H:%M:%S')
    return time_new


def bus_trip(foo, trip, vdata, tdata, city):
    if city == "satx":
        bus_data = vdata.entity[foo]
        bus_model = bus_data.vehicle.vehicle.id
        bus_route = bus_data.vehicle.trip.route_id

        routes = static_fetcher(city, "routes")
        trips = static_fetcher(city, "trips")
        stops = static_fetcher(city, "stops")

        route_name = routes[bus_route].route_long_name
        if trip in trips:
            trip_headsign = trips[trip].trip_headsign
            combined_name = f"\x1b[33mRoute \x1b[34m{bus_route} \x1b[35m{route_name} to \x1b[36m{trip_headsign}\x1b[0m"
        else:
            combined_name = f"\x1b[33mRoute \x1b[34m{bus_route} \x1b[35m{route_name}\x1b[0m"


        current_trip = tdata.entity[trip]
        current_stop = current_trip.trip_update.stop_time_update[0]
        current_stop_name = stops[current_stop.stop_id].stop_name

        if bus_data.vehicle.current_status:
            bus_status = status_converter(bus_data.vehicle.current_status)
        else:
            bus_status = "in transit to"
        string_return = f"#{bus_model} {combined_name} is {bus_status} {current_stop_name}\n"
        if current_stop.arrival is not None and current_stop.departure is not None:
            time_a = time_converter(int(current_stop.arrival.time))
            time_d = time_converter(int(current_stop.departure.time))
            string = f"Arrives at {current_stop_name} at {time_a}. Departs at {time_d}."
        elif current_stop.arrival is not None and current_stop.departure is None:
            time = time_converter(int(current_stop.arrival.time))
            string = f"Arrives at {current_stop_name} at {time}."
        elif current_stop.arrival is None and current_stop.departure is not None:
            time = time_converter(int(current_stop.departure.time))
            string = f"Departs from {current_stop_name} at {time}."
        else:
            string = ''
        print(string_return)
        print(string)


def buses_in_range(foo, bar, vdata, tdata, city):
    min_int = int(foo)
    max_int = int(bar)
    for i in range(min_int, max_int+1):
        if str(i) in vdata.entity:
            bus = vdata.entity[str(i)]
            if bus.vehicle.trip:
                trip = bus.vehicle.trip.trip_id
                bus_trip(str(i), trip, vdata, tdata, city)


def buses_on_route(route, vdata, tdata, city):
    for bus in vdata.entity:
        if vdata.entity[bus].vehicle:
            if vdata.entity[bus].vehicle.trip:
                if vdata.entity[bus].vehicle.trip.route_id == route:
                    bus_id = vdata.entity[bus].vehicle.vehicle.id
                    trip = vdata.entity[bus].vehicle.trip.trip_id
                    print("The following buses are on Route {route}:")
                    bus_trip(bus_id, trip, vdata, tdata, city)
