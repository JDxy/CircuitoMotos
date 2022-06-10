from contextlib import redirect_stderr
from re import X
import sqlite3
class Equipos:
    def __init__(self, database):
        self.database = database

    def __connect(self):
        conn = sqlite3.connect(self.database)
        return conn

    def get_cod_equipo(self, nombre_equipo):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("SELECT cod_equipo FROM equipos WHERE nombre LIKE ?", (str(nombre_equipo),))
        data = c.fetchone()
        conn.commit()
        c.close()
        return data

    def insertar_equipo(self,new1):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("INSERT INTO equipos(nombre) VALUES (?)", ((new1)))
        conn.commit()
        c.close()
        return True

    def insertar_miembros(self,nombre_equipo,new2,new3,new4):
        conn = self.__connect()
        c = conn.cursor()
        codigo = self.get_cod_equipo(nombre_equipo)
        c.execute("INSERT INTO miembros_equipo(nombre,apellidos,ocupacion) VALUES (?,?,?)", ((new2,new3,new4)))
        conn.commit()
        c.close()
        return True

    def espectador_o_piloto(self,email):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("select tipo_piloto from equipos where email = ?"), ((email))
        data = c.fetchone()
        conn.commit()
        c.close()
        return data