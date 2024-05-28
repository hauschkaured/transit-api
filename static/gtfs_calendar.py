class Calendar:
    def __init__(self, service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date):
        self.service_id = service_id
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"""{self.service_id} {self.monday} {self.tuesday} {self.wednesday} {self.thursday} {self.friday}
        {self.friday} {self.saturday} {self.sunday} {self.start_date} {self.end_date}"""


calendar = dict()


def cal_dates(foo):
    print(foo)
    if foo == "pgh":
        text = open("static/pittsburgh/calendar.txt", "r")
        text_reading(text)
    elif foo == "satx":
        text = open("static/san_antonio/calendar.txt", "r")
        text_reading(text)


def text_reading(text):
    textdata = text.read()
    for line in textdata.splitlines():
        items = line.split(',')
        itemList = []
        for i in items:
            itemList.append(i)

        service_id = itemList[0]
        monday = itemList[1]
        tuesday = itemList[2]


        object = Calendar(service_id, monday, tuesday,)
        calendar[service_id] = object
    print(calendar)
    return calendar