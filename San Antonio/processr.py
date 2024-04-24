import pprint as PP
pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

busRoute = {}
busStatus = {}
busStopSeq = {}
busLat = {}
busLong = {}
busTime = {}
busTripId = {}
busDate = {}

def data_process(data):
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
            full_process(attributes, vid)
        else:
            partial_process(attributes)
    vid_list.sort()
    pprint(busRoute)

def partial_process(attributes):
    pass

def full_process(attributes, vid):
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
    busLat[vid] = lat
    busLong[vid] = long
    busTime[vid] = time
    busTripId[vid] = tripId
    busDate[vid] = date

    # hdg = position["bearing"]
    # spd = position["speed"]

    ## Further probing of dictionaries:

