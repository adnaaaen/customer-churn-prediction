from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    send_from_directory,
)
import pandas as pd


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_redirect():
    return redirect(url_for("home"))


@app.route("/home/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.get("/predict/")
def predict():
    return render_template("predict.html")


@app.post("/predict/")
def make_prediction():
    if request.method == "POST":
        filename = request.files["file"]
        df = pd.read_csv(filename)
        print(df.shape)
    return render_template("predict.html")


@app.post("/download/")
def download_template():
    return send_from_directory(
        "uploads", "customer_churn_ip_template.csv", as_attachment=True
    )
