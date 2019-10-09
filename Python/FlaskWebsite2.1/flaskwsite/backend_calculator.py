from flask import render_template, flash


class Calc_Backend(object):

    def __init__(self, form):
        self.form = form

    def print_all(self):
        if self.form.button_0.data:
            self.form.user_input.data += '0'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_1.data:
            self.form.user_input.data += '1'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_2.data:
            self.form.user_input.data += '2'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_3.data:
            self.form.user_input.data += '3'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_4.data:
            self.form.user_input.data += '4'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_5.data:
            self.form.user_input.data += '5'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_6.data:
            self.form.user_input.data += '6'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_7.data:
            self.form.user_input.data += '7'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_8.data:
            self.form.user_input.data += '8'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_9.data:
            self.form.user_input.data += '9'
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_clear.data:
            self.form.user_input.data = ''
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_percent.data:
            self.form.user_input.data = float(self.form.user_input.data)*(1/100)
            return render_template("pycalc.html", form=self.form)

        elif self.form.button_dot.data:
            if self.form.user_input.data.count('.') == 0:

                self.form.user_input.data += '.'
                return render_template("pycalc.html", form=self.form)
            else:
                return render_template("pycalc.html", form=self.form)

        elif self.form.button_pm.data:
            self.form.user_input.data = float(self.form.user_input.data) * (-1)
            return render_template("pycalc.html", form=self.form)

        else:
            return render_template("pycalc.html", form=self.form)

    def binary_operation(self):
        firstnum = float(self.form.user_input.data)
        self.form.user_input.data = ''
        return firstnum, render_template("pycalc.html", form=self.form)

    def add_operation(self, firstnum):
        secondnum = float(self.form.user_input.data)
        self.form.user_input.data = ''
        self.form.user_input.data = firstnum + secondnum
        return render_template("pycalc.html", form=self.form)

    def subtract_operation(self, firstnum):
        secondnum = float(self.form.user_input.data)
        self.form.user_input.data = ''
        self.form.user_input.data = firstnum - secondnum
        return render_template("pycalc.html", form=self.form)

    def multiply_operation(self, firstnum):
        secondnum = float(self.form.user_input.data)
        self.form.user_input.data = ''
        self.form.user_input.data = round(firstnum * secondnum, 4)
        return render_template("pycalc.html", form=self.form)

    def divide_operation(self, firstnum):
        try:
            secondnum = float(self.form.user_input.data)
            self.form.user_input.data = ''
            self.form.user_input.data = round(firstnum / secondnum, 4)
            return render_template("pycalc.html", form=self.form)
        except ZeroDivisionError:
            flash('Cannot divide by zero! ', 'danger')
            return render_template("pycalc.html", form=self.form)

