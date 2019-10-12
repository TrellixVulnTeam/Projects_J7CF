from flask import render_template
from datacollector import app
from datacollector.forms import DataCollector
from datacollector.backend import Backend


@app.route('/', methods=['GET', 'POST'])
def home():
    form = DataCollector()
    backend = Backend(form)

    if form.submit.data:
        return backend.add_entry()

    return render_template("home.html", form=form)
