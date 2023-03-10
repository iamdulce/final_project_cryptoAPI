from crypto_app import app
from flask import render_template, request, redirect
from config import *
from datetime import datetime, date
from crypto_app.models import *


@app.route("/")
def index():
    register = show_all()

    return render_template("index.html", data = register, page = 'home')


@app.route("/purchase", methods = ["GET", "POST"])
def purchase():
    if request.method == "GET":
        return render_template("purchase.html", page = 'purchase', data = {}, purchase_error = 'bt_enable')

    else:
        if 'calculate' in request.form:
            from_coin = request.form['from_coin']
            from_quantity= float(request.form['from_quantity'])
            to_coin= request.form['to_coin']
            coin_rate = api_call(from_coin, to_coin)
            to_quantity = coin_rate * from_quantity 

            error = validateForm(from_quantity, from_coin)

            list_request = {
                    'from_coin': from_coin,
                    'from_quantity': from_quantity,
                    'to_coin': to_coin,
                    'to_quantity': to_quantity,
                    'unit_price': coin_rate,
                    }

            if error:
                return render_template("purchase.html", page = 'purchase', alertError = error, data = list_request, purchase_error = 'bt_disable')
            else:
                return render_template("purchase.html", page = 'purchase', data = list_request, purchase_error = 'bt_enable')

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
    invested = investedMoney()
    recovered = recoveredMoney()
    current_value = 0
    coins_bbdd = purchased_coins()

    purchase_val = invested - recovered

    for coin in coins_bbdd:
        balance = crypto_balance(coin)
        print('this is balance ', balance)
        if balance > 0:
            current_value += balance * api_call(coin, 'EUR')
            print("this is current value ", current_value)

    profit_loss = current_value - purchase_val
    if profit_loss < 0:
        status = 'loss'
    else:
        status = 'profit'

    return render_template("status.html", page = 'status', money_invested = invested, money_recovered = recovered, purchase_value = purchase_val, current_value = current_value, profit_loss = profit_loss, pl_status = status)
