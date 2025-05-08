from flask import Flask

app = Flask(__name__)

@app.route("/")
def confirmacion():
    return "Mensaje recibido con exito :D"

@app.route("/clientone")
def clientone():
    return "mensaje de cliente uno"

@app.route("/clientwo")
def clienttwo():
    return "mensaje de cliente dos"
