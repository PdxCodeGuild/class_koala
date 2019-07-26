import forecastio
import os

def weather(lat, lng):
    api_key = "5f96bbce0e67b37965b9ef3af8b32ceb"
    lat = float()
    lng = float()
    url = 'https://api.darksky.net/forecast/' + api_key + lat + ',' + lng

    forecast = forecastio.load_forecast(api_key, lat, lng)
    return forecast

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
    print('***********************************************************')
    print('***********************************************************\n')


name = input('What is your first name? ')
refresh_screen()
print (f'\nWelcome, {name}, to........\n')
header()

lat = input('Please enter your latitude: ')
lon = input('Please enter your longitude: ')

print(weather(lat, lon))
