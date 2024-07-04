from GetWeather import retrieveWeather
from SQL_DataBase import DB
print("Welcome!")
print("Here are your options: ")
print("View Saved Locations(0), or lookup a new location(1)")
choice = input("Enter your choice: ")
db = DB()

while True:
    if choice == "1":
        city = input('City: ')
        print('---'*20)
        data = retrieveWeather(city)

        print(f"The current Weather Condition for {city} is:  {data['Current_Weather']}")
        print(f"The current temperature in Celsius is: {data['Todays_high_c']}")
        print(f"The current temperature in Fahrenheit is: {data['Todays_high_f']}")

        save_ans = input("Would you like to save this city?(y/n): ")

        if save_ans == 'y':
            db.insert_values(city, data)
    else:
        print('------Which city do you want up to day info from?------')
        print('Your current saved cities: ')
        cities = db.saved_cities()

        for city in cities:
            print(city)

        print('---'*20)
        desired_city = input("Which city would you like to look at?: ")

        same_date = db.compare_data(desired_city)

        if same_date == False:
            db.update_db(desired_city)
            db.print_desired_city(desired_city)
        else:
            db.print_desired_city(desired_city)

    cont = input("Would you like to continue?(y/n): ")
    if cont == 'n':
        break
    else:
        print("View Saved Locations(0), or lookup a new location(1)")
        choice = input("Enter your choice: ")
