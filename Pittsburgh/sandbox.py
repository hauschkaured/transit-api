import requests     
from key import PRT_KEY 
from datetime import datetime
import pprint as PP
pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

API_URL = "https://truetime.portauthority.org/bustime/api/v3/"
BASE_PARAMS = {
    'key': PRT_KEY, 
    'format': 'json',
}

x = input("What query did you want to analyze?: ")

queries = {"gettime", "getvehicles", "getroutes", "getdirections", "getstops",
            "getpatterns", "getpredictions", "getservicebulletins", "getlocales",
            "getrtpidatafeeds", "getdetours", "getagencies"}
print(queries)

if x in queries:
    z = requests.get(f"{API_URL} + {x}, params=BASE_PARAMS")
    object = z.json()

pprint(object)



