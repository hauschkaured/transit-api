import gtfsrt_pb2
import requests
from google.protobuf import json_format
import pprint as PP

import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

rt1_endpoint: str = "https://truetime.portauthority.org/gtfsrt-bus/vehicles"  # GTFS-RT Endpoint
rt2_endpoint: str = "https://truetime.portauthority.org/gtfsrt-bus/trips"  # GTFS-RT Endpoint
rt3_endpoint: str = "https://truetime.portauthority.org/gtfsrt-train/vehicles"  # GTFS-RT Endpoint
rt4_endpoint: str = "https://truetime.portauthority.org/gtfsrt-train/trips"  # GTFS-RT Endpoint

output_path1: str = "./vehiclepositions_bus.out"  # Path for final written output, WARNING: WILL OVERWRITE EXISTING FILES
output_path2: str = "./tripupdates_bus.out"  # Path for final written output, WARNING: WILL OVERWRITE EXISTING FILES
output_path3: str = "./vehiclepositions_train.out"  # Path for final written output, WARNING: WILL OVERWRITE EXISTING FILES
output_path4: str = "./tripupdates_train.out"  # Path for final written output, WARNING: WILL OVERWRITE EXISTING FILES


def rest_status_color_helper(code: int) -> str:
    """
    Changes text color in supported terminals based on status code.
    
    200-299: Success, green
    300-399: Unsure,  yellow
    400+   : Failed,  red
    """
    ansi_esc: int = 32 if code < 300 else 33 if code < 400 else 31
    return f'\x1b[{ansi_esc}m{code}\x1b[0m'

def write_to_file(path: str, content: str) -> None:
    """
    Writes the content string to the specified path
    """
    with open(path, 'w') as f:
        f.write(content)
    
def main() -> None:
    # REST GET request to get protobuf data from endpoint
    response1: requests.Response = requests.get(rt1_endpoint)
    response2: requests.Response = requests.get(rt2_endpoint)
    response3: requests.Response = requests.get(rt3_endpoint)
    response4: requests.Response = requests.get(rt4_endpoint)

    bytestream1, rest_status1 = response1.content, response1.status_code  # NOTE: always decode protobuf response as byte stream
    bytestream2, rest_status2 = response2.content, response2.status_code  # NOTE: always decode protobuf response as byte stream
    bytestream3, rest_status3 = response3.content, response3.status_code  # NOTE: always decode protobuf response as byte stream
    bytestream4, rest_status4 = response4.content, response4.status_code  # NOTE: always decode protobuf response as byte stream


    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{rt1_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status1)}")
    print(f"\x1b[33mGET \x1b[34m{rt2_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status2)}")
    print(f"\x1b[33mGET \x1b[34m{rt3_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status3)}")
    print(f"\x1b[33mGET \x1b[34m{rt4_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status4)}")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream1) / 1000} KB\x1b[0m")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream2) / 1000} KB\x1b[0m")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream3) / 1000} KB\x1b[0m")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream4) / 1000} KB\x1b[0m")


    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg1 = gtfsrt_pb2.FeedMessage() 
    feedmsg2 = gtfsrt_pb2.FeedMessage() 
    feedmsg3 = gtfsrt_pb2.FeedMessage() 
    feedmsg4 = gtfsrt_pb2.FeedMessage() 




    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place
    proto_status1 = feedmsg1.ParseFromString(bytestream1)
    proto_status2 = feedmsg2.ParseFromString(bytestream2)
    proto_status3 = feedmsg3.ParseFromString(bytestream3)
    proto_status4 = feedmsg4.ParseFromString(bytestream4)


    # All protobuf classes can be converted to a debug string by using the string constructor
    fm_str1 = str(feedmsg1)
    fm_str2 = str(feedmsg2)
    fm_str3 = str(feedmsg3)
    fm_str4 = str(feedmsg4)

    data1 = json_format.MessageToDict(feedmsg1)
    data2 = json_format.MessageToDict(feedmsg2)
    data3 = json_format.MessageToDict(feedmsg3)
    data4 = json_format.MessageToDict(feedmsg4)
   
    return data1

    # Write output to output_path and additional pretty prints :3 
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str1) / 1000} KB\x1b[0m")
    write_to_file(output_path1, fm_str1)
    write_to_file(output_path2, fm_str2)
    write_to_file(output_path3, fm_str3)
    write_to_file(output_path4, fm_str4)

    print(f"\n\x1b[32mSuccessfully wrote output to \x1b[34m{output_path1}\x1b[0m")

if __name__ == "__main__":
    main()
