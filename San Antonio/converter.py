output_path="./stops.py"
text = open("gtfs_static_feed/stops.txt", "r")
import pprint as PP
import json

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint
stopNames = {}

textdata = text.read()
for line in textdata.splitlines():
    index = line.find(',')
    lineNew = line[index+1:]
    indexTwo = lineNew.find(',')
    lineNewTwo = lineNew[indexTwo+1:]
    indexThree = lineNewTwo.find(',')
    lineNewThree = lineNewTwo[indexThree+1:]
    indexFour = lineNewThree.find(',')
    stopName = lineNewTwo[:indexThree]
    stopNumber = line[:index]
    stopNames[stopNumber] = stopName
    print(stopName, stopNumber)

json = json.dumps(stopNames)
new = json.replace(',',',\n')
print(new)
with open(output_path, 'w') as f:
    f.write(new)
# write_to_file(output_path, data)
