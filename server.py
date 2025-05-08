from flask import Flask

app = Flask(__name__)

@app.route("/")
def confirmacion():
    return "<p>Conexion OK</p>"