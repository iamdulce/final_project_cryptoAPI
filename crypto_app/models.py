import requests
from config import *
from crypto_app.conexion_bbdd import *


# Debería mover la clase a otro archivo aparte?

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


def invested():
    connectInvested = Conexion("SELECT sum(from_quantity) FROM movements WHERE from_coin is 'EUR'")
    result = connectInvested.res.fetchall()
    connectInvested.con.close()

    return result[0][0]


def recovered():
    connectRecovered = Conexion("SELECT sum(to_quantity) FROM movements WHERE to_coin is 'EUR'")
    result = connectRecovered.res.fetchall()
    connectRecovered.con.close()

    return result[0][0]