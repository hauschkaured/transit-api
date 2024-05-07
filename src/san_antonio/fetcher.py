from typing import Dict, Any
from common import gtfsrt_pb2, utils, defs
from common.utils import write_to_file
import requests
from google.protobuf import json_format
import pprint as PP

## Configured Pretty Printing

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

## Endpoints and output files
output_path1: str = "./vehiclepositions.out"  # Path for final written output, WARNING: WILL OVERWRITE EXISTING FILES
output_path2: str = "./tripupdates.out"

def rest_status_color_helper(code: int) -> str:
    """
    Changes text color in supported terminals based on status code.
    
    200-299: Success, green
    300-399: Unsure,  yellow
    400+   : Failed,  red
    """
    ansi_esc: int = 32 if code < 300 else 33 if code < 400 else 31
    return f'\x1b[{ansi_esc}m{code}\x1b[0m'

def fetch_vehicles() -> Dict[str, Any]:
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(defs.SAN_ANTONIO_RT_VEHICLEPOSITION)

    bytestream, rest_status = response.content, response.status_code  # NOTE: always decode protobuf response as byte stream

    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{defs.SAN_ANTONIO_RT_VEHICLEPOSITION} \x1b[33m: returned status {rest_status_color_helper(rest_status)}")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream) / 1000} KB\x1b[0m")
    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg = gtfsrt_pb2.FeedMessage() 

    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place

    proto_status1 = feedmsg.ParseFromString(bytestream)

    # All protobuf classes can be converted to a debug string by using the string constructor

    fm_str1 = str(feedmsg)
    data = json_format.MessageToDict(feedmsg)
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    write_to_file(output_path1, fm_str1)

    return data
    

def fetch_tripupdate() -> Dict[str, Any]:
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(defs.SAN_ANTONIO_RT_TRIPUPDATE)

    bytestream, rest_status = response.content, response.status_code  # NOTE: always decode protobuf response as byte stream

    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{defs.SAN_ANTONIO_RT_TRIPUPDATE} \x1b[33m: returned status {rest_status_color_helper(rest_status)}")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream) / 1000} KB\x1b[0m")
    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg = gtfsrt_pb2.FeedMessage() 

    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place

    proto_status1 = feedmsg.ParseFromString(bytestream)

    # All protobuf classes can be converted to a debug string by using the string constructor
    
    fm_str1 = str(feedmsg)
    data = json_format.MessageToDict(feedmsg)
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    write_to_file(output_path1, fm_str1)

    return data
    
    # Write output to output_path and additional pretty prints :3 
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    # print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status2}\x1b[0m]")
    print(f"\x1b[33m    debug str1 has size \x1b[34m{len(fm_str1) / 1000} KB\x1b[0m")
    # print(f"\x1b[33m    debug str2 has size \x1b[34m{len(fm_str2) / 1000} KB\x1b[0m")
    write_to_file(output_path1, fm_str1)
    # write_to_file(output_path2, fm_str2)
    print(f"\n\x1b[32mSuccessfully wrote output to \x1b[34m{output_path1}\x1b[0m")
    # print(f"\n\x1b[32mSuccessfully wrote output to \x1b[34m{output_path2}\x1b[0m")


# def data_process(data):
#     busRoute = {}
#     busStatus = {}
#     busStopSeq = {}
#     busLat = {}
#     busLong = {}
#     busTime = {}
#     busTripId = {}
#     busDate = {}
#     busStopId = {}
#     vid_list = []


#     for entry in data["entity"]:
#         pprint(entry)

#     checkList = ["currentStatus", "currentStopSequence", "trip", "position", "vehicle"]
#     for entry in data["entity"]:
#         vid = entry["id"]
#         ## Layer 2 dictionary
#         attributes = entry["vehicle"]
#         ticker = 0
#         for i in checkList:
#             if i in attributes:
#                 ticker += 1
#         if ticker == 5:
#             full_process(attributes, vid, busRoute, busStatus, busStopSeq, busStopId,
#                          busLat, busLong, busTime, busTripId, busDate)
#         else:
#             partial_process(attributes)
#     vid_list.sort()

# def partial_process(attributes):
#     pass

# def full_process(attributes, vid, busRoute, busStatus, busStopSeq, busStopId, 
#                  busLat, busLong, busTime, busTripId, busDate):
#     ## Dictionaries to probe and other data
#     status = attributes["currentStatus"]
#     stopseq = attributes["currentStopSequence"]
#     position = attributes["position"]
#     stopId = attributes["stopId"]
#     time = attributes["timestamp"]
#     trip = attributes["trip"]
#     vid = attributes["vehicle"]["id"]

#     route = trip["routeId"]
#     date = trip["startDate"]
#     tripId = trip["tripId"]

#     lat = position["latitude"]
#     long = position["longitude"]

#     busRoute[vid] = route
#     busStatus[vid] = status
#     busStopSeq[vid] = stopseq
#     busStopId[vid] = stopId
#     busLat[vid] = lat
#     busLong[vid] = long
#     busTime[vid] = time
#     busTripId[vid] = tripId
#     busDate[vid] = date

#     busesOnRoute("93", busRoute, busStopId, busStatus, busLat, busLong)
#     busesOnRoute("17", busRoute, busStopId, busStatus, busLat, busLong)
#     busesOnRoute("64", busRoute, busStopId, busStatus, busLat, busLong)
#     busesOnRoute("7", busRoute, busStopId, busStatus, busLat, busLong)





#     # hdg = position["bearing"]
#     # spd = position["speed"]

# def busesOnRoute(rte, busRoute, busStopId, busStatus, busLat, busLong): ## FUNCTION 1
#     busList = []
#     for bus in busRoute:
#         if busRoute[bus] == rte:
#             busList.append(bus)
#             stop = busStopId[bus]
#             if stop in stops:
#                 name = stops[stop] 
#             status = busStatus[bus]
#             lat = busLat[bus]
#             long = busLong[bus]
#             if status == "IN_TRANSIT_TO":
#                 status = "in transit to"
#             elif status == "STOPPED_AT":
#                 status = "stopped at"
#             if stop in stops:
#                 print(f"\x1b[33mRoute \x1b[34m{rte} #{bus} \x1b[0m is {status} {name}")    
#             if status == "in transit to":
#                 print(f"    lat {lat} long {long}")
