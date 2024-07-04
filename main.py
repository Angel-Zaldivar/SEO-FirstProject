from GetWeather import retrieveWeather
from SQL_DataBase import DB
print("Welcome!")
print("Here are your options: ")
print("View Saved Locations(0), or lookup a new location(1)")
choice = input("Enter your choice: ")
db = DB()

if choice == "1":
    city = input('City: ')
    print('-'*20)
    data = retrieveWeather(city)

    print(f'The current Weather Condition for {city} is:  {data['Current_Weather']}')
    print(f"The current temperature in Celsius is: {data['Current_temp_c']}")
    print(f"The current temperature in Fahrenheit is: {data['Current_temp_f']}")

    save_ans = input("Would you like to save this city?(y/n): ")

    if save_ans == 'y':
        db.insert_values(city, data)
else:
    #user provides city and weather get returned,
    #weather should get updated
    #-------figure out how to update tables info---------
    print('------Which city do you want up to day info from?------')
    print('Your current saved cities: ')
