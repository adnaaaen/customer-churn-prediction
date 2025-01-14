from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    send_from_directory 
)
import pandas as pd
from src.utils import predict_with_pipeline


app = Flask(__name__)

ALLOW_FILE_EXTENSIONS = ["csv"]


@app.route("/", methods=["GET", "POST"])
def home_redirect():
    return redirect(url_for("home"))


@app.route("/home/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/model/", methods=["GET", "POST"])
def model():
    return render_template("model.html")


@app.post("/predict/")
def make_prediction():
    if request.files["file"] and request.files["file"].filename.split(".")[1] in ALLOW_FILE_EXTENSIONS:
        filename = request.files["file"]
        df = pd.read_csv(filename)
        prediction = predict_with_pipeline(df)
        return render_template("model.html", prediction=enumerate(prediction, start=1))
    return redirect(url_for('model'))


@app.post("/download/")
def download_template():
    return send_from_directory(
        "uploads", "customer_churn_ip_template.csv", as_attachment=True
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
