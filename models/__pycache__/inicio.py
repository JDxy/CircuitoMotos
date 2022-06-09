import os
from random import choices
import sys
sys.path.append('models') # add the models directory to the path
sys.path.append('forms')

from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , RadioField, TextAreaField, SelectField, validators
from config.config import DATABASE

class InicioForm(Form):

    email  = StringField('email', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                    validators.Email( message='Correo incorrecto')
                                ])

    contrasena = PasswordField('contrasena', [
                                    validators.Length(min=10, max=60),
                                    validators.EqualTo('password_confirm', message='Las contraseñas no coinciden')
                                ])

    iniciar_sesion = SubmitField('Iniciar')