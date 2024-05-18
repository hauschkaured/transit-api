text = open("Pittsburgh/gtfs_static_feed/agency.txt", "r")

class Agency:
    def __init__(self, id, name, url, timezone, lang, phone, fare_url):
        self.id = id
        self.name = name
        self.url = url
        self.timezone = timezone
        self.lang = lang
        self.phone = phone
        self.fare_url = fare_url

    def __repr__(self):
        return f"{self.name}"
    
prt_agency = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    
    # obj = Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang,
    #              agency_phone, 
    #             agency_fare_url)
    # agency[agency_id] = obj
