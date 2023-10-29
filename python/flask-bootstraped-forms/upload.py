from flask import Flask, flash, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from markupsafe import escape
from time import sleep
from wtforms import SubmitField, BooleanField, IntegerField


class UploadForm(FlaskForm):
    duration1 = IntegerField(
        "Mother pump duration",
        default=0,
        render_kw={"class": "form-control-sm"},
    )
    duration2 = IntegerField(
        "Payload pump duration",
        default=0,
        render_kw={"class": "form-control-sm"},
    )
    duration3 = IntegerField(
        "Cutlings pump duration",
        default=0,
        render_kw={"class": "form-control-sm"},
    )
    send = SubmitField("send")


app = Flask(__name__)
Bootstrap5(app)
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "lumen"
app.config["SECRET_KEY"] = "Happy420"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = UploadForm()
    return render_template("button.html", form=form)
