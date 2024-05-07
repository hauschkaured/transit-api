from common import utils, defs
from pittsburgh import fetcher
import os


agency, dates, calendar, feed, routes, shapes, times, stops, transfers, trips = \
    utils.gen_static_structs(os.path.join(defs.SRC_ROOT, defs.PITTSBURGH_DIR, "gtfs_static_feed"))

busloc, bustrip, trainloc, traintrip = fetcher.fetch()




