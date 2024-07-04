import sqlite3
from datetime import date
class DB:
    def __init__(self):
        self.con = sqlite3.connect('Weather.db') #creates a connection to the database
        self.cur = self.con.cursor() #cur is used to execute the SQL commands
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Weather (City, Condition, Date, Fahrenheit, Celsius)
                            VALUES(?,?,?,?,?)""")
        self.con.commit()

    def insert_values(self, city_name, weather_data):
        cur_w = weather_data['Current_Weather']
        temp_f = weather_data['Todays_high_f']
        temp_c = weather_data['Todays_high_c']
        date = weather_data['Date']
        self.cur.execute("""INSERT INTO Weather (city_name, cur_w, date, temp_f, temp_c) 
                            VALUES(?,?,?,?,?)""")
        self.con.commit()

    def print_desired_city(self, city_name):

        res = self.cur.execute(f'SELECT * FROM Weather')
        row = res.fetchone()

        print(row[city_name])
    def saved_cities(self):
        res = self.cur.execute('''SELECT City FROM Weather''')

        return res.fetchall()

    def compare_data(self, city_name):

        select_query = f"""
                        SELECT Date
                        FROM Weather
                        WHERE City = ?
                        """

        self.cur.execute(select_query, (city_name,))

        date_db = self.cur.fetchall()

        if date.today() != date_db[0]:
            return False
        else:
            return True

    def update_db(self, city):
        update_query = f"""
                        UPDATE Weather 
                        SET Date = ?
                        WHERE City = ?
                        """

        self.cur.execute(update_query, (date.today(), city))
        self.con.commit()
