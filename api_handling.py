#Spencer Wittrock #84023369
import urllib.request
import urllib.parse
import urllib.error
import json
import sys

key = 'QAJfK5wPLZWecLugWwxLTvk5NEwZoL9y'
BASE_MAPQUEST_URL = 'http://www.mapquestapi.com/directions/v2/route?'
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

def build_route_url(locations:list) -> str:
    '''Takes a list of locations and returns a valid URL for use on the mapquest API'''
    query_parameters =  [('key', key)]
    for x in range(len(locations)):
        if x == 0:
            query_parameters.append(('from', locations[0]))
        else:
            query_parameters.append(('to', locations[x]))
    return BASE_MAPQUEST_URL + urllib.parse.urlencode(query_parameters)

def get_latlng(route:dict):
    '''returns a list of tuples containing the lat and long of each location in the JSON response parameter'''
    coordinates = []
    for x in route['route']['locations']:
        coordinates.append(tuple((str((x['displayLatLng']['lat'])),(str(x['displayLatLng']['lng'])))))
    return coordinates

def build_elevation_url(coordinates:list):
    '''returns a list of the URLs containing the elevation of each location'''
    result_urls = []
    for x in coordinates:
        query_paramteres = [('key',key),('latLngCollection', (x[0]+','+x[1]))]
        result_urls.append(BASE_ELEVATION_URL + urllib.parse.urlencode(query_paramteres))
    return result_urls

def web_result(url:str):
    '''Given a valid URL, returns a JSON response converted to a list of dictionaries'''
    web_location = None
    try:
        web_location = urllib.request.urlopen(url)
        data = web_location.read()
        string_data = data.decode(encoding= 'utf-8')
        return json.loads(string_data)
    except urllib.error.URLError:
        print()
        print('MAPQUEST ERROR')
        sys.exit(0)
    finally:
        if web_location != None:
            web_location.close()