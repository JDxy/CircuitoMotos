import sqlite3
from bottle import route, run, request, template, get, post, redirect, static_file
from config.config import DATABASE
# from forms.inicio import InicioForm
from models.clientes import Clientes
from models.events import Event
from forms.inicio import InicioForm
from forms.register import RegistrationForm
clientes = Clientes(DATABASE)
event = Event(DATABASE)

@route('/todo')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("select * from clientes")
    result = c.fetchall()
    return str(result)

@route('/espectadores')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("select * from espectador")
    result = c.fetchall()
    return str(result)

@get('/new')
def register():
    form = RegistrationForm(request.POST)
    return template('register', form=form)

@post('/new')
def new_item_save():

    if request.POST.save_espectador: 
        new1 = request.POST.nombre.strip()
        new2 = request.POST.apellidos.strip()
        new3 = request.POST.email.strip() 
        new4 = request.POST.contrasena.strip()
        new5 = request.POST.tipo_cliente.strip()
        new6 = request.POST.espectador_tipo.strip()

        clientes.insertar_cliente(new1,new2,new3,new4,new5)
        clientes.insertar_espectadores(new3,new6)
        #new_id = c.lastrowid
        return redirect('/todo')

    if request.POST.save_piloto:
        new1 = request.POST.nombre.strip()
        new2 = request.POST.apellidos.strip()
        new3 = request.POST.email.strip()
        new4 = request.POST.contrasena.strip()
        new5 = request.POST.tipo_cliente.strip()
        new6 = request.POST.carreras.strip()

        clientes.insertar_cliente(new1,new2,new3,new4,new5)

        return redirect('/todo')

@get('/inicio')
def inicio():
    form = InicioForm(request.POST)
    return (template('inicio', form=form))

@post('/Inicio')
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

@route('/events/user')
def event_list():
    return template('events_users', rows=event.select())

@route('/events/admin')
def event_list():
    return template('make_event', rows=event.select())

@route('/events/admin')
def event_list():
    return template('make_table', rows=event.select())

@get('/new_event')
def new_event_form():
    return template('new_event')

@get('/new_event_client')
def new_client_form():
    return template('new_client')

@get('/new_moto_client')
def new_client_form():
    return template('registrar_moto')



@post('/new_event/client')
def new_client_save():
    if request.POST.save:
        nombre = request.POST.Nombre.strip()
        apellidos = request.POST.Apellidos.strip()
        dni = request.POST.DNI.strip()
        telefono = request.POST.Telefono.strip()
        email = request.POST.Email.strip()
        cod_evento = request.POST.Cod_evento.strip()
        tipo_cliente = request.POST.Tipo_cliente.strip()
        event.insert_cliente(nombre, apellidos, dni, telefono, email, cod_evento)
        redirect('/events/user')

from bottle import route, run, template, request, get, post, redirect, static_file
from config.config import DATABASE
from models.events import Event

event = Event(DATABASE)

@route('/events/user')
def event_list():
    return template('events_users', rows=event.select())

@route('/events/admin')
def event_list():
    return template('make_event', rows=event.select())

@get('/new_event')
def new_event_form():
    return template('new_event')

@get('/new_event_client')
def new_client_form():
    return template('new_client')

@get('/new_moto_client')
def new_client_form():
    return template('registrar_moto')



@post('/new_event/client')
def new_client_save():
    if request.POST.save:
        nombre = request.POST.Nombre.strip()
        apellidos = request.POST.Apellidos.strip()
        dni = request.POST.DNI.strip()
        telefono = request.POST.Telefono.strip()
        email = request.POST.Email.strip()
        cod_evento = request.POST.Cod_evento.strip()
        tipo_cliente = request.POST.Tipo_cliente.strip()
        event.insert_cliente(nombre, apellidos, dni, telefono, email, cod_evento)
        redirect('/events/user')

@post('/new_event')
def new_event_save():
    if request.POST.save:  # the user clicked the `save` button
        fecha_inicio = request.POST.Fecha_inicio.strip()
        fecha_fin = request.POST.Fecha_fin.strip()
        categoria = request.POST.categoria.strip()
        coste_participantes = request.POST.Coste_participantes.strip()
        coste_espectadores = request.POST.Coste_espectadores.strip()
        event.insert_event(fecha_inicio, fecha_fin, categoria, coste_participantes, coste_espectadores)
        return redirect('/events/admin')

@get('/edit/<no:int>')
def edit_item_form(no):
    cur_data = event.get_event(no)  # get the current data for the item we are editing
    return template('edit_event', old=cur_data, no=no)


@post('/edit/<no:int>')
def edit_item(no):

    if request.POST.save:
        # get the values of the form
        fecha_inicio = request.POST.Fecha_inicio.strip()
        fecha_fin = request.POST.Fecha_fin.strip()
        categoria = request.POST.categoria.strip()
        coste_participantes = request.POST.Coste_participantes.strip()
        coste_espectadores = request.POST.Coste_espectadores.strip()

        event.update(no, fecha_inicio, fecha_fin, categoria, coste_participantes, coste_espectadores)
        
        return redirect('/events/admin')

@get('/delete/<no:int>')
def delete_item_form(no):
    cur_data = event.get_event(no)  # get the current data for the item we are editing
    return template('delete_event', old=cur_data, no=no)
    
@get("/statics/<filepath:path>")
def html(filepath):
    return static_file(filepath, root="statics")

@post('/delete/<no:int>')
def delete_item(no):
    if request.POST.delete:
        event.delete(no)
    return redirect('/events/admin')

if __name__ == '__main__':
   run(host='localhost', port=8080, debug=True, reloader=True)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)

