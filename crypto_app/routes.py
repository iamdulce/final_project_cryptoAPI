from crypto_app import app
from flask import render_template, request
from config import *
from datetime import date
#from crypto_app.models import CoinsApi
import requests


@app.route("/")
def index():
    data_inputs = [
        {"id": 1, 
        "date": "25-01-2023", 
        "time": "22:17:34", 
        "from_coin": "EUR",
        "from_quantity": 500,
        "to_coin": "BTC",
        "to_quantity": 2
        }
    ]

    return render_template("index.html", data = data_inputs)

@app.route("/purchase", methods = ["GET", "POST"])
def purchase():
    if request.method == "GET":
        return render_template("purchase.html")
    else:
        print("Lo que recibo desde el form: ", request.form)
        
        if request.form['from_coin'] and request.form['from_quantity']:
            time = date.today() # Cómo obtengo esto en el form?
            base = request.form['from_coin']
            quote = request.form['to_coin']

            r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{quote}?time={time}&apikey={API_KEY}')
            coin_data = r.json()

            if r.status_code == 200:
                print(coin_data['asset_id_base'])
                print(coin_data['asset_id_quote'])
                print(coin_data['time'])
                print(coin_data['rate'])
            else: 
                raise Exception( f'Call assets failed:{r.status_code}')
            
        return "aquí va el post"


    
    '''
   #infoCoin = CoinsApi()

    if request.method == "GET":
        return render_template("purchase.html")
    
    else:
        #Aquí iría lla llamada a la API con los datos que introduzco en el form
        return render_template("purchase.html")
        #infoCoin.coinData(API_KEY)
    '''

@app.route("/status")
def status():
    return render_template("status.html")