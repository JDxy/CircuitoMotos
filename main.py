from bottle import route, run, template, request, get, post, redirect, static_file
from config.config import DATABASE
from models.events import Event

event = Event(DATABASE)

@route('/events/user')
def event_list():
    return templat
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    e('events_users', rows=event.select())

@route('/events/admin')
def event_list():
    return template('make_table', rows=event.select())

@route('/events/admin')
def event_list():
    return template('make_table', rows=event.select())

@get('/new_event')
def new_event_form():
    return template('new_event')

@get('/new_event')
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

