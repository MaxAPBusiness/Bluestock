/*Crea la tabla de alumnos con los campos id (PK), DNI, nombre, apellido e email*/
CREATE TABLE IF NOT EXISTS ALUMNOS(
    ID INTEGER PRIMARY KEY,
    DNI INTEGER UNIQUE NOT NULL,
    NOMBRE_APELLIDO VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(100)
);

/*Crea la tabla de herramientas con los campos id (PK), descripción, cantidad en condiciones,
cantidad en reparación, cantidad de baja, id de grupo e id de subgrupo.*/
CREATE TABLE  IF NOT EXISTS HERRAMIENTAS(
    ID INTEGER PRIMARY KEY,
    DESC_LARGA VARCHAR(100) NOT NULL,
    CANT_CONDICIONES INTEGER,
    CANT_REPARACION INTEGER,
    CANT_BAJA INTEGER,
    ID_GRUPO VARCHAR(50),
    ID_SUBGRUPO VARCHAR(50)
);

/*Crea la tabla de profesores con los campos id (PK) y nombre y apellido*/
CREATE TABLE IF NOT EXISTS  PROFESORES(
    ID INTEGER PRIMARY KEY,
    NOMB_APELLIDO VARCHAR(100) NOT NULL
);

/*Crea la tabla de alumnos con los campos id (PK), fecha, alumno, nombre y apellido y email*/
CREATE TABLE IF NOT EXISTS  TURNO_PANOL(
    ID INTEGER PRIMARY KEY,
    FECHA VARCHAR(12),
    ID_ALUMNO INTEGER,
    HORA_INGRESO VARCHAR(12),
    HORA_EGRESO VARCHAR(12),
    PROF_INGRESO INTEGER,
    PROF_EGRESO INTEGER,
    FOREIGN KEY (ID_ALUMNO) REFERENCES ALUMNOS(ID),
    FOREIGN KEY (PROF_INGRESO) REFERENCES PROFESORES(ID),
    FOREIGN KEY (PROF_EGRESO) REFERENCES PROFESORES(ID)
);

/*Crea la tabla de movimiento de herramientas con los campos id_herramienta, id_alumno, fecha, cantidad, 
tipo (ingreso o devolución y el id del turno del pañol.*/
CREATE TABLE IF NOT EXISTS  MOVIMIENTOS_HERRAMIENTAS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_HERRAMIENTA INTEGER,
    ID_ALUMNO INTEGER,
    FECHA VARCHAR(12),
    CANTIDAD INTEGER,
    TIPO VARCHAR(50),
    ID_TURNO_PANOL INTEGER,
    FOREIGN KEY(ID_ALUMNO) REFERENCES ALUMNOS(ID),
    FOREIGN KEY(ID_HERRAMIENTA) REFERENCES HERRAMIENTAS(ID),
    FOREIGN KEY(ID_TURNO_PANOL) REFERENCES TURNO_PANOL(ID)
);

/*Crea la tabla de usuarios. Ignorar por ahora*/
CREATE TABLE IF NOT EXISTS USUARIOS(
    ID INTEGER PRIMARY KEY,
    NOMBRE_APE_ALUM VARCHAR(50) NOT NULL,
    DNI INTEGER UNIQUE NOT NULL,
    EMAIL VARCHAR(100),
    CONTRASENA VARCHAR(20)
);