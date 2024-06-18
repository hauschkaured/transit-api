from fetcher import *
from functions import *
from trip_processing import *

import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint


def supported_cities():
    city_list = ["Pittsburgh", "San Antonio"]
    return city_list


def supported_functions_by_city():
    functions_dict = {
        "satx": ["bus", "route"],
        "pgh": ["bus", "route", "stop"]
    }
    return functions_dict


def listed_features(features, foo):
    available_features = features[foo]
    print(f"Features: {available_features}")


def list_of_values(foo):
    dash_index = foo.find('-')
    value_1 = foo[:dash_index]
    value_2 = foo[dash_index+1:]
    values = [value_1, value_2]
    return values


def data_select(foo, function, city):
    length = len(function)
    raw_data = foo[length+1:]
    if city == "satx":
        # Online
        vehicle_data = main(via_bus_vehicles, "./via_bus_vehicles.out")
        trip_data = main(via_bus_trips, "./via_bus_trips.out")
        vdata = processing(vehicle_data, "vehicle_position")
        tdata = processing(trip_data, "trip_update")
        data_analyzer(raw_data, function, vdata, tdata, city)
    elif city == "pgh":
        # Online
        vehicle_data = main(prt_bus_vehicles, "./prt_bus_vehicles.out")
        trip_data = main(prt_bus_trips, "./prt_bus_trips.out")
        # trainData = main(prt_train_vehicles, "./prt_train_vehicles.out")
        # trainTripData = main(prt_train_trips, "./prt_train_trips.out")
        vdata = processing(vehicle_data, "vehicle_position")
        tdata = processing(trip_data, "trip_update")
        data_analyzer(raw_data, function, vdata, tdata, city)

def data_analyzer(raw_data, function, vdata, tdata, city):
    for item in raw_data.split(','):
        if function == "Bus":
            if item.count('-') > 0:
                values = list_of_values(item)
                min_val = values[0]
                max_val = values[1]
                buses_in_range(min_val, max_val, vdata, tdata, city)
        elif function == "Stop":
            if item.count('-') > 0:
                pass
            else:
                pass
        elif function == "Route":
            route = item
            buses_on_route(route, vdata, tdata, city)
    


def mode_select(foo):
    if len(foo) >= 5:
        if foo[0:5] == "route" or foo[0:5] == "Route":
            return "Route"
        elif foo[0:4] == "stop" or foo[0:4] == "Stop":
            return "Stop"
        elif foo[0:3] == "bus" or foo[0:3] == "Bus":
            return "Bus"
    if len(foo) >= 4:
        if foo[0:4] == "stop" or foo[0:4] == "Stop":
            return "Stop"
        elif foo[0:3] == "bus" or foo[0:3] == "Bus":
            return "Bus"
    if len(foo) >= 3:
        if foo[0:3] == "bus" or foo[0:3] == "Bus":
            return "Bus"
    else:
        return "None"


def input_processing_level3(foo, city):
    if foo == "help":
        print("The following inputs are legitimate queries:")
        print(">>> Bus 387-405, 406-420")
        print(">>> Route 61D, 61C, 64")
        print(">>> Stop 4405, 7117")
        main_call(city)
    else:
        function = mode_select(foo)
        if function != "None":
            data_select(foo, function, city)
        else:
            print("Error: invalid input. Please try again!")
            main_call(city)


def main_call(city):
    z = input("Make your selection now: ")
    input_processing_level3(z, city)


def input_processing_level2(foo):
    features = supported_functions_by_city()
    if foo == "satx":
        city_name = "satx"
        listed_features(features, foo)
        main_call(city_name)
    elif foo == "pgh":
        city_name = "pgh"
        listed_features(features, foo)
        main_call(city_name)
    else:
        print("Error: invalid input. Please try again!")
        body_second_pass()


def input_processing_level1(foo):
    if foo == "help":
        print("Type one of the following cities:")
        for i in supported_cities():
            print(i)
        print("For debug mode, type 'debug'.")
        body_second_pass()
    elif foo == "Pittsburgh" or foo == "pittsburgh":
        input_processing_level2("pgh")
    elif (foo == "San Antonio" or foo == "san antonio"
        or foo == "San antonio"):
        input_processing_level2("satx")
    else:
        print("Error: invalid input. Please try again!")
        body_second_pass()


def body_second_pass():
    x = input("Select a city or type 'help' below. ")
    input_processing_level1(x)


def body():
    print("Welcome to TransitFoamer!")
    x = input("Select a city or type 'help' below. ")
    input_processing_level1(x)


body()
