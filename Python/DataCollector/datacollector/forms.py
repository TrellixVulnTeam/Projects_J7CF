from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class DataCollector(FlaskForm):
    email_addr = StringField('Your e-mail', validators=[DataRequired(), Length(min=2, max=50)])
    height = StringField('Your height in cm', validators=[DataRequired(), Length(min=2, max=50)])

    submit = SubmitField('Submit')
