import sqlite3
import string
class Clientes:
    def __init__(self, database):
        self.database = database

    def __connect(self):
        conn = sqlite3.connect(self.database)
        return conn

    def get_cod_cliente(self,email):
        cs = "SELECT cod_cliente FROM clientes WHERE email LIKE ?"
        conn = self.__connect()
        c = conn.cursor()
        c.execute(cs, (email, ))
        data = c.fetchone()
        conn.commit()
        c.close()
        return str(data)

    def insertar_cliente(self,new1,new2,new3,new4,new5):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("INSERT INTO clientes(nombre,apellidos,email,contrasena,tipo_cliente) VALUES (?,?,?,?,?)", ((new1,new2,new3,new4,new5)))
        conn.commit()
        c.close()
        return True

    def insertar_espectadores(self,email,miembro):
        conn = self.__connect()
        c = conn.cursor()
        codigo = self.get_cod_cliente(email)
        coma = codigo.index(",")
        codigo_num = codigo[1:coma]
        print(codigo)
        c.execute("INSERT INTO espectador(cod_cliente,miembro) VALUES (?,?)", ((codigo_num, miembro)))
        conn.commit()
        c.close()
        return True

    def espectador_o_piloto(self,email_):
        conn = self.__connect()
        sd = "select tipo_cliente from clientes where email = ?;"
        c = conn.cursor()
        c.execute(sd, (email_,))
        data = c.fetchall()
        conn.commit()
        c.close()
        return data

    def validar_email(self,email_):
        data = 0
        sd = "select cod_cliente from clientes where email = ?;"
        conn = self.__connect()
        c = conn.cursor()
        c.execute(sd, (email_,))
        data = c.fetchone()
        conn.commit()
        c.close()
        print(data)
        if data == None:
            return "error"
        return "true"

    def validar_contrasena(self,email,contrasena):
        data = 0
        sd = "select cod_cliente from clientes where email = ? and contrasena = ?;"
        conn = self.__connect()
        c = conn.cursor()
        c.execute(sd, (email, contrasena))
        data = c.fetchone()
        conn.commit()
        c.close()
        if data == None:
            return "false"
        else:
            return "true"
