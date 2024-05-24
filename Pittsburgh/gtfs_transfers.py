text = open("Pittsburgh/gtfs_static_feed/transfers.txt", "r")


class Transfer:
    def __init__(self, from_stop_id, to_stop_id, from_route_id, to_route_id, from_trip_id, to_trip_id,
                 transfer_type, min_transfer_time):
        self.from_stop_id = from_stop_id
        self.to_stop_id = to_stop_id
        self.from_route_id = from_route_id
        self.to_route_id = to_route_id
        self.from_trip_id = from_trip_id
        self.to_trip_id = to_trip_id
        self.transfer_type = transfer_type
        self.min_transfer_time = min_transfer_time

    def __repr__(self):
        return f'''{self.from_stop_id} {self.to_stop_id} {self.from_route_id} {self.to_route_id}
        {self.from_trip_id} {self.to_trip_id} {self.transfer_type} {self.min_transfer_time}'''


prt_transfers = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    from_id = line[0:indexList[0]]
    to_id = line[indexList[0]+1:indexList[1]]
    transfer_type = line[indexList[1]+1:indexList[2]]
    min_time = line[indexList[2]+1:]
    obj = Transfer(from_id, to_id, None, None, None, None,
                   transfer_type, min_time)
    prt_transfers[from_id] = obj

