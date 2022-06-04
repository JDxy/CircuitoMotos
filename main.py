import sqlite3
from bottle import route, run, template, request, get, post, redirect
from config.config import DATABASE

@route('/events')
def events_list():
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

        conn.commit()
        c.close()
        # se muestra el resultado de la operación
        return redirect('/events')

@get('/edit/<no:int>')
def edit_item(no):
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM eventos WHERE cod_evento = ?", (no,))
    cur_data = c.fetchone()
    return template('edit_event', old=cur_data, no=no)

@post('/edit/<no:int>')
def edit_item(no):
     if request.POST.save:
        Fecha_inicio = request.POST.Fecha_inicio.strip()
        Fecha_fin = request.POST.Fecha_fin.strip()
        Categoria = request.POST.Categoria.strip()
        Coste_participante = request.POST.Coste_participantes.strip()
        Coste_espectador = request.POST.Coste_espectadores.strip()
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("UPDATE eventos SET Fecha_inicio = ?, Fecha_fin = ?, Categoria = ?, Coste_participante = ?, Coste_espectadores = ? WHERE cod_evento LIKE ?", (Fecha_inicio, Fecha_fin, Categoria,Coste_participante,Coste_espectador,no))
        conn.commit()
        return redirect('/events')

@get('/delete/<no:int>')
def delete_item(no):
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM eventos WHERE cod_evento = ?", (str(no),))
    cur_data = c.fetchone()

    return template('delete_event', old=cur_data, no=no)


@post('/delete/<no:int>')
def delete_item(no):
    if request.POST.delete:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("DELETE FROM eventos WHERE cod_evento = ?", str(no))
        conn.commit()
        c.close()

    return redirect('/events')

if __name__ == '__main__':
   run(host='localhost', port=8080, debug=True, reloader=True)

