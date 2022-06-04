from bottle import route, run, template, request, get, post, redirect
from config.config import DATABASE
from models.events import Event

event = Event(DATABASE)


@route('/events')
def event_list():
    return template('make_table', rows=event.select())

@get('/new')
def new_task_form():
    return template('new_event')

@post('/new')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        new = request.POST.task.strip()    # get the task from the form
        
        event.insert_task(new)

        return redirect('/events')

@get('/edit/<no:int>')
def edit_item_form(no):
    cur_data = event.get_task(no)  # get the current data for the item we are editing
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
        
        return redirect('/events')

@get('/delete/<no:int>')
def delete_item_form(no):
    cur_data = event.get_task(no)  # get the current data for the item we are editing
    return template('delete_event', old=cur_data, no=no)

@post('/delete/<no:int>')
def delete_item(no):
    if request.POST.delete:
        event.delete(no)

    return redirect('/events')

if __name__ == '__main__':
   run(host='localhost', port=8080, debug=True, reloader=True)

