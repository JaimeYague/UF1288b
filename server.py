from flask import Flask

app = Flask(__name__)

@app.route("/")
def confirmacion():
    return "Mensaje recibido con exito :D"

@app.route("/mensajito")
def mensajito():
    return "mensajeeeee"
