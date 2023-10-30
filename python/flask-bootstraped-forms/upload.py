from flask import Flask, flash, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from markupsafe import escape
from time import sleep
from wtforms import SubmitField, BooleanField, IntegerField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class UploadForm(FlaskForm):
    student_id = IntegerField("Matrikelnummer", validators=[DataRequired()])
    first_name = StringField("Nachname", validators=[DataRequired()])
    last_name = StringField("Vorname", validators=[DataRequired()])
    report1 = FileField("Erstgutachten", validators=[FileRequired()])
    report2 = FileField("Zweitgutachten", validators=[FileRequired()])
    report_grade = FileField(
        "Notenmeldung", validators=[FileRequired()]
    )  # die excel sollte aber perspektivisch ganz abgeschafft werden!!!
    send = SubmitField("Absenden")


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
    return render_template("upload.html", form=form)
