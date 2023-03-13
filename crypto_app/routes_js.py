from crypto_app import app
from flask import jsonify, render_template, request, redirect
from config import *
from datetime import datetime, date
from crypto_app.models import *


@app.route("/")
def index():
    return render_template("main.html")

'''
Todo se muestra en una sola vista
'''

#GET: Devuelve lista de movimientos o mensaje de error (json)
@app.route(f"/api/{VERSION}/all_movements")
def all_movements():
    register = show_all()
    return jsonify(register) #Muestra los datos de mi bbdd en formato json

#GET: Trade -> Comprobar que haya suficiente de la from_coin
@app.route(f"/api/{VERSION}/rate/from_coin/to_coin", methods =["GET"])
def purchase():
    pass

#POST: Guardo como registro nuevo a la transacción. Compra (de euros a btc o btc disponible a otra), tradeo (entre bitcoins), venta (btc a eur)
@app.route(f"/api/{VERSION}/new_movement", methods = ["POST"])
def new_movement():
    pass

#GET: muestra el estado de la inversión
@app.route(f"/api/{VERSION}/status")
def status():
    pass