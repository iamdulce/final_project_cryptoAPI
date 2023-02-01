from crypto_app import app
from flask import render_template, request
from config import *
from datetime import datetime, date
from crypto_app.models import *


@app.route("/")
def index():
    register = show_all()
    return render_template("index.html", data = register)

@app.route("/purchase", methods = ["GET", "POST"])
def purchase():
    if request.method == "GET":
        return render_template("purchase.html", data = {})

    else:
        if 'calculate' in request.form:
            from_coin = request.form['from_coin']
            from_quantity= float(request.form['from_quantity'])
            to_coin= request.form['to_coin']
            coin_rate = api_call(from_coin, to_coin)
            to_quantity = coin_rate * from_quantity

                    
            list_request = {
                'from_coin': from_coin,
                'from_quantity': from_quantity,
                'to_coin': to_coin,
                'to_quantity': to_quantity,
                'unit_price': coin_rate,
                }

            print("Lo que recibo desde el form: ", list_request)
        
            return render_template("purchase.html", data = list_request)

        if 'buy' in request.form:
            return "guardar en bbdd"



@app.route("/status")
def status():
    return render_template("status.html")