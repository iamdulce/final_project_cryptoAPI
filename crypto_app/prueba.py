from crypto_app import app
from flask import render_template, request, redirect
from config import *
from datetime import datetime, date
from crypto_app.models import *
from crypto_app.forms import *


def validateForm():
    error=[]
    from_coin = request.form['from_coin']
    to_coin= request.form['to_coin']
    from_quantity = float(request.form['from_quantity'])
    
    if from_coin != 'EUR':
        sum_from_coin = sumFromCoin(from_coin)
        sum_to_coin = sumToCoin(to_coin)
        balance = sum_to_coin - sum_from_coin
        if sum_to_coin == 0:
            error.append(f"You don't have {to_coin} available")
        if from_quantity < balance:
            error.append(f"You don't have enough {from_coin} to sell/trade. Current value: {sum_from_coin}")
    if from_coin == to_coin:
            error.append("You can't do transactions between the same coin")
    return error

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
            
            error = validateForm()

            list_request = {
                    'from_coin': from_coin,
                    'from_quantity': from_quantity,
                    'to_coin': to_coin,
                    'to_quantity': to_quantity,
                    'unit_price': coin_rate,
                    }

            if error:
                return render_template("purchase.html", alertError = error, data = list_request)
            else:
                
                print("Lo que recibo desde el form: ", list_request)
                return render_template("purchase.html", data = list_request)

        if 'buy' in request.form:

            time = datetime.now()
            
            new_transaction([
                date.today(),
                time.strftime("%H:%M:%S"),
                request.form['from_coin'],
                request.form['from_quantity'],
                request.form['to_coin'],
                request.form['to_quantity'],
            ])

            return redirect('/')