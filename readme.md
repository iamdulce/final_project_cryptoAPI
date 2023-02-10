# Final Project for KeepCoding Bootcamp

# App Web My-Crypto

Made with Flask(Python) SQLite, CoinAPI and Pico.css, to simulate an app to buy/trade/sell cryptos.

## Install

-   In your python environment, execute the following command:

```
pip install -r requirements.txt
```

Framework used: flask https://flask.palletsprojects.com/en/2.2.x/

## Get your API key

-   You can get it from www.coinapi.com

## Database and API Set-Up

Rename the file _.config_template_ and add two variables, one with the path to your bbdd and the other with your API key:

`ORIGIN_DATA = "path/your_bbdd.sqlite"`
`API_KEY = '0000AAAA-00EE-00II-0O0O-0UUU000AAA00'`

## Create your database table

Copy the statement inside the file named **create_bbdd.sql** and create a new one.

## Run program

To initialize the server, rename the file named _.env_template_ to _.env_ and inside of it, add the following lines:

`FLASK_APP = main.py`
`FLASK_DEBUG = true`

This way you won't have to use a longer commands to run the server and the changes made will be seen in real time.

## Run the server

```
flask run
```

## Run server on a different port

```
flask -p run 5001
```
