from typing import Dict, Any
from .. import utils
from .. import defs
import os

class Dates:
    def __init__(self, id, date, type):
        self.id = id
        self.date = date
        self.type = type

    def __repr__(self):
        return f"ID={self.id} DATE={self.date} TYPE={self.type}\n"
    

def import_gtfs(path) -> Dict[str, Any]:  # See src/common/gtfs_agency.py for how this code works
    """
    Given a path to the "gtfs_static_feed" directory, this path will
    read in calendar dates information and return it in a JSON-esque dictionary 
    """
    dates = {}
    text = utils.read_file(os.path.join(path, defs.GTFS_STATIC_CALENDAR_DATES))
    for line in text.splitlines()[1:]:
        obj = Dates(*line.split(','))
        dates[obj.id] = obj
    return dates


# calendar_dates = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
#     id = line[0:indexList[0]]
#     date = line[indexList[0]+1:indexList[1]]
#     type = line[indexList[1]+1:]

#     obj = Dates(id, date, type)
#     calendar_dates[id] = obj
