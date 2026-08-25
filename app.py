from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Moi", image="cat.png")


@app.route("/owl")
def owl():
    return render_template("index.html", title="Owl", image="owl.svg")
