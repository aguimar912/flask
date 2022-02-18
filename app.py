from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return "hola mundo feo"

@app.route("/bonito") #para ver esto, en el navegador hay que poner esa ruta
def bonito():
    return render_template("index.html")