from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")                             #Asi se pone la ruta de la pagina principal
def index():
    return render_template("index.html")

@app.route("/hola")                         #Hay que agregar /hola despues de la direccion del servidor
def hola():
    return render_template("hola.html")

app.run(debug = True)       #Mantener ejecucion, con debug en True esta activado el modo desarrollador