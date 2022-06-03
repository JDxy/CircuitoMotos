from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , RadioField, TextAreaField, SelectField, validators

def comprobar_email(email_nuevo):
    resultado = DATABASE.get(['email', {'email':email_nuevo}])
    if resultado != None:
        raise forms.ValidationError("Este email ya existe")

class RegistrationForm(Form):
    
    nombre = StringField('nombre', 
                               [validators.Length(min=4, max=25)],
                               default='nombre de usuario', 
                               render_kw={'class':'myclass'}
                            )
    apellidos  = StringField('apellidos', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                    validators.Email( message='Correo incorrecto')
                                ])
    contrasena = PasswordField('contrasena', [
                                    validators.Length(min=10, max=60),
                                    validators.EqualTo('password_confirm', message='Las contraseñas no coinciden')
                                ])

    comfirmar_contrasena = PasswordField('repetir contrasena')
    email  = StringField('Email Address', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                    validators.comprobar_email(email), 
                                    validators.Email( message='Correo incorrecto')
                                ])
    tipo_cliente = RadioField('Tipo Cliente', choices=[('Piloto'), ('Espectador')])
    save = SubmitField('Guardar')
    cancel = SubmitField('Cancelar')
    
