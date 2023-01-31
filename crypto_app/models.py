import requests
from config import *
from crypto_app.conexion_bbdd import *


# Debería mover la clase a otro archivo aparte?
class ModelError(Exception):
    pass

class CoinsApi:
    def __init__(self):
        self.coin_data = None
        self.base = None
        self.quote = None
        self.time = None
        self.rate = None
        self.r = None

    def getCoinData(self, apiKey):
        self.r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.base}/{self.quote}?apikey={apiKey}')
        # Falta agregar a la URL después de ?: time={self.time}&
        self.coin_data = self.r.json()

        if self.r.status_code == 200:
            self.base = self.coin_data['asset_id_base']
            self.quote = self.coin_data['asset_id_quote']
            self.time = self.coin_data['time']
            self.rate = self.coin_data['rate']
        else:
            raise ModelError( f'Call assets failed:{self.r.status_code}')

def show_all():
    connect = Conexion("SELECT id,date,time,from_coin,from_quantity,to_coin,to_quantity FROM movements ORDER BY date;")
    rows = connect.res.fetchall()
    columns = connect.res.description

    result = []
    for row in rows:
        data_info = {}
        position = 0

        for field in columns:
            data_info[field[0]] = row[position]
            position += 1
        result.append(data_info)

    connect.con.close()

    return result

def new_transaction():
    pass
