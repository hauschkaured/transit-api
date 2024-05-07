from typing import Tuple
from .gtfs_static import gtfs_agency 
from .gtfs_static import gtfs_calendar_dates
from .gtfs_static import gtfs_calendar  
from .gtfs_static import gtfs_feed 
from .gtfs_static import gtfs_routes 
from .gtfs_static import gtfs_shapes 
from .gtfs_static import gtfs_stop_times 
from .gtfs_static import gtfs_stops 
from .gtfs_static import gtfs_transfers 
from .gtfs_static import gtfs_trips 

def read_file(path) -> str:
    """Reads full file and returns contents as a string"""
    with open(path, 'r') as f: return f.read()

def write_to_file(path: str, content: str) -> None:
    """Writes the content string to the specified path"""
    with open(path, 'w') as f: f.write(content)

def gen_static_structs(path) -> Tuple[gtfs_agency.Agency, gtfs_calendar_dates.Dates, 
                                      gtfs_calendar.Calendar, gtfs_feed.Feed, gtfs_routes.Routes, 
                                      gtfs_shapes.Shapes, gtfs_stop_times.Stoptimes, 
                                      gtfs_stops.Stops, gtfs_transfers.Transfer, gtfs_trips.Trips]:
    return gtfs_agency.import_gtfs(path), gtfs_calendar_dates.import_gtfs(path), \
            gtfs_calendar.import_gtfs(path), gtfs_feed.import_gtfs(path), gtfs_routes.import_gtfs(path), \
            gtfs_shapes.import_gtfs(path), gtfs_stop_times.import_gtfs(path), gtfs_stops.import_gtfs(path), \
            gtfs_transfers.import_gtfs(path), gtfs_trips.import_gtfs(path)