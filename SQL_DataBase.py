import sqlite3

class DB():
    def __init__(self):
        self.con = sqlite3.connect('Weather.db') #creates a connection to the database
        self.cur = self.con.cursor() #cur is used to execute the SQL commands
