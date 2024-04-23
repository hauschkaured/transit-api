import gtfs_realtime_pb2
import requests


bus_endpoint: str = "https://truetime.portauthority.org/gtfsrt-bus/vehicles"  # GTFS-RT Endpoint
bustrip_endpoint: str = "https://truetime.portauthority.org/gtfsrt-bus/trips"
train_endpoint: str = "https://truetime.portauthority.org/gtfsrt-train/vehicles"
traintrip_endpoint: str = "https://truetime.portauthority.org/gtfsrt-train/trips"


output_path: str = "./gtfs_rt.out"  # Path for final written output, WARNING: WILL OVERWRITE EXISTING FILES

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
    response1: requests.Response = requests.get(bus_endpoint)
    bytestream1, rest1_status = response1.content, response1.status_code  # NOTE: always decode protobuf response as byte stream

# REST GET request to get protobuf data from endpoint
    response2: requests.Response = requests.get(bustrip_endpoint)
    bytestream2, rest2_status = response1.content, response1.status_code  # NOTE: always decode protobuf response as byte stream

    # REST GET request to get protobuf data from endpoint
    response3: requests.Response = requests.get(train_endpoint)
    bytestream3, rest3_status = response1.content, response1.status_code  # NOTE: always decode protobuf response as byte stream

    # REST GET request to get protobuf data from endpoint
    response4: requests.Response = requests.get(traintrip_endpoint)
    bytestream4, rest4_status = response1.content, response1.status_code  # NOTE: always decode protobuf response as byte stream


    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{bus_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest1_status)}")
    print(f"\x1b[33mGET \x1b[34m{bustrip_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest2_status)}")
    print(f"\x1b[33mGET \x1b[34m{train_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest3_status)}")
    print(f"\x1b[33mGET \x1b[34m{traintrip_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest4_status)}")

    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream1) / 1000} KB\x1b[0m")

    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg1 = gtfs_realtime_pb2.FeedMessage() 
    feedmsg2 = gtfs_realtime_pb2.FeedMessage() 
    feedmsg3 = gtfs_realtime_pb2.FeedMessage() 
    feedmsg4 = gtfs_realtime_pb2.FeedMessage() 


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


    # Write output to output_path and additional pretty prints :3 
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status2}\x1b[0m]")
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status3}\x1b[0m]")
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status4}\x1b[0m]")
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str1) / 1000} KB\x1b[0m")
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str2) / 1000} KB\x1b[0m")
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str3) / 1000} KB\x1b[0m")
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str4) / 1000} KB\x1b[0m")

    write_to_file(output_path, fm_str1)
    print(f"\n\x1b[32mSuccessfully wrote output to \x1b[34m{output_path}\x1b[0m")

if __name__ == "__main__":
    main()



