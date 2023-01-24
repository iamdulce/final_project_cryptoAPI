import sqlite3
from config import ORIGIN_DATA

class Conexion:
    def __init__(self, querySQL, new_data = []):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res =  self.cur.execute(querySQL, new_data)