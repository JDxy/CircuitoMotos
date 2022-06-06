import sqlite3
class Clientes:
    def __init__(self, database):
        self.database = database

    def __connect(self):
        conn = sqlite3.connect(self.database)
        return conn

    def get_cod_cliente(self,email):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("SELECT cod_cliente FROM clientes WHERE email LIKE ?", (str(email),))
        data = c.fetchone()
        conn.commit()
        c.close()
        return data

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
        c.execute("INSERT INTO espectador(cod_cliente,miembro) VALUES (?,?)", ((email,miembro)))
        conn.commit()
        c.close()
        return True