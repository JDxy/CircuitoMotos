import sqlite3
from urllib.request import Request
from bottle import route, run, request, template, get, post, redirect, static_file
from config.config import DATABASE
from forms.register import RegistrationForm
from forms.inicio import InicioForm
from models.clientes import Equipos

clientes = Equipos(DATABASE)

@route('/todo')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("select * from clientes")
    result = c.fetchall()
    return str(result)

@route('/equipos')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("select * from miembros_equipo")
    result = c.fetchall()
    return str(result)

@get('/new')
def register():
    form = RegistrationForm(request.POST)
    return template('register', form=form)


@post('/new')
def new_item_save():

        new1 = request.POST.nombre_equipo.strip()
        new2 = request.POST.nombre_miembro.strip()
        new3 = request.POST.apellidos_miembro.strip() 
        new4 = request.POST.ocupacion.strip()

        clientes.insertar_equipo(new1)
        clientes.insertar_miembros(new2, new3, new4)

        return redirect('/todo')

@get('/inicio')
def inicio():
    form = InicioForm(request.POST)
    return (template('inicio', form=form))

@post('/inicio')
def inicio():
    if request.POST.Iniciar_sesion:
        email = request.POST.email.strip()
        contrasena = request.POST.contrasena.strip()
        valido = clientes.validar_email(email)
        if valido == "true":
            contrasena_confirmada = clientes.validar_contrasena(email,contrasena)
            if contrasena_confirmada == "true":
                espectador_piloto = clientes.espectador_o_piloto(email)
                if espectador_piloto == "piloto":
                    return redirect(/pagina_piloto)
                else:
                    return redirect(/pagina_espectadores)
            else:
                


@get("/static/<filepath:path>")
def html(filepath):
    return static_file(filepath, root = "static")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)

