from flask import Flask

app = Flask(__name__)
app.config.from_object("config")#para que reconosca la clave secreta desde config.py

from crypto_app.routes import *