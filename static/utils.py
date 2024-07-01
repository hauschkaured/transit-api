from interface import *

def trips_on_route(route, trips_data):
    for line in trips_data.splitlines():
        items = line.split(',')
        route_data = items[1]
        trip = items[0]
        if route == route_data:
            print(route, trip)
            print(stops_on_trip(trip))


def trips_analyzer():
    trips = open("pittsburgh/trips.txt", "r")
    trips_data = trips.read()
    pattern_analyzer("2", trips_data)
    print(trips_on_route('RLSH', trips_data))

    # print(f"Pattern 1 has {trips_per_pattern("1", trips_data)} trips (Saturday)")
    # print(f"Pattern 2 has {trips_per_pattern("2", trips_data)} trips (Sunday)")
    # print(f"Pattern 3 has {trips_per_pattern("3", trips_data)} trips (Thursday)")
    # print(f"Pattern 4 has {trips_per_pattern("4", trips_data)} trips (M-F)")

def pattern_analyzer(pattern, trips_data): # Routes that run on a given PATTERN
    buses = set()
    for line in trips_data.splitlines():
        items = line.split(',')
        if items[2] == pattern:
            buses.add(items[1])
    return buses

def trips_per_pattern(pattern, trips_data):
    count = 0
    for line in trips_data.splitlines():
        items = line.split(',')
        if items[2] == pattern:
            if items[1] == "RLSH" or items[1] == "BLUE" or items[1] == "SLVR":
                count += 1
    return count


def stops_on_trip(trip):
    stop_times = open("pittsburgh/stop_times.txt", "r")
    stop_times_data = stop_times.read()
    for line in stop_times_data.splitlines():
        index_start = line.find(',')
        trip_data = line[0:index_start]
        if trip_data == trip:
            items = line.split(',')
            arrival = items[1]
            departure = items[2]
            stop_number = items[3]
            stops_dict = static_fetcher("pgh", "stops")
            stop_name = stops_dict[stop_number].stop_name
            print(arrival, departure, stop_name)

trips_analyzer()

