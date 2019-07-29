import forecastio
import requests
import os
import argparse
from datetime import datetime

"""
    To-Do:
        - Still need to implement an email function:
            - needs to take results of display() and save it into a file
            - take that file and email it to me
"""



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

# Gets latitude and longitude of the zipcode
def get_latlon(zipcode):
    map_api = 'VhicHGxyitNwdtTPZFczl8z9TeeM0voN'
    map_url = 'http://www.mapquestapi.com/geocoding/v1/address?key=' + map_api + '&location=' + str(zipcode)

    # Retrieves the info from the mapquest API
    map_res = requests.get(map_url)
    # Stores the retreived data as a JSON file
    map_data = map_res.json()

    # Extracts and stores the city name from the JSON file
    map_location = map_data['results'][0]['locations'][0]['adminArea5']
    # Extracts and stores the latitude of the zipcode from the JSON file
    map_latitude = map_data['results'][0]['locations'][0]['latLng']['lat']
    # Extracts and stores the longitude of the zipcode from the JSON file
    map_longitude = map_data['results'][0]['locations'][0]['latLng']['lng']

    return (map_latitude, map_longitude, map_location)

# Gets the weather from the Dark Sky API using the Lat/Lon from get_latlon()
def weather(zipcode):
    api_key = "5f96bbce0e67b37965b9ef3af8b32ceb"
    weather_latitude = get_latlon(req_zipcode)[0]
    weather_longitude = get_latlon(req_zipcode)[1]
    print(f'Latitude: {weather_latitude}')
    print(f'Longitude: {weather_longitude}')
    forecast = forecastio.load_forecast(api_key, weather_latitude, weather_longitude, units='us')
    
    # Stores the weather information from the darksky API as a JSON file
    data = forecast.json

    # Extracts and stores the current summary of the weather (sunny, cloudy, rainy, partly cloudy, etc.), current temperature, what temperature it actually feels like and the weather summary for the day
    wanted_data = [data['currently']['summary'], data['currently']['temperature'], data['currently']['apparentTemperature'], data['daily']['summary']]
    
    return wanted_data

# Displays all of the info 
def display(info):
    # Gets the current time
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    weather = info[0]
    current_temp = info[1]
    feels_temp = info[2]
    weather_summary = info[3]
    city = get_latlon(req_zipcode)[2]

    print(f'Currently at {current_time} in {city}, the weather is {weather}.')  
    print(f'Your weather summary for the week is: {weather_summary}.')
    print(f'The current temperature is {current_temp} degrees F but feels more like {feels_temp} degrees F.')

# Main
req_zipcode = ''

parser = argparse.ArgumentParser()
parser.add_argument('-z', '--zipcode', help = 'Enter zipcode for the place you would like a weather report for.')
parser.parse_args()
args = parser.parse_args()
req_zipcode = args.zipcode

if args.zipcode:
    
    display(weather(req_zipcode))
    
else:
    name = input('What is your first name? ')
    refresh_screen()
    print (f'\nWelcome, {name}, to........\n')
    header()

    req_zipcode = input(f'What zipcode do you want to get the weather for? ')

    display(weather(req_zipcode))
    

       