import requests     
from key import PRT_KEY 
from datetime import datetime
import pprint as PP
pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

x = input("What query did you want to make?: ")

API_URL = "https://truetime.portauthority.org/bustime/api/v3/"
BASE_PARAMS = {
    'key': PRT_KEY, 
    'format': 'json',
}

parameters = {
    **BASE_PARAMS
}

output = requests.get(f"{API_URL} + {x}", params=parameters)
