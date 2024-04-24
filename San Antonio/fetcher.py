import gtfsrt_pb2
import requests
from google.protobuf import json_format
import pprint as PP
from stop_names import stopNames

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

rt_endpoint: str = "http://gtfs.viainfo.net/vehicle/vehiclepositions.pb"  # GTFS-RT Endpoint
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

def data_process(data):
    busRoute = {}
    busStatus = {}
    busStopSeq = {}
    busLat = {}
    busLong = {}
    busTime = {}
    busTripId = {}
    busDate = {}
    busStopId = {}
    vid_list = []
    checkList = ["currentStatus", "currentStopSequence", "trip", "position", "vehicle"]
    for entry in data["entity"]:
        vid = entry["id"]
        vid_list.append(vid)       
        ## Layer 2 dictionary
        attributes = entry["vehicle"]
        ticker = 0
        for i in checkList:
            if i in attributes:
                ticker += 1
        if ticker == 5:
            full_process(attributes, vid, busRoute, busStatus, busStopSeq, busStopId,
                         busLat, busLong, busTime, busTripId, busDate)
        else:
            partial_process(attributes)
    vid_list.sort()

def partial_process(attributes):
    pass

def full_process(attributes, vid, busRoute, busStatus, busStopSeq, busStopId, 
                 busLat, busLong, busTime, busTripId, busDate):
    ## Dictionaries to probe and other data
    status = attributes["currentStatus"]
    stopseq = attributes["currentStopSequence"]
    position = attributes["position"]
    stopId = attributes["stopId"]
    time = attributes["timestamp"]
    trip = attributes["trip"]
    vid = attributes["vehicle"]["id"]

    route = trip["routeId"]
    date = trip["startDate"]
    tripId = trip["tripId"]

    lat = position["latitude"]
    long = position["longitude"]

    busRoute[vid] = route
    busStatus[vid] = status
    busStopSeq[vid] = stopseq
    busStopId[vid] = stopId
    busLat[vid] = lat
    busLong[vid] = long
    busTime[vid] = time
    busTripId[vid] = tripId
    busDate[vid] = date

    pprint(busRoute)

    busesOnRoute("93", busRoute, busStopId, busStatus)



    # hdg = position["bearing"]
    # spd = position["speed"]
def busesOnRoute(rte, busRoute, busStopId, busStatus):
    busList = []
    for bus in busRoute:
        if busRoute[bus] == rte:
            busList.append(bus)
            status = busStatus[bus]
            id = busStopId[bus]
            stop = stopName(id)
            print(f"Bus {bus} on route {rte} is {status} {stop}")    



def stopName(id):
    return stopNames[id]






def main() -> None:
    # REST GET request to get protobuf data from endpoint
    response: requests.Response = requests.get(rt_endpoint)
    bytestream, rest_status = response.content, response.status_code  # NOTE: always decode protobuf response as byte stream

    # Debug print statements, odd escape sequences are to add colors, dwai it
    print(f"\x1b[33mGET \x1b[34m{rt_endpoint} \x1b[33m: returned status {rest_status_color_helper(rest_status)}")
    print(f"\x1b[33m    Reponse has length \x1b[34m{len(bytestream) / 1000} KB\x1b[0m")

    # Create an empty instance of a FeedMessage (the class that holds all GTFS-RT data)
    # We will populate this later
    feedmsg = gtfsrt_pb2.FeedMessage() 

    # Use byte stream from response to Parse into object
    # NOTE: The function returns a status code. The data is populated in place
    proto_status = feedmsg.ParseFromString(bytestream)

    # All protobuf classes can be converted to a debug string by using the string constructor
    fm_str = str(feedmsg)
    data = json_format.MessageToDict(feedmsg)
    data_process(data)

    
    # Write output to output_path and additional pretty prints :3 
    print(f"\n\x1b[33mStatusCode from \x1b[36mfeedmsg.ParseFromString(...) \x1b[0m: \x1b[34m{proto_status}\x1b[0m]")
    print(f"\x1b[33m    debug str has size \x1b[34m{len(fm_str) / 1000} KB\x1b[0m")
    # write_to_file(output_path, fm_str)
    # print(f"\n\x1b[32mSuccessfully wrote output to \x1b[34m{output_path}\x1b[0m")

if __name__ == "__main__":
    main()

