import gtfsrt_pb2
import requests
from google.protobuf import json_format

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
    
def main_1() -> None:
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(rt1_endpoint)

    bytestream, rest_status = response.content, response.status_code  # NOTE: always decode protobuf response as byte stream

    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{rt1_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status)}")
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
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str1) / 1000} KB\x1b[0m")
   

    print(f"\n\x1b[32mSuccessfully wrote output to \x1b[34m{output_path1}\x1b[0m")

def main_2() -> None:
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(rt2_endpoint)

    bytestream, rest_status = response.content, response.status_code  # NOTE: always decode protobuf response as byte stream

    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{rt2_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status)}")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream) / 1000} KB\x1b[0m")
    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg = gtfsrt_pb2.FeedMessage() 

    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place

    proto_status1 = feedmsg.ParseFromString(bytestream)

    # All protobuf classes can be converted to a debug string by using the string constructor

    fm_str2 = str(feedmsg)
    data = json_format.MessageToDict(feedmsg)
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    write_to_file(output_path2, fm_str2)

    return data

def main_3() -> None:
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(rt3_endpoint)

    bytestream, rest_status = response.content, response.status_code  # NOTE: always decode protobuf response as byte stream

    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{rt3_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status)}")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream) / 1000} KB\x1b[0m")
    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg = gtfsrt_pb2.FeedMessage() 

    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place

    proto_status1 = feedmsg.ParseFromString(bytestream)

    # All protobuf classes can be converted to a debug string by using the string constructor

    fm_str3 = str(feedmsg)
    data = json_format.MessageToDict(feedmsg)
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    write_to_file(output_path3, fm_str3)

    return data

def main_4() -> None:
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(rt4_endpoint)

    bytestream, rest_status = response.content, response.status_code  # NOTE: always decode protobuf response as byte stream

    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{rt4_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status)}")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream) / 1000} KB\x1b[0m")
    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg = gtfsrt_pb2.FeedMessage() 

    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place

    proto_status1 = feedmsg.ParseFromString(bytestream)

    # All protobuf classes can be converted to a debug string by using the string constructor

    fm_str4 = str(feedmsg)
    data = json_format.MessageToDict(feedmsg)
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    write_to_file(output_path4, fm_str4)

    return data