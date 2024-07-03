import requests
import json

#API Key: 5956245bd2754f27a65213703240307

def retrieveForecast(city):
    important_Weather_Details = {}
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=5956245bd2754f27a65213703240307&q={city}&days=1&aqi=yes&alerts=yes')

    data = response.json()

    important_Weather_Details['Current_Forecast'] = data['current']['condition']['text']
    important_Weather_Details['Current_temp_c'] = data['current']['temp_c']
    important_Weather_Details['Current_temp_f'] = data['current']['temp_f']
    important_Weather_Details['Current_humidity'] = data['current']['humidity']

    return important_Weather_Details

