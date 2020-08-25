from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")                             #Asi se pone la ruta de la pagina principal
def index():
    return render_template("index.html")

@app.route("/blogs")                         #Hay que agregar /hola despues de la direccion del servidor
def blogs():
    return render_template("blogs.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

app.run(debug = True)       #Mantener ejecucion, con debug en True esta activado el modo desarrollador