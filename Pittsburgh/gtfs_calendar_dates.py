text = open("gtfs_static_feed/calendar_dates.txt", "r")

class Dates:
    def __init__(self, id, date, type):
        self.id = id
        self.date = date
        self.type = type

    def __repr__(self):
        return f"ID={self.id} DATE={self.date} TYPE={self.type}\n"
    
calendar_dates = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    id = line[0:indexList[0]]
    date = line[indexList[0]+1:indexList[1]]
    type = line[indexList[1]+1:]

    obj = Dates(id, date, type)
    calendar_dates[id] = obj