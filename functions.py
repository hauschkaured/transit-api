from trip_processing import *
from static.interface import *
from realtime_interface import *


def bus_list_grabber(vdata):
    buses = dict()
    print(type(vdata))
    print(type(vdata.entity))
    for i in vdata.entity:
        k = vdata.entity[i]





def buses_in_range(foo, bar, vdata, tdata, city):
    print(tdata)
    min_int = int(foo)
    max_int = int(bar)
    bus_list_grabber(vdata)
    stops = static_fetcher(city, "stops")
    # for i in range(min_int, max_int+1):
    #     if i in bus_dict:
    #         list_id = bus_dict[i]



