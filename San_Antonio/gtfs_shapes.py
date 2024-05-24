text = open("gtfs_static_feed/shapes.txt", "r")


class Shapes:
    def __init__(self, shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled):
        self.shape_id = shape_id
        self.shape_pt_lat = shape_pt_lat
        self.shape_pt_lon = shape_pt_lon
        self.shape_pt_sequence = shape_pt_sequence
        self.shape_dist_traveled = shape_dist_traveled

    def __repr__(self):
        return f'''{self.shape_id} {self.shape_pt_lat} {self.shape_pt_lon} 
        {self.shape_pt_sequence} {self.shape_dist_traveled}'''


via_shapes = {}

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
    via_shapes[lon] = obj