from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length



class GameStore(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    company = StringField('Company', validators=[DataRequired(), Length(min=2, max=50)])
    type = StringField('Type', validators=[DataRequired(), Length(min=2, max=50)])
    rdate = StringField('Year', validators=[DataRequired(), Length(min=2, max=50)])

    add_entry = SubmitField('Add Entry')
    view_all = SubmitField('View All')
    search_entry = SubmitField('Search Entry')
    update_selected = SubmitField('Update Selected')
    delete_selected = SubmitField('Delete Selected')
    delete_all = SubmitField('Delete All')

    table = SelectMultipleField(u'Your Games: ')


class Calculator(FlaskForm):
    user_input = StringField('Input', validators=[DataRequired(), Length(min=2, max=50)])

    button_0 = SubmitField('0')
    button_1 = SubmitField('1')
    button_2 = SubmitField('2')
    button_3 = SubmitField('3')
    button_4 = SubmitField('4')
    button_5 = SubmitField('5')
    button_6 = SubmitField('6')
    button_7 = SubmitField('7')
    button_8 = SubmitField('8')
    button_9 = SubmitField('9')
    button_dot = SubmitField('.')
    button_pm = SubmitField('+/_')

    button_clear = SubmitField('C')

    button_subtract = SubmitField('-')
    button_add = SubmitField('+')
    button_divide = SubmitField('/')
    button_multiply = SubmitField('*')

    button_percent = SubmitField('%')
    button_eq = SubmitField('=')
