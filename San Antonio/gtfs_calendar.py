text = open("gtfs_static_feed/calendar.txt", "r")

class Calendar:
    def __init__(self, id, mon, tue, wed, thu, fri, sat, sun, start, end):
        self.id = id
        self.mon = mon
        self.tue = tue
        self.wed = wed
        self.thu = thu
        self.fri = fri
        self.sat = sat
        self.sun = sun
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.id}"
    
gtfscalendar = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    id = line[0:indexList[0]]
    mon = line[indexList[0]+1:indexList[1]]
    tue= line[indexList[1]+1:indexList[2]]
    wed = line[indexList[2]+1:indexList[3]]
    thu = line[indexList[3]+1:indexList[4]]
    fri = line[indexList[4]+1:indexList[5]]
    sat = line[indexList[5]+1:indexList[6]]
    sun = line[indexList[6]+1:indexList[7]]
    start = line[indexList[7]+1:indexList[8]]
    end = line[indexList[8]+1:]
    obj = Calendar(id, mon, tue, wed, thu, fri, sat, sun, start, end)
    gtfscalendar[id] = obj