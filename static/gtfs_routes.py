class Routes:
    def __init__(self, route_id, agency_id, route_short_name, route_long_name, route_desc, route_type, route_url,
                 route_color, route_text_color):
        self.route_id = route_id
        self.agency_id = agency_id
        self.route_short_name = route_short_name
        self.route_long_name = route_long_name
        self.route_desc = route_desc
        self.route_type = route_type
        self.route_url = route_url
        self.route_color = route_color
        self.route_text_color = route_text_color

    def __repr__(self):
        return f'''{self.route_id} {self.agency_id} {self.route_short_name} {self.route_long_name}
        {self.route_desc} {self.route_type} {self.route_url} {self.route_color} {self.route_text_color}'''

    
prt_routes = {}

textdata = text.read()

for line in textdata.splitlines():
    indexList = []
    for i in range(len(line)):
        if line[i] == ',':
            indexList.append(i)
    route_id = line[0:indexList[0]]
    agency_id = line[indexList[0]+1:indexList[1]]
    route_short_name = line[indexList[1]+1:indexList[2]]
    route_long_name = line[indexList[2]+1:indexList[3]]
    route_desc = line[indexList[3]+1:indexList[4]]
    route_type = line[indexList[4]+1:indexList[5]]
    route_url = line[indexList[5]+1:indexList[6]]
    route_color = line[indexList[6]+1:indexList[7]]
    route_text_color = line[indexList[7]+1:]
    obj = Routes(route_id, agency_id, route_short_name, route_long_name,
                 route_desc, route_type, route_url, route_color, 
                 route_text_color)
    prt_routes[route_id] = obj