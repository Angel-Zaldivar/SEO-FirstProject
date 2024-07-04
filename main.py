from GetWeather import retrieveWeather
from SQL_DataBase import DB
print("Welcome!")
print("Here are your options: ")
print("lookup a new location(0), View Saved Locations(1), Delete a location(2)")
choice = input("Enter your choice: ")
db = DB()

while True:
    if choice == "0":
        city = input('City: ')
        print('---'*20)
        data = retrieveWeather(city)

        print(f"The current Weather Condition for {city} is:  {data['Current_Weather']}")
        print(f"The current temperature in Celsius is: {data['Todays_high_c']}")
        print(f"The current temperature in Fahrenheit is: {data['Todays_high_f']}")

        save_ans = input("Would you like to save this city?(y/n): ")

        if save_ans == 'y':
            db.insert_values(city, data)
    elif choice == "1":
        cities = db.saved_cities()

        if len(cities) == 0:
            print("There are no saved cities.")
        else:
            while True:
                print('------Which city do you want up to day info from?------')
                print('Your current saved cities: ')

                for city in cities:
                    print(city[0])

                print('---'*20)
                desired_city = input("Which city would you like to look at?: ")

                same_date = db.compare_data(desired_city)

                if not same_date:
                    db.update_db(desired_city)
                    db.print_desired_city(desired_city)
                else:
                    db.print_desired_city(desired_city)

                cont_saved = input('Would you like to continue looking at your locations?(y/n): ')

                if cont_saved == 'n':
                    break
    else:
        while True:
            cities = db.saved_cities()
            print('------Which city do you want up to delete------')
            for city in cities:
                print(city[0])
            print('---'*20)
            delete_city = input('City: ')

            db.delete_row(delete_city)

            cont_deletion = input('Would you like to continue deleting?(y/n): ')

            if cont_deletion == 'n':
                break


    cont = input("This is the end of the app, would you like to continue?(y/n): ")
    if cont == 'n':
        break
    else:
        print("lookup a new location(0), View Saved Locations(1), Delete a location(2)")
        choice = input("Enter your choice: ")
