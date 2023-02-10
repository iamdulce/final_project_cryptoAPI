import requests
from flask import request
from config import *
from crypto_app.conexion_bbdd import *


def api_call(base, quote):
    call = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{quote}?&apikey={API_KEY}')
    coin_data = call.json()
    if call.status_code == 200:
        return coin_data['rate']
    else: 
        raise Exception( f'Call assets failed:{call.status_code}')


def show_all():
    connect = Conexion("SELECT id,date,time,from_coin,from_quantity,to_coin,to_quantity FROM movements ORDER BY date;")
    rows = connect.res.fetchall()
    columns = connect.res.description

    result = []
    for row in rows:
        data_info = {}
        position = 0

        for field in columns:
            data_info[field[0]] = row[position]
            position += 1
        result.append(data_info)

    connect.con.close()

    return result


def new_transaction(newRegister):
    connectNew= Conexion("INSERT INTO movements(date,time,from_coin,from_quantity,to_coin,to_quantity) VALUES(?,?,?,?,?,?)",newRegister)
    connectNew.con.commit()
    connectNew.con.close()


def investedMoney():
    connectInvested = Conexion(f"SELECT coalesce(sum(from_quantity),0) FROM movements WHERE from_coin IS 'EUR'")
    result = connectInvested.res.fetchall()
    connectInvested.con.close()

    return result[0][0]


def recoveredMoney():
    connectRecovered = Conexion(f"SELECT coalesce(sum(to_quantity),0) FROM movements WHERE to_coin IS 'EUR'")
    result = connectRecovered.res.fetchall()
    connectRecovered.con.close()

    return result[0][0]


def crypto_balance(coin):
    connectBalance1 = Conexion(f"SELECT coalesce(sum(to_quantity),0) FROM movements WHERE to_coin IS '{coin}' AND (to_coin NOT LIKE 'EUR')")
    connectBalance2 = Conexion(f"SELECT coalesce(sum(from_quantity),0) FROM movements WHERE from_coin IS '{coin}' AND (from_coin NOT LIKE 'EUR')")
    result1 = connectBalance1.res.fetchall()
    result2 = connectBalance2.res.fetchall()
    connectBalance1.con.close()
    connectBalance2.con.close()

    balance = result1[0][0] - result2[0][0]
    
    return balance


def validateForm(from_quantity, coin):
    error=[]
    to_coin= request.form['to_coin']
    from_coin = request.form['from_coin']

    if from_coin == to_coin:
        error.append("You can't make transactions between the same coin")
    if from_coin != 'EUR': 
        if from_quantity > crypto_balance(coin):
            error.append(f"You don't have enough {from_coin} to sell/trade. Current credit: {crypto_balance(coin)}")
    
    return error


def purchased_coins():
    connect = Conexion("SELECT DISTINCT to_coin FROM movements WHERE to_coin NOT LIKE 'EUR'")
    result = [r[0] for r in connect.res]
    connect.con.close()

    print('this is what purchased_coins returns: ', result)

    if result == []:
        return ''
    else:
        return result