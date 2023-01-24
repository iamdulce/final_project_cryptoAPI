from crypto_app import app

@app.route("/")
def index():
    return "Working"