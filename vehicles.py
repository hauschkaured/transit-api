import requests
import json

# Outputs of the API are either in XML or JSON. 

response = requests.get("""http://truetime.portauthority.org/bustime/api/v3/
                        getvehicles?key=yT2htEkvExjjJnKfD22dY6dTT
                        &rt=61A,61B,61C,61D&format=json""")
print(response.status_code)

result = response.json()

# We want to remove all error messages yielded to give us accurate tracking data
# For bus number search only.
# del result["bustime-response"]["error"]  

print(type(result["bustime-response"]["vehicle"]) == list)
busList = result["bustime-response"]["vehicle"]
for i in range(len(busList)):
    route = busList[i]["rt"]
    destination = busList[i]["des"]
    bus = busList[i]["vid"]
    print(f"{route} bus number {bus} to {destination}")

resultClean = json.dumps(result, sort_keys=True, indent=4)
print(resultClean)


    