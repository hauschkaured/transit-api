text = open("Pittsburgh/gtfs_static_feed/shapes.txt", "r")


class Shapes:
    def __init__(self, id, lat, lon, sequence, dist_traveled): 
        self.id = id
        self.lat = lat
        self.lon = lon
        self.sequence = sequence
        self.dist_traveled = dist_traveled

        
    def __repr__(self):
        return(f'''{self.id}, {self.lat}, {self.lon}''')

    
prt_shapes = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    id = line[0:indexList[0]]
    lat = line[indexList[0]+1:indexList[1]]
    lon = line[indexList[1]+1:indexList[2]]
    sequence = line[indexList[2]+1:indexList[3]]
    dist_traveled = line[indexList[3]+1:]
    obj = Shapes(id, lat, lon, sequence, dist_traveled)
    prt_shapes[lon] = obj