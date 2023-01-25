from crypto_app import app
from flask import render_template

@app.route("/")
def index():
    data_inputs = [
        {"id": 1, 
        "date": "25-01-2023", 
        "time": "22:17:34", 
        "from_coin": "EUR",
        "from_quantity": 500,
        "to_coin": "BTC",
        "to_quantity": 2
        }
    ]

    return render_template("index.html", data = data_inputs)