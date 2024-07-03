from GetWeather import retrieveWeather

print("Want to know the forecast for today, just input a city!")
city = input('City: ')

print('-'*20)
data = retrieveWeather(city)

print('The current Weather is: ', data['Current_Weather'])
print(f"The current temperature in Celsius is: {data['Current_temp_c']}")
print(f"The current temperature in Fahrenheit is: {data['Current_temp_f']}")
