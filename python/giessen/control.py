from flask import Flask, flash, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from markupsafe import escape
from time import sleep
from wtforms import SubmitField, BooleanField, IntegerField
import subprocess
import shlex


class PowerSwitchForm(FlaskForm):
    duration1 = IntegerField("Mother pump duration", default=0, render_kw={'class': 'form-control-sm'} )
    duration2 = IntegerField("Payload pump duration", default=0, render_kw={'class': 'form-control-sm'})
    duration3 = IntegerField("Cutlings pump duration", default=0, render_kw={'class': 'form-control-sm'})
    send = SubmitField("send")


app = Flask(__name__)
Bootstrap5(app)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lumen'
app.config['SECRET_KEY'] = 'asdf'

@app.route('/', methods=['GET', 'POST'])
def index():
    # GPIO
    form = PowerSwitchForm()
    if form.validate_on_submit() :
        duration1=form.duration1.data
        duration2=form.duration2.data
        duration3=form.duration3.data
        if duration1 > 0:
            pin=11
            cmd = f"python handle_gpio.py {pin} {duration1}"
            args = shlex.split(cmd)
            flash(cmd)
            subprocess.Popen(args)
        if duration2 > 0:
            pin=13
            sleep(duration1)
            cmd = f"python handle_gpio.py {pin} {duration2}"
            args = shlex.split(cmd)
            flash(cmd)
            subprocess.Popen(args)
        if duration3 > 0:
            pin=16
            sleep(duration1+duration2)
            cmd = f"python handle_gpio.py {pin} {duration3}"
            args = shlex.split(cmd)
            flash(cmd)
            subprocess.Popen(args, stdout=subprocess.PIPE)
    return render_template('button.html', form=form)
