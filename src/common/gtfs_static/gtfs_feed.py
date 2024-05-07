from typing import Dict, Any
from .. import utils
from .. import defs
import os

class Feed:
    def __init__(self, publisher, url, lang, start, end, version):
        self.publisher = publisher
        self.url = url
        self.lang = lang
        self.start = start
        self.end = end
        self.version = version

    def __repr__(self):
        return f'''PUB {self.publisher} URL {self.url} LANG {self.lang} \n
        ST {self.start} END {self.end} VER {self.version}'''
    

def import_gtfs(path) -> Dict[str, Any]:  # See src/common/gtfs_agency.py for how this code works
    """
    Given a path to the "gtfs_static_feed" directory, this path will
    read in feed information and return it in a JSON-esque dictionary 
    """
    feed = {}
    text = utils.read_file(os.path.join(path, defs.GTFS_STATIC_FEED_INFO))
    for line in text.splitlines()[1:]:
        obj = Feed(*line.split(','))
        feed[obj.publisher] = obj
    return feed



# feed = {}

# textdata = text.read()

# for line in textdata.splitlines():
#     indexList = []
#     for i in range(len(line)):
#         if line[i] == ',':
#             indexList.append(i)
#     publisher = line[0:indexList[0]]
#     url = line[indexList[0]+1:indexList[1]]
#     lang = line[indexList[1]+1:indexList[2]]
#     start = line[indexList[2]+1:indexList[3]]
#     end = line[indexList[3]+1:indexList[4]]
#     version = line[indexList[4]+1:]


#     obj = Feed(publisher, url, lang, start, end, version)
#     feed[id] = obj