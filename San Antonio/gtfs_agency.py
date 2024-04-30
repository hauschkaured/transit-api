text = open("gtfs_static_feed/agency.txt", "r")

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
    
agency = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    agency_id = line[0:indexList[0]]
    agency_name = line[indexList[0]+1:indexList[1]]
    agency_url = line[indexList[1]+1:indexList[2]]
    agency_timezone = line[indexList[2]+1:indexList[3]]
    agency_lang = line[indexList[3]+1:indexList[4]]
    agency_phone = line[indexList[4]+1:indexList[5]]
    agency_fare_url = line[indexList[5]+1:]
    obj = Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang,
                 agency_phone, 
                agency_fare_url)
    agency[agency_id] = obj