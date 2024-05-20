import gtfsrt_pb2
import requests
from google.protobuf import json_format

prt_bus_vehicles: str = "https://truetime.portauthority.org/gtfsrt-bus/vehicles"
prt_bus_trips: str = "https://truetime.portauthority.org/gtfsrt-bus/trips"
prt_train_vehicles: str = "https://truetime.portauthority.org/gtfsrt-train/vehicles"
prt_train_trips: str = "https://truetime.portauthority.org/gtfsrt-train/trips"
via_bus_vehicles: str = "http://gtfs.viainfo.net/vehicle/vehiclepositions.pb"
via_bus_trips: str = "http://gtfs.viainfo.net/tripupdate/tripupdates.pb"



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


def main(endpoint, output):
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(endpoint)
    bytestream, rest_status = response.content, response.status_code
    # Always decode protobuf response as byte stream
    # Debug print statements
    print(f"""\x1b[33mGET \x1b[34m{endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status)}, 
          \x1b[33m Response has length \x1b[34m{len(bytestream) / 1000} KB\x1b[0m""")
    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg = gtfsrt_pb2.FeedMessage()
    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place
    proto_status1 = feedmsg.ParseFromString(bytestream)
    # All protobuf classes can be converted to a debug string by using the string constructor
    fm_str = str(feedmsg)
    data = json_format.MessageToDict(feedmsg)
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status1}\x1b[0m]")
    write_to_file(output, fm_str)
    # Write output to output_path and additional pretty prints :3
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str) / 1000} KB\x1b[0m")
    print(f"\n\x1b[32mSuccessfully wrote output to \x1b[34m{output}\x1b[0m")
    return data


