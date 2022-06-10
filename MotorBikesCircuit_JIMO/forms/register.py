import os
from random import choices
import sys
sys.path.append('models') # add the models directory to the path
sys.path.append('forms')
from email_validator import EmailNotValidError
from WTForms import Form, BooleanField, StringField, PasswordField, SubmitField , RadioField, TextAreaField, SelectField, validators
from config.config import DATABASE
#todo = Todo(DATABASE)


class RegistrationForm(Form):

    #def comprobar_email(form, email_nuevo):
        #resultado = DATABASE.get(['Email', {'Email':email_nuevo.data}])
        #if resultado != None:
            #raise validators.ValidationError("Este email ya existe")
    
    nombre_equipo = StringField('nombre del equipo', 
                               [validators.Length(min=4, max=30)],
                               default='nombre del equipo', 
                               render_kw={'class':'myclass'}
                            )
    nombre_miembro = StringField('nombre del integrante', 
                               [validators.Length(min=4, max=25)],
                               default='nombre del miembro', 
                               render_kw={'class':'myclass'}
                            )
    apellidos_miembro  = StringField('apellidos del integrante', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                ])
    ocupacion  = StringField('ocupacion del integrante', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                ])
    save_equipo = SubmitField('Guardar equipo')