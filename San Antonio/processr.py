import pprint as PP
pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

class BusData:
    def __init__(self, status, stopseq, stopId, time, vid, route, date, tripId, lat, long):
        self.status = status,
        self.stopseq = stopseq,
        self.stopId = stopId,
        self.time = time,
        self.vid = vid,
        self.route = route,
        self.date = date,
        self.tripId = tripId,
        self.lat = lat,
        self.long = long

    def __repr__(self):
        return f'{self.status, self.stopseq, self.stopId, self.time, self.vid}'
    
def data_process(data):
    checkList = ["currentStatus", "currentStopSequence", "trip", "position", "vehicle"]
    for entry in data["entity"]:
        vid = entry["id"]        
        ## Layer 2 dictionary
        attributes = entry["vehicle"]
        
        ticker = 0
        for i in checkList:
            if i in attributes:
                ticker += 1
        if ticker == 5:
            full_process(attributes)
        else:
            partial_process(attributes)


def partial_process(attributes):
    pass

def full_process(attributes):
    pprint(attributes)
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
    # hdg = position["bearing"]
    # spd = position["speed"]

    ## Further probing of dictionaries:

    vid = BusData(status, stopseq, stopId, time, vid, route, date, tripId, lat, long)