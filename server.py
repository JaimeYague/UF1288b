from flask import Flask

app = Flask(__name__)

@app.route("/")
def confirmacion():
    return "Mensaje recibido con exito :D"

@app.route("/clientone")
def clientone():
    return "mensaje de cliente uno"

@app.route("/clienttwo")
def clienttwo():
    return "mensaje de cliente dos"


if __name__ == '__main__':
    # Si se ejecuta server.py, entonces inicia el servidor Flask
    app.run(host='0.0.0.0', port=5000)