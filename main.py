import sqlite3
from bottle import route, run, request, template, get, post, redirect, static_file
from config.config import DATABASE
from forms.inicio import InicioForm
from models.clientes import Clientes

clientes = Clientes(DATABASE)

@route('/todo')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("select * from clientes")
    result = c.fetchall()
    return str(result)

@get('/new')
def register():
    form = InicioForm(request.POST)
    return template('inicio', form=form)



@post('/new')
def inicio():
    if request.POST.Iniciar_sesion:
        email = request.POST.email.strip()
        print(email)
        contrasena = request.POST.contrasena.strip()
        valido = clientes.validar_email(email)
        if valido == "true":
            contrasena_confirmada = clientes.validar_contrasena(email,contrasena)
            if contrasena_confirmada == "true":
                espectador_piloto = clientes.espectador_o_piloto(email)
                if espectador_piloto == "piloto":
                    return redirect('/pagina_piloto')
                else:
                    return redirect('/pagina_espectadores')
            else:
                return "eorror"

        return redirect('/todo')

@get("/static/<filepath:path>")
def html(filepath):
    return static_file(filepath, root = "static")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)

