import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect('Weather.db') #creates a connection to the database
        self.cur = self.con.cursor() #cur is used to execute the SQL commands
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Weather (City, Condition, Fahrenheit, Celsius)''')
        self.con.commit()

    def insert_values(self, city_name, weather_data):
        self.cur.execute('''INSERT INTO Weather (city_name, weather_data['Current_Weather'], weather_data['temp_f'], weather_data['temp_c']) ''')
        self.con.commit()

    def print_db(self):

    def saved_location(self):
