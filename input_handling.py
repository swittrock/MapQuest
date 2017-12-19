#Spencer Wittrock #84023369
from api_handling import *
from classes_and_output import *



def location_input():
    '''prompts the user for location input'''
    number_of_locations = int(input())
    location_list = []
    for x in range(number_of_locations):
        location_list.append(input())
    return(location_list)

def output_choice():
    '''prompts the user for number and type of outputs'''
    number_of_outputs = int(input())
    output_list = []
    for y in range(number_of_outputs):
        output_list.append(input())
    return(output_list)

if __name__ == '__main__':

    if generate_outputs(web_result(build_route_url(location_input())),assign_classes(output_choice())) == "MAPQUEST ERROR":
        print('MAPQUEST ERROR')
