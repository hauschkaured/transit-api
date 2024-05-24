text = open("gtfs_static_feed/calendar_dates.txt", "r")

class Dates:
    def __init__(self, service_id, date, exception_type):
        self.service_id = service_id
        self.date = date
        self.exception_type = exception_type

    def __repr__(self):
        return f"{self.service_id} {self.date} {self.exception_type}"


via_calendar_dates = {}

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
    via_calendar_dates[id] = obj