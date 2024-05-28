class Agency:
    def __init__(self, agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone, agency_fare_url):
        self.agency_id = agency_id
        self.agency_name = agency_name
        self.agency_url = agency_url
        self.agency_timezone = agency_timezone
        self.agency_lang = agency_lang
        self.agency_phone = agency_phone
        self.agency_fare_url = agency_fare_url

    def __repr__(self):
        return f"""{self.agency_id} {self.agency_name} {self.agency_url}
        {self.agency_timezone} {self.agency_lang} {self.agency_phone} {self.agency_fare_url}"""


def agency(foo):
    print(foo)
    if foo == "pgh":
        text = open("static/pittsburgh/agency.txt", "r")
        text_reading(text)
    elif foo == "satx":
        text = open("static/san_antonio/agency.txt", "r")
        text_reading(text)


def text_reading(text):
    textdata = text.read()
    data = textdata.splitlines()
    info = data[1]
    info_list = info.split(',')
    
    agency_id = info_list[0]
    agency_name = info_list[1]
    agency_url = info_list[2]
    agency_timezone = info_list[3]
    agency_lang = info_list[4]
    agency_phone = info_list[5]
    agency_fare_url = info_list[6]

    obj = Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang,
                 agency_phone, agency_fare_url)
    print(obj)
    return obj
