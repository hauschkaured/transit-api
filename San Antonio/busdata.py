class Busdata:
    def __init__(self, id, lat, lon, hdg=None, spd=None, status=None, 
                 stop=None, stopseq=None, start=None, route=None, trip=None):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.hdg = hdg
        self.spd = spd
        self.status = status
        self.stop = stop
        self.stopseq = stopseq
        self.start = start
        self.route = route
        self.trip = trip

    