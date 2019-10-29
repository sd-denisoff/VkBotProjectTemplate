from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class SomeForm(FlaskForm):
    text = StringField(label='Text', validators=[DataRequired(message='Это обязательное поле')])
    password = PasswordField(label='Password', validators=[DataRequired(message='Это обязательное поле')])
    submit = SubmitField('Submit')
