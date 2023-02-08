from flask import Flask

app = Flask(__name__)

from crypto_app.routes import *

#from crypto_app.prueba import *