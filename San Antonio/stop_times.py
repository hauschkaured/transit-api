text = open("gtfs_static_feed/stop_times.txt", "r")

class Stoptimes:
    def __init__(self, id, arrival, departure, stop_id, stopseq, headsign, 
                 pickup_type, dropoff_type, shape_dist_traveled, timepoint):
        self.id = id
        self.arrival = arrival
        self.departure = departure
        self.stop_id = stop_id
        self.stopseq = stopseq
        self.headsign = headsign
        self.pickup_type = pickup_type
        self.dropoff_type = dropoff_type
        self.shape_dist_traveled = shape_dist_traveled
        self.timepoint = timepoint

    def __repr__(self):
        return f"{self.departure}, {self.stopseq}, {self.headsign}"
    
stoptimes = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    id = line[0:indexList[0]]
    arrival = line[indexList[0]+1:indexList[1]]
    departure = line[indexList[1]+1:indexList[2]]
    stop_id = line[indexList[2]+1:indexList[3]]
    stopseq = line[indexList[3]+1:indexList[4]]
    headsign = line[indexList[4]+1:indexList[5]]
    pickup_type = line[indexList[5]+1:indexList[6]]
    dropoff_type = line[indexList[6]+1:indexList[7]]
    shape_dist_traveled = line[indexList[7]+1:indexList[8]]
    timepoint = line[indexList[8]+1:indexList[9]]

    obj = Stoptimes(id, arrival, departure, stop_id, stopseq, headsign, 
                pickup_type, dropoff_type, shape_dist_traveled, timepoint)
    stoptimes[stop_id] = obj