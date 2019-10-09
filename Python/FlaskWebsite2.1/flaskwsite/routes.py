from flask import render_template, request
from flaskwsite import app
from flaskwsite import edict
from flaskwsite.forms import GameStore, Calculator
from flaskwsite.backend_gamestore import Backend
from flaskwsite.backend_calculator import Calc_Backend

flagAdd = False
flagSubtract = False
flagDivide = False
flagMultiply = False


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/links/')
def links():
    return render_template("links.html")


@app.route('/projects/')
def projects():
    return render_template("projects.html")


@app.route('/projects/pycalc/', methods=['GET', 'POST'])
def pycalc():
    form = Calculator()
    calc = Calc_Backend(form)
    global firstnum

    global flagAdd
    global flagSubtract
    global flagMultiply
    global flagDivide

    if calc.form.button_add.data:
        flagAdd = True
        returned = calc.binary_operation()
        firstnum = returned[0]
        return returned[1]

    elif calc.form.button_subtract.data:
        flagSubtract = True
        returned = calc.binary_operation()
        firstnum = returned[0]
        return returned[1]

    elif calc.form.button_multiply.data:
        flagMultiply = True
        returned = calc.binary_operation()
        firstnum = returned[0]
        return returned[1]

    elif calc.form.button_divide.data:
        flagDivide = True
        returned = calc.binary_operation()
        firstnum = returned[0]
        return returned[1]

    elif calc.form.button_eq.data:
        if flagAdd:
            flagAdd = False
            return calc.add_operation(firstnum)

        elif flagSubtract:
            flagSubtract = False
            return calc.subtract_operation(firstnum)

        elif flagMultiply:
            flagMultiply = False
            return calc.multiply_operation(firstnum)

        elif flagDivide:
            flagDivide = False
            return calc.divide_operation(firstnum)

    else:
        return calc.print_all()


@app.route('/projects/englishdict/')
def dictionary():
    return render_template("englishdict.html")


@app.route('/projects/englishdict/word', methods=['POST'])
def return_word():
    word = request.form['text']
    definiton = edict.main(word)
    return render_template("englishdict.html", definition=definiton, word=word)


@app.route('/projects/gamestore/', methods=['GET', 'POST'])
def gamestore():
    form = GameStore()
    backend = Backend(form)

    if backend.form.add_entry.data and backend.form.validate_on_submit():
        return backend.add_entry()

    elif backend.form.view_all.data:
        return backend.print_all()

    elif backend.form.search_entry.data:
        return backend.search_entry()

    elif backend.form.delete_all.data:
        return backend.delete_all()

    elif backend.form.delete_selected.data:
        return backend.delete_selected()

    elif backend.form.update_selected.data:
        return backend.update_selected()
    else:
        return render_template("gamestore.html", form=backend.form)


@app.route('/projects/webmap/')
def map():
    return render_template("map.html")


@app.route('/projects/webmap/clean_map')
def clean_map():
    return render_template("clean_map.html")
