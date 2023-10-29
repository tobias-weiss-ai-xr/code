from flask_bootstrap import Bootstrap5
from flask import Flask, redirect, render_template, url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename

app = Flask(__name__)
bootstrap = Bootstrap5(app)


class UploadForm(FlaskForm):
    file = FileField()


from flask import Flask

app = Flask(__name__)


@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save("uploads/" + filename)
        return redirect(url_for("upload"))

    return render_template("upload.html", form=form)
