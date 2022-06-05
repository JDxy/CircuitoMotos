import sqlite3
class Event:
    def __init__(self, database):
        self.database = database
    
    def __connect(self):
        conn = sqlite3.connect(self.database)
        return conn

    def select(self):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("SELECT * FROM eventos")
        data = c.fetchall()
        conn.commit()
        c.close()
        return data
    
    def get_task(self, no):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("SELECT * FROM eventos WHERE cod_evento LIKE ?", (str(no),))
        data = c.fetchone()
        conn.commit()
        c.close()
        return data
    
    def insert_task(self, new1, new2, new3, new4, new5):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("INSERT INTO eventos(fecha_inicio,fecha_fin,categoria,coste_participante,coste_espectadores) VALUES (?,?,?,?,?)", ((new1,new2,new3,new4,new5)))
        conn.commit()
        c.close()
        return True
    
    def update(self, no, fecha_inicio, fecha_fin, categoria, coste_participante, coste_espectador):
        conn = self.__connect()
        c = conn.cursor()
        if fecha_inicio != "":
            c.execute("UPDATE eventos SET Fecha_inicio = ? WHERE cod_evento LIKE ?", (fecha_inicio,no))
            conn.commit()
            c.close()
            return True
        elif fecha_fin != "":
            c.execute("UPDATE eventos SET Fecha_fin = ? WHERE cod_evento LIKE ?", (fecha_fin,no))
            conn.commit()
            c.close()
            return True
        elif categoria != "":
            c.execute("UPDATE eventos SET categoria = ? WHERE cod_evento LIKE ?", (categoria,no))
            conn.commit()
            c.close()
            return True
        elif coste_participante != "":
            c.execute("UPDATE eventos SET coste_participante = ? WHERE cod_evento LIKE ?", (coste_participante,no))
            conn.commit()
            c.close()
            return True
        elif coste_espectador != "":
            c.execute("UPDATE eventos SET coste_espectadores = ? WHERE cod_evento LIKE ?", (coste_espectador,no))
            conn.commit()
            c.close()
            return True
        

    
    def delete(self, no):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("DELETE FROM eventos WHERE cod_evento = ?", str(no))
        conn.commit()
        c.close()
        return True