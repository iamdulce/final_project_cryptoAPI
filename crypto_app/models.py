import requests
#import sqlite3
#from crypto_app.conexion_bbdd import *
from datetime import date




#- PROBANDO LLAMADA A API -
time = date.today() # Cómo obtengo esto en el form?
base = "EUR"
quote = "BTC"
API_KEY = "8B30787E-E140-44C4-B21A-E093FB2DAE75"

r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{quote}?time={time}&apikey={API_KEY}')
coin_data = r.json()

if r.status_code == 200:
    print(coin_data['asset_id_base'])
    print(coin_data['asset_id_quote'])
    print(coin_data['time'])
    print(coin_data['rate'])
else: 
    raise Exception( f'Call assets failed:{r.status_code}')

# Falta agregar a la URL después de ?: time={self.time}&

'''
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
        self.coin_data = self.r.json()

        if self.r.status_code == 200:
            self.base = self.coin_data['asset_id_base']
            self.quote = self.coin_data['asset_id_quote']
            self.time = self.coin_data['time']
            self.rate = self.coin_data['rate']
        else:
            raise ModelError( f'Call assets failed:{self.r.status_code}')
'''
