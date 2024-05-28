class Dates:
    def __init__(self, service_id, date, exception_type):
        self.service_id = service_id
        self.date = date
        self.exception_type = exception_type

    def __repr__(self):
        return f"{self.service_id} {self.date} {self.exception_type}"
    
calendar_dates = dict()

def cal_dates(foo):
    print(foo)
    if foo == "pgh":
        text = open("static/pittsburgh/calendar_dates.txt", "r")
        text_reading(text)
    elif foo == "satx":
        text = open("static/san_antonio/calendar_dates.txt", "r")
        text_reading(text)

def text_reading(text):
    textdata = text.read()
    for line in textdata.splitlines():
        items = line.split(',')
        itemList = []
        for i in items:
            itemList.append(i)

        service_id = itemList[0]
        date = itemList[1]
        exception_type = itemList[2]

        object = Dates(service_id, date, exception_type)
        calendar_dates[service_id] = object
    print(calendar_dates)
    return calendar_dates