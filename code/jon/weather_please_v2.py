import forecastio
import requests
import os
import argparse
import email,smtplib, ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    wanted_data = [data['currently']['summary'], data['currently']['temperature'], data['daily']['summary']]
    
    return wanted_data

# Displays all of the info 
def display(info):
    # Gets the current time
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    weather = info[0]
    current_temp = round(info[1])
    weather_summary = info[2]
    city = get_latlon(req_zipcode)[2]

    show_me_the_weather = (f'\nCurrently at {current_time} in {city}, the weather is {weather}.\nSummary for the week: {weather_summary}\nCurrent temperature: {current_temp} degrees F.\nSending you an email as well!')

    print(show_me_the_weather)
    return show_me_the_weather

# Place show_me_the_weather into a new text file
# def result_text():
#     result = display(weather(req_zipcode))
#     with open('weather.txt', 'wb') as file:
#        file.write(result)

# # Take weather.txt file and email it to my email address
def email_results():
    subject = 'Here is your weather report'
    body = 'This is an email with attachement sent from Python'
    sender_email = 'codeguildprogrammer@gmail.com'
    receiver_email = 'jon@jonbascos.com'
    
    # Creating a multipart message and headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    
    # Add body to email

    message.attach(MIMEText(body, 'plain'))

    # filename = 'weather.txt'

    with open('weather.txt', 'w+') as attachment:
        result = display(weather(req_zipcode))
        attachment.write(result)
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    #Add header as key/value pair to attachment part
    part.add_header(
        'Content-Disposition',
        f'attachment; filename = "weather.txt"',
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log-in, attach and send email
    port = 465 # For SSL
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context = context) as server:
        server.login(sender_email, 'p@ssword1234')
        server.sendmail(sender_email, receiver_email, text)

    print('Email Sent')


# Main
req_zipcode = ''

parser = argparse.ArgumentParser()
parser.add_argument('-z', '--zipcode', help = 'Enter zipcode for the place you would like a weather report for.')
parser.parse_args()
args = parser.parse_args()
req_zipcode = args.zipcode

if args.zipcode:
    
    display(weather(req_zipcode))
    email_results()
    
else:
    name = input('What is your first name? ')
    refresh_screen()
    print (f'\nWelcome, {name}, to........\n')
    header()

    req_zipcode = input(f'What zipcode do you want to get the weather for? ')

    display(weather(req_zipcode))
    email_results()

    

       