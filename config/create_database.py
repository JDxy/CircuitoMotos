import sqlite3
def create_database(db_file):
    conn = sqlite3.connect(db_file) # Warning: This file is created in the current directory
    
    conn.execute("CREATE TABLE eventos (cod_evento INTEGER PRIMARY KEY AUTOINCREMENT, fecha_inicio datetime, fecha_fin datetime,  categoria varchar(25), coste_participante dec(4,2), coste_espectadores dec(4,2))")
    
    conn.execute("CREATE TABLE clientes (cod_cliente INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(20),apellidos varchar(50),pago DECIMAL(5,2),email varchar(70),contrasena varchar(30),tipo_cliente varchar(10))")
    
    conn.execute("CREATE TABLE trabajadores (cod_trabajador INTEGER PRIMARY KEY AUTOINCREMENT,nombre varchar(20),apellidos varchar(20),salario int,puesto varchar(20))")
    
    conn.execute("CREATE TABLE equipos (cod_equipo INTEGER PRIMARY KEY AUTOINCREMENT,nombre varchar(20))")
    
    conn.execute("CREATE TABLE moto (cod_moto INTEGER PRIMARY KEY AUTOINCREMENT,nombre varchar(20),tipo_moto varchar(20) not null,cilindrada varchar(8))")

    conn.execute("CREATE TABLE miembros_equipo (cod_miembro INTEGER PRIMARY KEY AUTOINCREMENT, cod_equipo int not null,nombre varchar(20),apellidos varchar(30),ocupacion varchar(25),FOREIGN KEY (cod_equipo) REFERENCES equipos(cod_equipo))")

    conn.execute("CREATE TABLE espectador (cod_espectador INTEGER PRIMARY KEY AUTOINCREMENT,cod_cliente int,miembro boolean default False,FOREIGN KEY (cod_cliente) REFERENCES clientes(cod_cliente))")

    conn.execute("CREATE TABLE espectadoresyeventos (cod_espectador INTEGER,cod_evento integer,primary KEY (cod_espectador, cod_evento),FOREIGN KEY (cod_espectador) REFERENCES espectador(cod_espectador),FOREIGN KEY (cod_evento) REFERENCES eventos(cod_evento))")

    conn.execute("CREATE TABLE cliente_piloto_moto (cod_cliente int,cod_moto int,primary KEY(cod_moto, cod_cliente),FOREIGN KEY (cod_cliente) REFERENCES clientes(cod_cliente),FOREIGN KEY (cod_moto) REFERENCES moto(cod_moto))")

    conn.execute("CREATE TABLE miembros_equipo_piloto_moto (cod_miembro int,cod_moto int,primary KEY(cod_moto, cod_miembro),FOREIGN KEY (cod_miembro) REFERENCES miembros_equipo(cod_miembro),FOREIGN KEY (cod_moto) REFERENCES moto(cod_moto))")

    conn.execute("CREATE TABLE cliente_piloto_evento (cod_cliente int,cod_evento int,primary KEY(cod_cliente, cod_evento),FOREIGN KEY (cod_cliente) REFERENCES clientes(cod_cliente),FOREIGN KEY (cod_evento) REFERENCES eventos(cod_evento))")

    conn.execute("CREATE TABLE equipo_evento (cod_equipo int,cod_evento int,primary KEY(cod_equipo, cod_evento),FOREIGN KEY (cod_equipo) REFERENCES equipos(cod_equipo),FOREIGN KEY (cod_evento) REFERENCES eventos(cod_evento))")

    conn.execute("INSERT INTO eventos(fecha_inicio,fecha_fin,categoria,coste_participante,coste_espectadores) values('2022-01-04 09:30','2022-01-05 21:00','amateur',15.00,1.00),('2022-04-01 13:30','2022-04-04 20:00','profesional',40.00,10.00),('2022-06-04 09:30','2022-06-06 21:00','amateur',15.00,1.00),('2022-06-01 10:30','2022-06-04 21:00','profesional',80.00,30.00),('2022-07-10 10:00','2022-07-12 20:00','profesional',40.00,10.00),('2022-10-13 09:30','2022-10-17 21:00','profesional',80.00,30.00),('2022-11-15 11:30','2022-11-16 19:00','amateur',15.00,1.00)")

    conn.execute("insert into clientes(nombre, apellidos, pago, email, contrasena, tipo_cliente) values('Alfredo', 'Molina', 15, 'juaanAlfredo23@gmail.com','Sinfrenosmejor1', 'Piloto'),('Alfredo', 'Molina', 15, 'juaanAlfredo23@gmail.com','Sinfrenosmejor1', 'Piloto'),('John', 'Zamora', 10, 'Pa12coJZ@gmail.com', 'Terminator99laparte', 'Espectador'),('Sara', 'Espinosa', 1,'Cobradordelcrack@gmail.com', '6NoquedaParaEmpanadas9', 'Espectador'),('Marta', 'Álvez', 80, 'Supermangoatx100@gmail.com', '23012001MG', 'Piloto'),('Marcos', 'Santana', 80,'MarcosSantanaGP@gmail.com', '467175bt26fewsjV', 'Piloto'),('Nuria', 'Sanchez', 30,'PerroSanchez@gmail.com', 'NuriasinNoria223', 'Espectador')")
    
    conn.execute("insert into trabajadores(nombre, apellidos, salario, puesto) values('Alberto', 'Salazar', 950, 'Tendero'),('Cristina', 'Albez', 950, 'Tendero'),('Pablo', 'Dominguez', 800, 'Limpiador'),('Yuleima', 'Taisma', 800, 'Limpiador'),('Lola', 'Segura', 1000, 'Mecanico'),('Paula', 'Araya', 1000, 'Mecanico'),('Roberto', 'Santana', 1000, 'Mecanico'),('Yerai', 'Espinosa', 1200, 'Ingeniero')")

    
    conn.execute("insert into equipos(nombre) values ('VinDieselFC'),('HotWheels'),('RayoMcTeam'),('MotoBrothers')")

    conn.execute("insert into moto(nombre, tipo_moto, cilindrada) values( 'BMW', 'profesional', 250),('Kawasaki', 'amateur', 150),( 'Suzuki', 'profesional', 500),( 'Kawasaki', 'amateur', 150),( 'Kawasaki', 'profesional', 500),( 'BMW', 'amateur', 250),( 'BMW', 'profesional', 250)")

    conn.execute("insert into miembros_equipo(cod_equipo, nombre, apellidos, ocupacion) values (1,'Maria', 'Garcia', 'Piloto'),(1,'Jerico', 'Santana', 'Piloto'),(2,'Shakira', 'Gonzalez', 'Piloto'),(2,'Adrian', 'Henriquez', 'Piloto'),(4,'Sebastian', 'Ramirez', 'Mecanico'),(1,'Raul', 'Heredia', 'Jefe de equipo'),(3,'Sofia', 'Collantes', 'Piloto'),(3,'Adrian', 'Mejias', 'Piloto'),(3,'Paco', 'Lopez', 'Ingeniero'),(3,'Adam', 'Morales', 'Jefe de equipo'),(4,'Peter', 'Parker', 'Jefe de equipo'),(2,'Kiko', 'Rivera', 'Jefe de equipo'),(4,'Kike', 'Montilla', 'Piloto'),(4,'Daniel', 'Sanchez', 'Piloto'),(1,'Berta', 'Robinson', 'Mecanico')")

    conn.execute("insert into espectador (cod_cliente,miembro) values(2,True),(6,False),(3,False)")

    conn.execute("insert into cliente_piloto_moto(cod_cliente, cod_moto) values (1,2),(2,4),(3,6)")

    conn.execute("insert into miembros_equipo_piloto_moto(cod_miembro, cod_moto) values (1,1),(2,5),(3,3)")

    conn.execute("insert into espectadoresyeventos(cod_espectador, cod_evento) values (1,2),(1,4),(1,5),(1,6),(2,2),(2,5),(3,4)")

    conn.execute("insert into cliente_piloto_evento values(1,7),(4,3),(5,1)")

    conn.execute("insert into equipo_evento values (1,5),(2,4),(3,2),(4,6)")

    conn.commit()