from common import utils, defs
from pittsburgh import fetcher
import os


agency, dates, calendar, feed, routes, shapes, times, stops, transfers, trips = \
    utils.gen_static_structs(defs.PITTSBURGH_GTFS)

busloc, bustrip, trainloc, traintrip = fetcher.fetch()




