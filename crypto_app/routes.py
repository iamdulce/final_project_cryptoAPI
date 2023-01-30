from crypto_app import app
from flask import render_template, request
from config import *
from crypto_app.models import CoinsApi
from datetime import date


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
    return render_template("purchase.html")
    
    '''
   #infoCoin = CoinsApi()

    if request.method == "GET":
        return render_template("purchase.html", data_form = None)
    
    else:
        #Aquí iría lla llamada a la API con los datos que introduzco en el form
        return render_template("purchase.html")
        #infoCoin.coinData(API_KEY)
    '''

@app.route("/status")
def status():
    return render_template("status.html")