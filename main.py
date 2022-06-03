import sqlite3
from bottle import route, run, request, template, get, post
from config.config import DATABASE
from forms.register import RegistrationForm

@route('/todo')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("select * from eventos")
    result = c.fetchall()
    return str(result)

@get('/register')
def register():
    form = RegistrationForm(request.POST)
    return template('register', form=form)

@get('/edit/<no:int>')

@post('/new')
def new_item_save():
    if request.POST.save:  # the user clicked the `save` button
        new1 = request.POST.nombre.strip()    # get the task from the form
        new2 = request.POST.apellidos.strip() 
        new3 = request.POST.contrasena.strip()
        new4 = request.POST.tipo_cliente.strip()
        new5 = request.POST.Coste_espectadores.strip()

        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO eventos(fecha_inicio,fecha_fin,categoria,coste_participante,coste_espectadores) VALUES (?,?,?,?,?)", ((new1,new2,new3,new4,new5)))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        # se muestra el resultado de la operación
        return redirect('/todo')

@post('/new')
def new_item_save():
    if request.POST.save_espectador:  # the user clicked the `save` button
        new1 = request.POST.nombre.strip()    # get the task from the form
        new2 = request.POST.apellidos.strip() 
        new3 = request.POST.contrasena.strip()
        new4 = request.POST.tipo_cliente.strip()
        new5 = request.POST.Coste_espectadores.strip()

        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO clientes(fecha_inicio,fecha_fin,categoria,coste_participante,coste_espectadores) VALUES (?,?,?,?,?)", ((new1,new2,new3,new4,new5)))
        c.execute("INSERT INTO eventos(fecha_inicio,fecha_fin,categoria,coste_participante,coste_espectadores) VALUES (?,?,?,?,?)", ((new1,new2,new3,new4,new5)))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        # se muestra el resultado de la operación
        return redirect('/todo')

def new_item_save():
    if request.POST.save_piloto:  # the user clicked the `save` button
        new1 = request.POST.nombre.strip()    # get the task from the form
        new2 = request.POST.apellidos.strip() 
        new3 = request.POST.contrasena.strip()
        new4 = request.POST.tipo_cliente.strip()
        new5 = request.POST.Coste_espectadores.strip()

        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO eventos(fecha_inicio,fecha_fin,categoria,coste_participante,coste_espectadores) VALUES (?,?,?,?,?)", ((new1,new2,new3,new4,new5)))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        # se muestra el resultado de la operación
        return redirect('/todo')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)