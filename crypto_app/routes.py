from crypto_app import app
from flask import render_template, request
from config import *
from datetime import datetime, date
from crypto_app.models import *
import requests


@app.route("/")
def index():
    register = show_all()
    return render_template("index.html", data = register)

@app.route("/purchase", methods = ["GET", "POST"])
def purchase():
    if request.method == "GET":
        return render_template("purchase.html", dataForm = {})

    else:
        print("Lo que recibo desde el form: ", request.form)
        
        if 'calculate' in request.form:
            while request.form['from_quantity'] != '' and request.form['from_coin'] and request.form['to_coin']:
             #WHILE INCOMPLETO: para validación de datos
             #CREAR CLASE o FUNCIÓN Y LLEVAR A MODELS para llamada a API
                time = date.today()
                base = request.form['from_coin']
                quote = request.form['to_coin']

                r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{quote}?time={time}&apikey={API_KEY}')
                coin_data = r.json()

                if r.status_code == 200:
                    print(coin_data['rate'])

                    '''
                    from_quantity = request.form['from_quantity']
                    from_coin = coin_data['asset_id_base']
                    to_coin = coin_data['asset_id_quote']
                    unit_price = coin_data['rate']
                    to_quantity = float(from_quantity) * float(unit_price)
                    '''

                else: 
                    raise Exception( f'Call assets failed:{r.status_code}')
                break
            return render_template("purchase.html", dataForm = request.form,)

        else:
            pass #AQUÍ GUARDO EN BBDD



@app.route("/status")
def status():
    return render_template("status.html")