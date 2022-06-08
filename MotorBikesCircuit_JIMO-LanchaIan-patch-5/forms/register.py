import os
from random import choices
import sys
sys.path.append('models') # add the models directory to the path
sys.path.append('forms')

from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , RadioField, TextAreaField, SelectField, validators
from config.config import DATABASE
#todo = Todo(DATABASE)


class RegistrationForm(Form):

    #def comprobar_email(form, email_nuevo):
        #resultado = DATABASE.get(['Email', {'Email':email_nuevo.data}])
        #if resultado != None:
            #raise validators.ValidationError("Este email ya existe")
    
    nombre = StringField('nombre', 
                               [validators.Length(min=4, max=25)],
                               default='nombre de usuario', 
                               render_kw={'class':'myclass'}
                            )
    apellidos  = StringField('apellidos', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                ])
    contrasena = PasswordField('contrasena', [
                                    validators.Length(min=10, max=60),
                                    validators.EqualTo('password_confirm', message='Las contraseñas no coinciden')
                                ])

    comfirmar_contrasena = PasswordField('repetir contrasena')
    email  = StringField('email', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                    validators.Email( message='Correo incorrecto')
                                ])
    tipo_cliente = RadioField('cliente_tipo', choices=[('piloto'), ('espectador')])
    miembro = RadioField('miembro', choices=[('miembro_si',('miembro_no'))])
    save_piloto = SubmitField('Guardar piloto')
    save_espectador = SubmitField('Guardar')
    
