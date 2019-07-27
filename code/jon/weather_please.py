import forecastio
import requests
from datetime import datetime
import os

"""
    - Still need to work on geocoding zipcode to lat/long
    - Still need to work on argparse to include zipcode as an argument when     starting program.
    - Still need to implement an email function:
        - needs to take results of display() and save it into a file
        - take that file and email it to me
"""

def get_lanlon(zipcode):
    map_api = 'VhicHGxyitNwdtTPZFczl8z9TeeM0voN'
    map_url = 'http://www.mapquestapi.com/geocoding/v1/address?key=' + map_api + '&location=' + zipcode

    map_res = requests.get(map_url)
    map_data = map_res.json()
    # map_data_wanted = map_data['results'][0]['locations'][0]['latLng']
    map_latitude = map_data['results'][0]['locations'][0]['latLng']['lat']
    map_longitude = map_data['results'][0]['locations'][0]['latLng']['lng']
    # print(map_data_wanted)
    return map_latitude, map_longitude

def weather(lat, lng):
    api_key = "5f96bbce0e67b37965b9ef3af8b32ceb"
    print(f'Latitude: {lat}')
    print(f'Longitude: {lng}')
    forecast = forecastio.load_forecast(api_key, lat, lng, units='us')
    
    data = forecast.json
    
    wanted_data = [data['currently']['summary'], data['currently']['temperature'], data['currently']['apparentTemperature'], data['daily']['summary']]
    
    # print(f'from dictionary: {wanted_data}')
    return wanted_data

def display(info):
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    weather = info[1]
    current_temp = info[2]
    feels_temp = info[3]
    weather_summary = info[4]

    print(f'Currently at {current_time} the weather is {weather}.')  
    print(f'Your weather summary for the week is: {weather_summary}.')
    print(f'The current temperature is {current_temp} degrees F but feels more like {feels_temp} degrees F.')

def refresh_screen():
    os.system('clear')

def header():
    print('\n***********************************************************')
    print('***********************************************************')
    print('**                                                       **')
    print('**      ****     **     ****      ****       ****        **')
    print('**      ****    ****    ****      *****     *****        **')
    print('**       ****  ******  *****       *****   *****         **')
    print('**        *****************         ***** *****          **')
    print('**         *****     *****           **** ****           **')
    print('**          ****      ****          ****   ****          **')
    print('**           ***      ***          ****      ***         **')
    print('**            **      **          ****        ****       **')
    print('**             *      *          *****        *****      **')
    print('***********************************************************')
    print('***********************************************************\n')


name = input('What is your first name? ')
refresh_screen()
print (f'\nWelcome, {name}, to........\n')
header()

# display(weather(lat, lon))

req_zipcode = input(f'What zipcode do you want to get the weather for? ')

print(get_lanlon[req_zipcode])
