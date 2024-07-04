import sqlite3
from datetime import date
class DB:
    def __init__(self):
        self.con = sqlite3.connect('Weather.db') #creates a connection to the database
        self.cur = self.con.cursor() #cur is used to execute the SQL commands
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Current_Weather (City, Condition, Date, Fahrenheit, Celsius)""")
        self.con.commit()

    def insert_values(self, city_name, weather_data):
        cur_w = weather_data['Current_Weather']
        temp_f = weather_data['Todays_high_f']
        temp_c = weather_data['Todays_high_c']
        date_today = date.today().isoformat()
        self.cur.execute("""
            INSERT INTO Current_Weather (City, Condition, Date, Fahrenheit, Celsius) 
            VALUES (?, ?, ?, ?, ?)
        """, (city_name, cur_w, date_today, temp_f, temp_c))
        self.con.commit()

    def print_desired_city(self, city_name):

        self.cur.execute(f'SELECT * FROM Current_Weather')
        row = self.cur.fetchall()

        for rows in row:
            if rows[0] == city_name:
                print(rows)
                return True

        return False
    def saved_cities(self):
        res = self.cur.execute('''SELECT City FROM Current_Weather''')

        return res.fetchall()

    def compare_data(self, city_name):

        select_query = f"""
                        SELECT Date
                        FROM Current_Weather
                        WHERE City = ?
                        """

        self.cur.execute(select_query, (city_name,))

        date_db = self.cur.fetchall()
        if date.today().isoformat() != date_db[0][0]:
            return False
        else:
            return True

    def update_db(self, city):
        update_query = f"""
                        UPDATE Current_Weather 
                        SET Date = ?
                        WHERE City = ?
                        """

        self.cur.execute(update_query, (date.today(), city))
        self.con.commit()

    def delete_row(self, city_name):
        delete_query = f"""DELETE FROM Current_Weather
                           WHERE City = ? """

        self.cur.execute(delete_query, (city_name,))
        self.con.commit()

        print('Row deleted!')