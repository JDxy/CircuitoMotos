import sqlite3
from bottle import route, run, request, template, get, post, redirect
from config.config import DATABASE
from forms.register import RegistrationForm
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
        new6 = request.POST.miembro.strip()

        clientes.insertar_cliente(new1,new2,new3,new4,new5)
        #new_id = c.lastrowid
        return redirect('/todo')

    if request.POST.save_piloto:
        new1 = request.POST.nombre.strip()
        new2 = request.POST.apellidos.strip()
        new3 = request.POST.email.strip()
        new4 = request.POST.contrasena.strip()
        new5 = request.POST.cliente_tipo.strip()
        new6 = request.POST.carreras.strip()

        clientes.insertar_cliente(new1,new2,new3,new4,new5)

        return redirect('/todo')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)

