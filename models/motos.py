import sqlite3
from models.clientes import Clientes

class Motos:
    def __init__(self, database):
        self.database = database
    
    def __connect(self):
        conn = sqlite3.connect(self.database)
        return conn

    def añadir_reserva(self,email,cod_moto):
            cod_cliente = Clientes.get_cod_cliente(email)
            conn = self.__connect()
            c = conn.cursor()
            c.execute("INSERT INTO cliente_piloto_moto(cod_cliente,cod_moto) VALUES (?,?)", ((cod_cliente,cod_moto)))
            conn.commit()
            c.close()
            return True

    def get_cod_moto(self,nombre):
        cs = "SELECT cod_moto FROM moto WHERE nombre LIKE ?"
        conn = self.__connect()
        c = conn.cursor()
        c.execute(cs, (nombre, ))
        data = c.fetchone()
        conn.commit()
        c.close()
        return data