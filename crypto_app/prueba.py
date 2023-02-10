from crypto_app import app
from flask import render_template, request, redirect
from config import *
from datetime import datetime, date
from crypto_app.models import *

'''
def validateForm(from_quantity, coin):
    error=[]
    to_coin= request.form['to_coin']
    from_coin = request.form['from_coin']


    if from_coin == to_coin:
        error.append("You can't make transactions between the same coin")
    if from_quantity > crypto_total(coin):
         error.append(f"You don't have enough {from_coin} to sell/trade. Current credit: {crypto_total(coin)}")
    
    return error

@app.route("/purchase", methods = ["GET", "POST"])
def purchase():
    if request.method == "GET":
        return render_template("purchase.html", page = 'purchase', data = {})

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
                return render_template("purchase.html", page = 'purchase', alertError = error, data = list_request)
            else:
                
                print("Lo que recibo desde el form: ", list_request)
                return render_template("purchase.html", page = 'purchase', data = list_request)

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
'''

@app.route("/status")
def status():
    invested = investedMoney()
    recovered = recoveredMoney()
    current_value = 0
    coins_bbdd = purchased_coins()

    print("this is my variable (should be the list): " , coins_bbdd)


    for coin in coins_bbdd:
        balance = crypto_balance(coin)
        print('this is balance ', balance)
        if balance > 0:
            current_value += balance * api_call(coin, 'EUR')
            print("this is current value ", current_value)

    return render_template("status.html", page = 'status', money_invested = invested, money_recovered = recovered, current_value = current_value)