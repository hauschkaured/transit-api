from typing import Dict, Any
from .. import utils
from .. import defs
import os

class Routes:
    def __init__(self, id, agency, short_name, long_name, desc, type, url, 
                 color, text):
        self.id = id
        self.agency = agency
        self.short_name = short_name
        self.long_name = long_name
        self.desc = desc
        self.type = type
        self.url = url
        self.type = type
        self.color = color
        self.text = text

    def __repr__(self):
        return f"{self.id}, {self.long_name}, {self.type}"
    
# routes = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
#     route_id = line[0:indexList[0]]
#     agency_id = line[indexList[0]+1:indexList[1]]
#     route_short_name = line[indexList[1]+1:indexList[2]]
#     route_long_name = line[indexList[2]+1:indexList[3]]
#     route_desc = line[indexList[3]+1:indexList[4]]
#     route_type = line[indexList[4]+1:indexList[5]]
#     route_url = line[indexList[5]+1:indexList[6]]
#     route_color = line[indexList[6]+1:indexList[7]]
#     route_text_color = line[indexList[7]+1:]
#     obj = Routes(route_id, agency_id, route_short_name, route_long_name,
#                  route_desc, route_type, route_url, route_color, 
#                  route_text_color)
#     routes[route_id] = obj


def import_gtfs(path) -> Dict[str, Any]:  # See src/common/gtfs_agency.py for how this code works
    """
    Given a path to the "gtfs_static_feed" directory, this path will
    read in agency information and return it in a JSON-esque dictionary 
    """
    routes = {}
    text = utils.read_file(os.path.join(path, defs.GTFS_STATIC_ROUTES))
    for line in text.splitlines()[1:]:
        obj = Routes(*line.split(','))
        routes[obj.id] = obj
    return routes