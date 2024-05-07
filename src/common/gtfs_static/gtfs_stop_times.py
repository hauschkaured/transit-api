from typing import Dict, Any
from .. import utils
from .. import defs
import os

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
    

def import_gtfs(path) -> Dict[str, Any]:  # See src/common/gtfs_agency.py for how this code works
    """
    Given a path to the "gtfs_static_feed" directory, this path will
    read in agency information and return it in a JSON-esque dictionary 
    """
    times = {}
    text = utils.read_file(os.path.join(path, defs.GTFS_STATIC_STOP_TIMES))
    for line in text.splitlines()[1:]:
        obj = Stoptimes(*line.split(','))
        times[obj.id] = obj
    return times


# stoptimes = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
#     id = line[0:indexList[0]]
#     arrival = line[indexList[0]+1:indexList[1]]
#     departure = line[indexList[1]+1:indexList[2]]
#     stop_id = line[indexList[2]+1:indexList[3]]
#     stopseq = line[indexList[3]+1:indexList[4]]
#     headsign = line[indexList[4]+1:indexList[5]]
#     pickup_type = line[indexList[5]+1:indexList[6]]
#     dropoff_type = line[indexList[6]+1:indexList[7]]
#     shape_dist_traveled = line[indexList[7]+1:indexList[8]]
#     timepoint = line[indexList[8]+1:]

#     obj = Stoptimes(id, arrival, departure, stop_id, stopseq, headsign, 
#                 pickup_type, dropoff_type, shape_dist_traveled, timepoint)
#     stoptimes[stop_id] = obj
