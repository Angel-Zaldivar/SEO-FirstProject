from datetime import date
import requests
import json

def retrieveWeather(city):
    important_Weather_Details = {}
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=5956245bd2754f27a65213703240307&q={city}&days=1&aqi=no&alerts=no')

    data = response.json()
    important_Weather_Details['City'] = city
    important_Weather_Details['Current_Weather'] = data['current']['condition']['text']
    important_Weather_Details['Todays_high_c'] = data['current']['Todays_high_c']
    important_Weather_Details['Todays_high_f'] = data['current']['Todays_high_f']
    important_Weather_Details['Todays_Date'] = date.today()

    return important_Weather_Details

