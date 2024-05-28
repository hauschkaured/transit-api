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
        item_list = []
        for i in items:
            item_list.append(i)

        service_id = item_list[0]
        date = item_list[1]
        exception_type = item_list[2]

        obj = Dates(service_id, date, exception_type)
        calendar_dates[service_id] = obj
    print(calendar_dates)
    return calendar_dates
