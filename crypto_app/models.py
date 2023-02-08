import requests
from config import *
from crypto_app.conexion_bbdd import *


def api_call(base, quote):
    call = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{quote}?&apikey={API_KEY}')
    coin_data = call.json()
    if call.status_code == 200:
        return coin_data['rate']
    else: 
        raise Exception( f'Call assets failed:{call.status_code}')

#Home function
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


#Purchase functions
def new_transaction(newRegister):
    connectNew= Conexion("INSERT INTO movements(date,time,from_coin,from_quantity,to_coin,to_quantity) VALUES(?,?,?,?,?,?)",newRegister)
    connectNew.con.commit()
    connectNew.con.close()


def sumFromCoin(coin):
    connectSumfc = Conexion(f"SELECT coalesce(sum(from_quantity),0) FROM movements WHERE from_coin IS'{coin}'")
    result = connectSumfc.res.fetchall()
    connectSumfc.con.close()

    return result[0][0]


def sumToCoin(coin):
    connectSumtc = Conexion(f"SELECT coalesce(sum(to_quantity),0) FROM movements WHERE to_coin IS '{coin}'")
    result = connectSumtc.res.fetchall()
    connectSumtc.con.close()

    return result[0][0]
