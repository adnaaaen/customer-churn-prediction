from flask import Flask, render_template


app = Flask(__name__)


@app.route("/home/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.post("/predict/")
def predict():
    prediction = "demo"
    return render_template("home.html", prediction=prediction)
