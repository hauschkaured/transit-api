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

queries = {"gettime", "getvehicles", "getroutes", "getdirections", "getstops",
            "getpatterns", "getpredictions", "getservicebulletins", "getlocales",
            "getrtpidatafeeds", "getdetours", "getagencies"}

print(queries)
x = input("What query did you want to analyze?: ")

getvehicles_params = {
    **BASE_PARAMS,
    "rt": "61C"
}

if x in queries:
    z = requests.get(API_URL + f"get{x}", params=getvehicles_params)
    a = z.json()
pprint(a)



