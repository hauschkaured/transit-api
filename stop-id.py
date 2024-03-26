import requests
import json

response = requests.get("""http://truetime.portauthority.org/bustime/api/v3/getstops?key=yT2htEkvExjjJnKfD22dY6dTT&stpid="18179"&format=json""")
result = response.json()

print(result)