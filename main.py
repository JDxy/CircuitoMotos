import sqlite3
from bottle import route, run, template, request, get, post, redirect
from config.config import DATABASE

@route('/todo')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("select * from eventos")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


@route('/new')
def new_item_form():
    return template('new_task')

@post('/new')
def new_item_save():
    if request.POST.save:  # the user clicked the `save` button
        new1 = request.POST.Fecha_inicio.strip()    # get the task from the form
        new2 = request.POST.Fecha_fin.strip() 
        new3 = request.POST.Categoria.strip()
        new4 = request.POST.Coste_participantes.strip()
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

