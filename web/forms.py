from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class SomeForm(FlaskForm):
    login = StringField(label='Login', validators=[DataRequired(message='Это обязательное поле')])
    password = PasswordField(label='Password', validators=[DataRequired(message='Это обязательное поле')])
    submit = SubmitField('Submit')
