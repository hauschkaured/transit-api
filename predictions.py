## Preamble 

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
    'rtpidatafeed': 'Port Authority Bus',
}

prediction_params = {
    **BASE_PARAMS
    }  

time_params = {
    **BASE_PARAMS,
    'unixTime': 0
}

def oneStop():
    time = requests.get(API_URL + "gettime", params=time_params)
    predictions = requests.get(API_URL + "getpredictions", params=prediction_params)
    bustime = predictions.json()
    data = bustime["bustime-response"]["prd"]
    timedata = time.json()
    datatime = timedata["bustime-response"]["tm"]
    currentTime = timeFormat(datatime)
    print(f"IT'S {currentTime}")
    print(f"YOUR STOP ID'S #{prediction_params['stpid']}")
    for i in range(len(data)):
        if data[i]["prdctdn"] == "DUE":
            print(f"{data[i]["rt"]} BUS {data[i]["vid"]} IS DUE")
        else:
            print(f"{data[i]["rt"]} BUS {data[i]["vid"]} ARRIVES IN {data[i]["prdctdn"]} MINUTES")

def multiStops():
    time = requests.get(API_URL + "gettime", params=time_params)
    predictions = requests.get(API_URL + "getpredictions", params=prediction_params)
    bustime = predictions.json()
    data = bustime["bustime-response"]["prd"]
    timedata = time.json()
    datatime = timedata["bustime-response"]["tm"]
    currentTime = timeFormat(datatime)
    print(f"IT'S {currentTime}")
    print(f"YOUR STOP IDS ARE #{prediction_params['stpid']}")
    for i in range(len(data)):
        if data[i]["prdctdn"] == "DUE":
            print(f"(#{data[i]["stpid"]}) {data[i]["rt"]} {data[i]["vid"]} IS DUE")
        else:
            print(f"(#{data[i]["stpid"]}) BUS {data[i]["vid"]} ARRIVES IN {data[i]["prdctdn"]} MINUTES")

def timeFormat(x):
    string = x[0:4] + '-' + x[4:6] + '-' + x[6:8] + ' AT' + x[8:]
    print(string)
    return string

x = input('Enter your desired operation: ')

if x == '':
    prediction_params['stpid'] = '18179'  
elif x == "stop":
    y = input("Enter the stop #(s) here: ")
    prediction_params['stpid'] = f'{y}'
    if y.count(',') == 0:
        oneStop() 
    else:
        multiStops()
elif x == "route":
    y = input()
    prediction_params['rt'] = f'{y}'









# getvehicles
vehicle_params = {
    **BASE_PARAMS,
    # 'vid':'7001,7002,7101,7102,7103,7104,7105,7106,3501', # COMMNENT OPTION
    # 'rt':'28X',
    # 'tmres':'s' # OPTIONAL
}

# getdirections
direction_params = {
    **BASE_PARAMS,
    'rt': '93'
}

# getstops
stops_params = {
    **BASE_PARAMS,
    # 'rt':
    # 'dir':
    'stpid': '18179'
}

# getpatterns
pattern_params = {
    **BASE_PARAMS,
    # 'pid':
    'rt':'61D'
}

# getpredictions
prediction_params = {
    **BASE_PARAMS,
    'stpid': '18179'
    # 'rt':
    # 'vid':
    # 'top':
    # 'tmres':
    # 'unixTime':
}

# getbulletins
bulletin_params = {
    **BASE_PARAMS,
    # 'rt':
    # 'rtdir':
    'stpid': '4407'
}

# getlocales
locale_params = {
    **BASE_PARAMS,
    # 'locale':
    # 'inLocaleLanguage':
}

# getdetours
detour_params = {
    **BASE_PARAMS,
     'rt': 'P1'
    # 'rtdir':
    # 'rtpidatafeed':
}

# vehicle = requests.get(API_URL + "getvehicles", params=vehicle_params)
# direction = requests.get(API_URL + "getdirections", params=direction_params)
# stops = requests.get(API_URL + "getstops", params=stops_params)
# patterns = requests.get(API_URL + "getpatterns", params=pattern_params) 
# bulletins = requests.get(API_URL + "getservicebulletins", params=bulletin_params)
# locales = requests.get(API_URL + "getlocalelist", params=locale_params)
# rtpidatafeeds = requests.get(API_URL + "getrtpidatafeeds", params=BASE_PARAMS)
# detours = requests.get(API_URL + "getdetours", params=detour_params))




# busNumberList = []
# for i in range(len(data)):
#     busNumberList.append(data[i]["vid"])

# print(busNumberList)

# for i in busNumberList:
#     vehicle_params = {
#         **BASE_PARAMS,
#         'vid':f'{i}'
#     }
#     vehicle = requests.get(API_URL + "getvehicles", params=vehicle_params)
#     print((vehicle.json()))
#     print(vehicle.json()["bustime-response"])
#     thing = vehicle.json()["bustime-response"]
#     print(thing['vehicle'])
#     thing2 = thing['vehicle']
#     pprint(thing2)

# for i in range(len(data)):
#     print(f"{data[i]["rtdir"]} {data[i]["rt"]} BUS #{data[i]["vid"]} TO {data[i]["des"]} ARRIVES IN {data[i]["prdctdn"]} MINUTES")
