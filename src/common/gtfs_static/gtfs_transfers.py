from typing import Dict, Any
from .. import utils
from .. import defs
import os

class Transfer:
    def __init__(self, from_id, to_id, transfer_type, min_time):
        self.from_id = from_id
        self.to_id = to_id
        self.transfer_type = transfer_type
        self.min_time = min_time

    def __repr__(self):
        return f"{self.from_id}, {self.to_id}"


def import_gtfs(path) -> Dict[str, Any]:  # See src/common/gtfs_agency.py for how this code works
    """
    Given a path to the "gtfs_static_feed" directory, this path will
    read in agency information and return it in a JSON-esque dictionary 
    """
    transfers = {}
    text = utils.read_file(os.path.join(path, defs.GTFS_STATIC_TRANSFERS))
    for line in text.splitlines()[1:]:
        obj = Transfer(*line.split(','))
        transfers[obj.from_id] = obj
    return transfers

# transfers = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
#     from_id = line[0:indexList[0]]
#     to_id = line[indexList[0]+1:indexList[1]]
#     transfer_type = line[indexList[1]+1:indexList[2]]
#     min_time = line[indexList[2]+1:]
#     obj = Transfer(from_id, to_id, transfer_type, min_time)
#     transfers[from_id] = obj

