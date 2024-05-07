from typing import Dict, Any
from .. import utils
from .. import defs
import os

class Shapes:
    def __init__(self, id, lat, lon, sequence, dist_traveled): 
        self.id = id
        self.lat = lat
        self.lon = lon
        self.sequence = sequence
        self.dist_traveled = dist_traveled

        
    def __repr__(self):
        return(f'''{self.id}, {self.lat}, {self.lon}''')

    
# shapes = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
#     id = line[0:indexList[0]]
#     lat = line[indexList[0]+1:indexList[1]]
#     lon = line[indexList[1]+1:indexList[2]]
#     sequence = line[indexList[2]+1:indexList[3]]
#     dist_traveled = line[indexList[3]+1:]
#     obj = Shapes(id, lat, lon, sequence, dist_traveled)
#     shapes[lon] = obj


def import_gtfs(path) -> Dict[str, Any]:  # See src/common/gtfs_agency.py for how this code works
    """
    Given a path to the "gtfs_static_feed" directory, this path will
    read in agency information and return it in a JSON-esque dictionary 
    """
    shapes = {}
    text = utils.read_file(os.path.join(path, defs.GTFS_STATIC_SHAPES))
    for line in text.splitlines()[1:]:
        obj = Shapes(*line.split(','))
        shapes[obj.lon] = obj
    return shapes