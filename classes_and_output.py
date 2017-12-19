#Spencer Wittrock #84023369
import api_handling

class steps:
    def output(self, location:dict):
        '''prints the step by stp directions'''
        location_steps = location['route']['legs']
        print()
        print('DIRECTIONS', '\n')
        for term in location_steps:
            for choice in term['maneuvers']:
                print(choice['narrative'])
        return "\n"

class distance:
    def output(self, location:dict):
        '''prints total distance'''
        print()
        print('TOTAL DISTANCE: {:.0f} MILES'.format(location['route']['distance']))
        return('\n')

class time:
    def output(self, location:dict):
        '''prints total amount of minutes'''
        print()
        print('TOTAL TIME: {:.0f} MINUTES'.format(int((location['route']['realTime']) / 60)))
        return('\n')

class elevation:
    def output(self, location:dict):
        '''returns all elevations of the trip'''
        print('ELEVATIONS:')
        for x in api_handling.build_elevation_url(api_handling.get_latlng(location)):
            for y in api_handling.web_result(x)['elevationProfile']:
                print(y['height'],'METERS')
        return('\n')

class lat_and_long:
    def output(self, location:dict):
        '''returns the lat on long of each location'''
        print('LATTITUDE AND LONGITUDE')
        for x in location['route']['locations']:
            if float(x['displayLatLng']['lat']) > 0:
                lat_direction = "N"
            else:
                lat_direction = "S"

            if float(x['displayLatLng']['lng']) > 0:
                long_direction = "E"
            else:
                long_direction = "W"
            print('{:12} Latitude: {:.5f} {}  Longitude: {:.5f} {}'.format(x['adminArea5'], float(x['displayLatLng']['lat']), lat_direction,float(x['displayLatLng']['lng']),long_direction))
        return('\n')

def assign_classes(user_outputs:list):
    '''checks to see which type of output should be assigned to each user entered input'''
    new_output_list = []
    for output in user_outputs:
        if output == 'STEPS':
            new_output_list.append(steps)
        elif output == 'TOTALDISTANCE':
            new_output_list.append(distance)
        elif output == 'TOTALTIME':
            new_output_list.append(time)
        elif output == 'LATLONG':
            new_output_list.append(lat_and_long)
        elif output == 'ELEVATION':
            new_output_list.append(elevation)
    return new_output_list

def generate_outputs(location_info:dict, class_list:list):
    '''makes each item in the list of outputs generate its inteded output'''
    try:
        for x in class_list:
            print(x.output(x,location_info))
    except:
        print()
        print('NO ROUTE FOUND')
        return "NO ROUTE FOUND"



