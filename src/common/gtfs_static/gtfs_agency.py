from typing import Dict, Any
from .. import utils
from .. import defs
import os

class Agency:
    def __init__(self, id, name, url, timezone, lang, phone, fare_url):
        self.id = id
        self.name = name
        self.url = url
        self.timezone = timezone
        self.lang = lang
        self.phone = phone
        self.fare_url = fare_url

    def __repr__(self):
        return f"{self.name}"
    
# agency = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
    
    # obj = Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang,
    #              agency_phone, 
    #             agency_fare_url)
    # agency[agency_id] = obj

def import_gtfs(path) -> Dict[str, Any]:
    """
    Given a path to the "gtfs_static_feed" directory, this path will
    read in agency information and return it in a JSON-esque dictionary 
    """

    # Initialize blank dict to store all agencies
    agency = {}

    # Read full text file, since the path param is to the directory, we use defs to get the full file path
    text: str = utils.read_file(os.path.join(path, defs.GTFS_STATIC_AGENCY)).strip()

    # Each line in GTFS static data feeds is a new entry, splitting by lines
    for line in text.splitlines()[1:]:  # Indexing [1:] because the 0th entry is just stating what the cols are
        obj = Agency(*line.split(','))  # All GTFS data is CSV, split with comma and unpack contents into constructor
        agency[obj.id] = obj  # Creating new mapping in dict, agency_id : Agency (obj)
    
    return agency

# print(agency)

## FIX THIS FILE ##