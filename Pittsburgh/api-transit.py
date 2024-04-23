import requests # API requests made with this.
from key import PRT_KEY # Our API key is imported from the file key.py
import pprint as PP # Printing JSON with this. 
from datetime import datetime
from google.protobuf.json_format import MessageToJson
import json 

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

buses = requests.get("https://truetime.portauthority.org/gtfsrt-bus/vehicles")
# busdata = buses.text
# print(type(busdata))

# busdatajson = json.loads(busdata)
# bustrip = requests.get("https://truetime.portauthority.org/gtfsrt-bus/trips?debug")
# bustripdata = bustrip.text

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
    **BASE_PARAMS,
    # 'vid':'7001,7002,7101,7102,7103,7104,7105,7106,3501', # COMMNENT OPTION
    # 'rt':'28X',
    # 'tmres':'s' # OPTIONAL
}

def seriesPicker(x):    
    buses = {
        '1700':'2015 Gillig Low Floor 35 Foot',
        '3200':'2011 New Flyer D60LFR',
        '3300':'2013 New Flyer D60LFR',
        '3400':'2017 New Flyer XD60',
        '3500':'2024 New Flyer XD60',
        '5800':'2011 Gillig Low Floor',
        '5900':'2012 Gillig Low Floor',
        '6000':'2014 Gillig Low Floor',
        '6100':'2015 Gillig Low Floor',
        '6200':'2016 Gillig Low Floor',
        '6300':'2017 Gillig Low Floor',
        '6400':'2018 Gillig Low Floor',
        '6500':'2019 Gillig Low Floor',
        '6600':'2020 Gillig Low Floor',
        '6700':'2021 Gillig Low Floor',
        '7000':'2020 New Flyer XE40',
        '7100':'2021 New Flyer XE40'
    }
    if x in buses:
        pass

def timeFormat(x):
    string = x[0:4] + '-' + x[4:6] + '-' + x[6:8] + ' at' + x[8:]
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
    print(f"It's {time}")
    print(f"Your stop ID is #{prediction_params['stpid']}")
    for i in range(len(data)):
        if data[i]["prdctdn"] == "DUE":
            print(f"{data[i]['rt']} bus {data[i]['vid']} is due.")
        else:
            print(f"{data[i]['rt']} bus {data[i]['vid']} arrives in {data[i]['prdctdn']} minutes.")

def multiStops():
    time = timeCall()
    data = routeCall()
    print(f"It is {time}")
    print(f"Your stop IDs are #{prediction_params['stpid']}")
    for i in range(len(data)):
        if data[i]["prdctdn"] == "DUE":
            print(f"(#{data[i]['stpid']}) {data[i]['rt']} {data[i]['vid']} is due")
        else:
            print(f"(#{data[i]['stpid']}) bus {data[i]['vid']} arrives in {data[i]['prdctdn']} minutesb")

def oneRoute():
    time = timeCall()
    data = busCall()
    print(f"It's {time}")
    print(f"Your selected route is {vehicle_params['rt']}")
    for i in range(len(data)):
        print(f"{data[i]['vid']} to {data[i]['des']}")

def multiRoute():
    time = timeCall()
    data = busCall()
    print(f"It's {time}")
    print(f"Your selected routes are {vehicle_params['rt']}")
    for i in range(len(data)):
        print(f"Route {data[i]['rt']} {data[i]['vid']} to {data[i]['des']}")

def oneBus():
    time = timeCall()
    data = busCall()
    print(f"It's {time}")
    print(f"Your selected bus is {vehicle_params['vid']}")
    if data == 0:
        print("This bus is not running right now.")
    else:
        print(f"Route {data[0]['rt']} {data[0]['vid']} to {data[0]['des']}")

def multiBus():
    time = timeCall()
    data = busCall()
    print(f"It's {time}")
    print(f"Your selected buses are {vehicle_params['vid']}")
    if data == 0:
        print("None of these buses are running right now.")
    else:
        print("The following buses are running:")
        for i in range(len(data)):
            print(f"Route {data[i]['rt']} {data[i]['vid']} to {data[i]['des']}")

print("Welcome to TransitFoamer!")

print("This is version 0.4.")

print("There are three modes: stop, route, and foamer.")

x = input("Input your selection: ")

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
    y = input("Enter the route #(s) here: ")
    vehicle_params['rt'] = f'{y}'
    if y.count(',') == 0:
        oneRoute()
    else:
        multiRoute()
elif x == "foamer":
    a = input('Series or model? Enter your selection: ')
    if a == "series":
        print("What series do you want to track?")
        print("3200, 3300, 3400, 3500, 5800, 5900, 6000, 6100, 6200")
        print("6300, 6400, 6500, 6600, 6700, 7000, 7100")
        b = input('What series would you like? Enter your selection: ')
        seriesPicker(b)

    elif a == "model":
        y = input("Enter the bus unit #(s) here: ")
        vehicle_params['vid'] = f'{y}'
        if y.count(',') == 0:
            oneBus()
        else:
            multiBus()
else:
    print("Sorry, this selection is not valid.")
    print("Please try running the program again.")

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
