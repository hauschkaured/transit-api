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

vehicle_params = {
    **BASE_PARAMS
}

def timeFormat(x):
    string = x[0:4] + '-' + x[4:6] + '-' + x[6:8] + ' AT' + x[8:]
    return string

def timeCall():
    time = requests.get(API_URL + "gettime", params=time_params)
    timedata = time.json()
    datatime = timedata["bustime-response"]["tm"]
    currentTime = timeFormat(datatime)
    return currentTime

def busCall():
    buses = requests.get(API_URL + "getvehicles", params=vehicle_params)
    bustime = buses.json()
    if "vehicle" in bustime["bustime-response"]:
        data = bustime["bustime-response"]["vehicle"]
        return data
    return 0

def routeCall():
    predictions = requests.get(API_URL + "getpredictions", params=prediction_params)
    bustime = predictions.json()
    data = bustime["bustime-response"]["prd"]
    return data

def oneStop():
    time = timeCall()
    data = routeCall()
    print(f"IT'S {time}")
    print(f"YOUR STOP ID'S #{prediction_params['stpid']}")
    for i in range(len(data)):
        if data[i]["prdctdn"] == "DUE":
            print(f"{data[i]["rt"]} BUS {data[i]["vid"]} IS DUE")
        else:
            print(f"{data[i]["rt"]} BUS {data[i]["vid"]} ARRIVES IN {data[i]["prdctdn"]} MINUTES")

def multiStops():
    time = timeCall()
    data = routeCall()
    print(f"IT'S {time}")
    print(f"YOUR STOP IDS ARE #{prediction_params['stpid']}")
    for i in range(len(data)):
        if data[i]["prdctdn"] == "DUE":
            print(f"(#{data[i]["stpid"]}) {data[i]["rt"]} {data[i]["vid"]} IS DUE")
        else:
            print(f"(#{data[i]["stpid"]}) BUS {data[i]["vid"]} ARRIVES IN {data[i]["prdctdn"]} MINUTES")

def oneRoute():
    time = timeCall()
    data = busCall()
    print(f"IT'S {time}")
    print(f"YOUR SELECTED ROUTE IS {vehicle_params['rt']}")
    for i in range(len(data)):
        print(f"{data[i]["vid"]} TO {data[i]["des"]}")

def multiRoute():
    time = timeCall()
    data = busCall()
    print(f"IT'S {time}")
    print(f"YOUR SELECTED ROUTES ARE {vehicle_params['rt']}")
    for i in range(len(data)):
        print(f"ROUTE {data[i]["rt"]} {data[i]["vid"]} TO {data[i]["des"]}")

def oneBus():
    time = timeCall()
    data = busCall()
    print(f"IT'S {time}")
    print(f"YOUR SELECTED BUS IS {vehicle_params['vid']}")
    if data == 0:
        print("THIS BUS IS NOT RUNNING RIGHT NOW.")
    else:
        print(f"ROUTE {data[0]["rt"]} {data[0]["vid"]} TO {data[0]["des"]}")

def multiBus():
    time = timeCall()
    data = busCall()
    print(f"IT'S {time}")
    print(f"YOUR SELECTED BUSES ARE {vehicle_params['vid']}")
    if data == 0:
        print("NONE OF THESE BUSES ARE RUNNING RIGHT NOW.")
    else:
        print("THE FOLLOWING BUSES ARE RUNNING")
        for i in range(len(data)):
            print(f"ROUTE {data[i]["rt"]} {data[i]["vid"]} TO {data[i]["des"]}")

x = input('Enter your desired operation: ')

if x == '':
    prediction_params['stpid'] = '18179'  
    oneStop()
elif x == "stop":
    y = input("Enter the stop #(s) here: ")
    prediction_params['stpid'] = f'{y}'
    if y.count(',') == 0:
        oneStop() 
    else:
        multiStops()
elif x == "route":
    y = input()
    vehicle_params['rt'] = f'{y}'
    if y.count(',') == 0:
        oneRoute()
    else:
        multiRoute()
elif x == "foamer":
    y = input()
    vehicle_params['vid'] = f'{y}'
    if y.count(',') == 0:
        oneBus()
    else:
        multiBus()










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
