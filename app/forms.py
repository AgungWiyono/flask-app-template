# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, DateTimeField, PasswordField
from wtforms.validators import InputRequired


class ExampleForm(FlaskForm):
    title = TextField(u'Título', validators=[InputRequired()])
    content = TextAreaField(u'Conteúdo')
    date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')
    # recaptcha = RecaptchaField(u'Recaptcha')


class LoginForm(FlaskForm):
    user = TextField(u'Usuário', validators=[InputRequired()])
    password = PasswordField(u'Senha', validators=[InputRequired()])
