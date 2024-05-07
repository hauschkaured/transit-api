from typing import Dict, Any
from .. import utils
from .. import defs
import os


class Trips:
    def __init__(self, route_id, service_id, trip_id, headsign, short_name, 
                 direction_id, block_id, shape_id, wheelchair, bikes):
        self.route_id = route_id
        self.service_id = service_id
        self.trip_id = trip_id
        self.headsign = headsign
        self.short_name = short_name
        self.direction_id = direction_id
        self.block_id = block_id
        self.shape_id = shape_id
        self.wheelchair = wheelchair
        self.bikes = bikes
        
    def __repr__(self):
        return(f'''{self.route_id}, {self.service_id}, {self.trip_id},\n 
               {self.headsign}, {self.direction_id}, {self.block_id},\n
               {self.shape_id}, {self.wheelchair}, {self.bikes}\n''') 


def import_gtfs(path) -> Dict[str, Any]:  # See src/common/gtfs_agency.py for how this code works
    trips = {}
    text = utils.read_file(os.path.join(path, defs.GTFS_STATIC_TRIPS))
    for line in text.splitlines()[1:]:
        obj = Trips(*line.split(','))
        trips[obj.trip_id] = obj
    return trips

# trips = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
#     route_id = line[0:indexList[0]]
#     service_id = line[indexList[0]+1:indexList[1]]
#     trip_id = line[indexList[1]+1:indexList[2]]
#     headsign = line[indexList[2]+1:indexList[3]]
#     short_name = line[indexList[3]+1:indexList[4]]
#     direction_id = line[indexList[4]+1:indexList[5]]
#     block_id = line[indexList[5]+1:indexList[6]]
#     shape_id = line[indexList[6]+1:indexList[7]]
#     wheelchair = line[indexList[7]+1:indexList[8]]
#     bikes = line[indexList[8]+1:]
#     obj = Trips(route_id, service_id, trip_id, headsign, short_name, 
#                 direction_id, block_id, shape_id, wheelchair, bikes)
#     trips[trip_id] = obj