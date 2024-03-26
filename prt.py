import requests

# Outputs of the API are either in XML or JSON. 

response = requests.get("http://truetime.portauthority.org/bustime/api/v3/getvehicles?key=yT2htEkvExjjJnKfD22dY6dTT&rt=61C,61D&format=json")
print(response.status_code)

result = response.json()

print(result)
