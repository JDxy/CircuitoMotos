from distutils.log import error
import sqlite3
from bottle import route, run, request, template, get, post, redirect, static_file
from config.config import DATABASE
from forms.inicio import InicioForm
from models.clientes import Clientes
from models.events import Event
from forms.inicio import InicioForm
from forms.register import RegistrationForm
from models.motos import Motos
clientes = Clientes(DATABASE)
event = Event(DATABASE)
motos = Motos(DATABASE)
valor_madre = "None"

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

@route('/')
def register():
    return template('index')

@get('/registrarse')
def register():
    form = RegistrationForm(request.POST)
    return template('register', form=form)

@post('/registrarse')
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
        if request.POST.pago:
            clientes.cobrar_miembro(new3)
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

@post('/inicio')
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
                    valor_madre = email
                    return redirect('/pagina_piloto')
                else:
                    valor_madre = email
                    return redirect('/pagina_espectadores')
            else:
                return "eorror"

        return "error"

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
        if tipo_cliente == 1:
            event.insert_cliente(nombre, apellidos, dni, telefono, email, cod_evento)
        redirect('/events/user')

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

@post('/new_moto_client')
def new_reserva_moto():
    if valor_madre != "None":
        tipo_miembro = clientes.tipo_miembro(valor_madre)
        cod_moto = motos.get_cod_moto()
        if request.POST.keeway:
            cod_moto = motos.get_cod_moto("keeway")
            motos.añadir_reserva(valor_madre,cod_moto)
        if request.POST.keeway:
            cod_moto = motos.get_cod_moto("keeway")
            motos.añadir_reserva(valor_madre,cod_moto)
        if request.POST.keeway:
            cod_moto = motos.get_cod_moto("keeway")
            motos.añadir_reserva(valor_madre,cod_moto)
    return redirect('/inicio')

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

@get('/reservar/<no:int>')
def reservar(no):
    cur_data = event.get_event(no)
    return template('reservar_evento', old=cur_data, no=no)

@post('/reservar/<no:int>')
def edit_item(no):
    if request.POST.reservar_confirmar:
        if valor_madre != "None":
            tipo_miembro = clientes.tipo_miembro(valor_madre)
            if tipo_miembro == 1:
                clientes.añadir_reserva(valor_madre,no)
            else:
                clientes.añadir_reserva(valor_madre,no)
                clientes.cobrar_entrada(valor_madre,no)
        return redirect('/inicio')

@get('/participar/<no:int>')
def participar(no):
    cur_data = event.get_event(no)
    return template('edit_event', old=cur_data, no=no)

@post('/participar/<no:int>')
def edit_item(no):
    if request.POST.participar_confirmar:
        if valor_madre != "None":
            conf_piloto = clientes.espectador_o_piloto(valor_madre)
            if conf_piloto == "Piloto":
                clientes.añadir_participante(valor_madre,no)
                clientes.cobrar_piloto(valor_madre,no)
            else:
                return ("Usted no es piloto")
        return redirect('/inicio')

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

