import sqlite3
from bottle import route, run, template, request, get, post, redirect, static_file
import smtplib 
from email.message import EmailMessage

@route('/trabaja_con_nosotros')
def trabaja_route():
    return template('trabaja_con_mosotros')

@get("static/<filepath:path>")
def html(filepath):
    return static_file(filepath, root="static")

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.execute("SELECT * FROM todo")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

@get('/')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.execute("SELECT * FROM todo")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


@get('/new')
def new_todo_form():
    return template('new_task')


@post('/new', method="POST")
def new_todo_save():
    if request.POST.save:
        new = request.POST.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
    return redirect("/todo")

@get('/edit/<no:int>')
def edit_item(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id = ?", str(no))
    cur_data = c.fetchone()
    return template('edit_task', old=cur_data, no=no)

@post('/edit/<no:int>')
def edit_todo_save(no):
    edit = request.POST.task.strip()
    status = request.POST.status.strip()

    if status == "pendiente":
        status = 1
    else:
        status = 0
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?)", (edit, status, no))
    return redirect("/todo")

@get('/delete/<no:int>')
def delete_item(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
    cur_data = c.fetchone()

    return template('delete_task', old=cur_data, no=no)


@post('/delete/<no:int>')
def delete_item(no):
    if request.POST.delete:
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()
        c.execute("DELETE FROM todo WHERE id LIKE ?", str(no))
        conn.commit()
        c.close()

    return redirect('/todo')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)