from crypto_app import app
from flask import render_template, request, redirect
from config import *
from datetime import datetime, date
from crypto_app.models import *
from crypto_app.forms import *


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

            
            while from_coin != 'EUR':
                sum_to_coin = sumToCoin(to_coin)
                sum_from_coin = sumFromCoin(from_coin)
                balance = sum_to_coin - sum_from_coin
                print('this is toC: ', sum_to_coin)
                print('this is fromC: ', sum_from_coin)
                print('balance is: ', balance)

                if from_quantity < balance:
                    print(f"You have enough {from_coin} to sell/trade. Current value: {sum_from_coin}")
                break

          
                    
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


@app.route("/status")
def status():
    
    from_coin = 'EUR'
    to_coin = 'EUR'

    return render_template("status.html", money_invested = sumFromCoin(from_coin), money_recovered = sumToCoin(to_coin))