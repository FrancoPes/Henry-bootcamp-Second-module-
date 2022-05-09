#RESUMEN
#* DDL: Data Definition Language. (CREATE, ALTER, TRUNCATE, DROP)
#* DML: Data Manipulation Language. (SELECT, INSERT, UPDATE, DELETE)
#* DCL: Data Control Language. (GRANT, REVOKE)
#* TCL: Transacition Control Language. (COMMIT, ROLLBACK)

#---------------------------------------------------------------------------------------------------------------------------------------------
#SINTAXIS ORDENADA
#? SELECT ---> CAMPOS O TODOS (*)
#? FROM ---> QUE TABLA?
#? WHERE ---> FILTRO
#? GROUP BY ---> AGRUPAR POR UN CAMPO
#? HAVING ---> ES UN FILTRO SOBRE LOS CAMPOS AGRUPADOS
#? ORDER BY ---> ORDENAR POR CAMPOS DETERMINADOS
#? limit --->limite




#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#CREAR DATA BASE Y TABLA 
#?CREATE DATABASE NOMBRE

#? USE NOMBRE


#---------------------------------------------------------------------------------------------------------------------------------------------
#crear TABLAS con primary y foreing key
'''
#?create table carrera (idcarrera int not null auto_increment,
					nombre varchar (30) not null,
                    duracion int not null,
                    primary key (idcarrera)
);

#?create table alumno (idalumno int not null auto_increment,
					 id_carrera int not null,
					 nombre varchar (30) not null,
                     apellido varchar (30) not null,
                     email varchar(30) not null,
                     primary key (idalumno),
                     foreign key (id_carrera) references carrera(idcarrera)
                     
                     
);

'''

#---------------------------------------------------------------------------------------------------------------------------------------------
# insertar rows con datos 
#? INSERT INTO  carrera(nombre, duracion) values ('policia',5);    (insertamos las carreras)

#? INSERT INTO alumno(id_Carrera,Nombre,ApPaterno,ApMaterno,Email)  VALUES('7','Hector','Suarez','Costa','hsc@gmail.com');  (insertamos el nombre relacinadoa  la carrera)


#! NOTA, SE PUEDEN EXPLICITAR O NO LAS PRIMARY KEY. EN EL CASO QUE NO, EL MOTOR SE ENCARGA
#Explicita ejemplo:
#INSERT INTO alumnos (idAlumno,cedulaIdentidad,nombre,apellido,fechaNacimiento,fechaIngreso,Cohorte)
#VALUES (2,'313262855','Beverly','Gardner','2006-10-03','2019-12-04',1235)

#---------------------------------------------------------------------------------------------------------------------------------------------
# seleccionar y mostrar
#? select * from carrera   WHERE '''    (seleciconamos todo)



#---------------------------------------------------------------------------------------------------------------------------------------------
# FUNCIONES (GENERALMENTE RELACIONADO CON SELECCIONAR)

#?---> COUNT(*) CUENTA LA CANTIDAD DE REGISTROS
''' 
SELECT COUNT(*)       ----------------------------->el count(*) nos cuenta todas las filas. es lo mismoq ue contar el id
FROM ALUMNO
WHERE CARRERA = 'DATA SCIENCE'
'''

'''
select count(nombre)
from carrera
'''
#?---> avg(columna) OBTIENE EL PROMEDIO DE UNA COLUMNA QUE CUMPLA CIERTA CONDICION
''' 
SELECT COUNT(NOTAS)
FROM ALUMNO
WHERE CARRERA = 'DATA SCIENCE'
'''
#?---> MIN(COLUMNA)

#?---> MAX(COLUMNA)

#?---> DISTINCT   VA DESPUES DEL SELECT Y SIRVE PARA SACAR UN REGISTRO UNICO(NOS ELIMINA DUPLICADOS)

#---------------------------------------------------------------------------------------------------------------------------------------------
# actualizar o modificar una fila

#? UPDATE Alumno SET Nombre='Juan',Email='jgl@hotmail.com' WHERE idAlumno=2   (corrijo una row mal escrita)
'''
UPDATE alumno_nuevoc
SET mes_nacimiento = month(fechaNacimiento)
WHERE mes_nacimiento IS NULL;

'''

#? update cohorte set fechaInicio = '2022-05-16' where idCohorte = 1243        (modifico fecha)
#! ES EXTREMADAMENTE IMPORTANTE 

#---------------------------------------------------------------------------------------------------------------------------------------------
# borrarar una fila

#? DELETE FROM carrera  WHERE idCarrera=2
#? DELETE FROM carrera  WHERE xxx is null
#? DELETE FROM carrera  WHERE IDCARRERA <> null   ----> DISTINTO
#! SIEMPRE EL WHERE, DE OTRA FORMA NOS BORRA TODO
#? delete from cohorte where idcohorte between 1245 and 1246
#? truncate table (borra todos los registros)
#---------------------------------------------------------------------------------------------------------------------------------------------
# operadores logicos (en el where o groupby o having) --- > update, delete, select
#? and (se cumplen ambas condiciones)
#? or (se cumple uno o dos)
#? xor (cumple el primer filtro pero no el segundo)
#? not (donde no se cumple)
#? in (tengo que poner una lista ('peru; 'colombia'))
#? like 'lic%a'  ---> me sirve cuando no recuerdo una palabra pero se las iniciales y/o una letra final
#? between 3 and 5 (ambos incluyentes)
#---------------------------------------------------------------------------------------------------------------------------------------------
# DATETIME

#? CURRENT_TIMESTAMP()   ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
#? YEAR(CURDATE())  ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
'''
select * from alumno
group by year(fechaingreso)
'''
''' 
select count(*) from alumno
group by year(fechaingreso)
'''

#? DATE_FORMAT(NOW, "%H:%I:%S")  ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
#? CURDATE()  ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
#? and year(fechaIngreso) = tanto -----> me saca el anio de una fecha
#---------------------------------------------------------------------------------------------------------------------------------------------
# operadores aritmeticos  (+ - / *)

#? select  nombredelproducto, col1 + col2 as total
#?from productos




#---------------------------------------------------------------------------------------------------------------------------------------------
# WHERE

#-----> ES UN FILTRO SOBRE COLUMNAS



#---------------------------------------------------------------------------------------------------------------------------------------------
# GROUPBY

#-----> NOS AGRUPA POR COLUMNAS
'''
select cohorte, count(*)  #-----> NOS AGRUPA POR COLUMNA cohorte y me cuenta los alumnos de cada uno
from alumno
group by cohorte

'''

#---------------------------------------------------------------------------------------------------------------------------------------------
# HAVING 

#-----> ES UN FILTRO SOBRE COLUMNAS, GENERALMENTE DESPUES DEL WHERE (SON MUY PARECIDOS)


'''
select count(*) as cantidad, year (fechaingreso)
from alumno
group by year(fechaingreso)
having count(*) > 20              ----> anios donde entraron mas de 20 alumnos a henry
'''
#---------------------------------------------------------------------------------------------------------------------------------------------
# orden by

#? orden by column2 asc ---> ordena una consulta, por la columna1 de acsendente
#? orden by  column1 desc ---> ordena una consulta, por la columna1 de forma decendete

''' 
select nombre, apellido
from alumno 
ORDER BY fechaIngreso ASC
LIMIT 1                           #-----> me saca solo la primer fila
'''

#---------------------------------------------------------------------------------------------------------------------------------------------
# agregar una columna, borrar una y otras funciones del ALTER
#? alter table xxx
#? ADD COLUMN columnxx varcahr(20)  ---> anadir columnaS

#? alter table xxx
#? alter COLUMN columnxx varcahr(20)  ---> alterar los tipos de datos

#? alter table xxx
#? alter COLUMN columnxx varcahr(20)  ---> alterar los tipos de datos

#? alter table xxx
#? drop COLUMN columnxx   ---> borrar columna

#? truncate table ccc

#?ALTER TABLE Books;
#?RENAME COLUMN BID TO BooksID;

#---------------------------------------------------------------------------------------------------------------------------------------------
# renombrar tabla
#? rename table xxx to ccc





#---------------------------------------------------------------------------------------------------------------------------------------------
# consultas

#select nombre, apellido, cedulaidentidad, fechaingreso 
#from alumno
#where cohorte = 1243


#---------------------------------------------------------------------------------------------------------------------------------------------
# join

# join de a dos
#? select tabla1.columnx, tabla2.columna2    (una vez que hice el join puedo poner tablar de ambos)
#? from tabla1  (generalmente se pone un alia con AS)
#? join tabla2   
#? on tabla1.pk = tabla2.fk (pongo las tablas en comun)
#?
'''
select   i.cedulaIdentidad,
		i.nombre,
        i.apellido,
        i.fechaNacimiento,
        i.fechaIncorporacion,
        co.carrera
from instructor i join cohorte co
on (i.idInstructor = co.instructor)
where i.nombre like 'L%';

'''

# join de a tres
#? select tabla1.columnx, tabla2.columna2    (una vez que hice el join puedo poner tablar de ambos)
#? from tabla1  (generalmente se pone un alia con AS)
#? join tabla2   
#?      on tabla1.pk = tabla2.fk (pongo las tablas en comun)
#?   join tabla3
#?      on (tabla2. = tabla3.)

# Ejemplo
'''
select   i.cedulaIdentidad,
		i.nombre,
        i.apellido,
        i.fechaNacimiento,
        i.fechaIncorporacion,
        co.carrera
from instructor i join cohorte co
on (i.idInstructor = co.instructor)
join carrera ca
on (co.Carrera = ca.idCarrera)
where ca.nombre = 'Full Stack Developer';
'''

# otro ejemplo
'''
select count(*) as cant,ca.nombre
from instructor i join cohorte co
on (i.idInstructor = co.instructor)
join carrera ca
on (co.carrera = ca.idCarrera)
group by ca.nombre

'''
#---------------------------------------------------------------------------------------------------------------------------------------------
# left 

'''
SELECT count(*) cant_alumno, left(fechaingreso,4) anioingreso
from alumno        ##---------------->   me muestra los primeros 4 caracteres
group by year(fechaingreso)
'''


#---------------------------------------------------------------------------------------------------------------------------------------------
# like 
'''
select * from alumno
where nombre like 'c%';


'''

#---------------------------------------------------------------------------------------------------------------------------------------------
# crear tabla apartir de otra

'''
CREATE TABLE alumno_nuevoC as
(SELECT * FROM alumno where nombre like 'c%');

'''

#---------------------------------------------------------------------------------------------------------------------------------------------
# MAS FUNCIONES DE FECHA
# https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html

#? CURRENT_TIMESTAMP()   ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
#? YEAR(CURDATE())  ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
'''
select * from alumno
group by year(fechaingreso)
'''
''' 
select count(*) from alumno
group by year(fechaingreso)
'''

#? DATE_FORMAT(NOW, "%H:%I:%S")  ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
#? CURDATE()  ---> PONER TAL CUAL ESTA, COMO DATO CUANDO INSERTAMOS UNA NUEVA FILA
#? and year(fechaIngreso) = tanto -----> me saca el anio de una fecha
#? timediff(month, fecha1, fecha2)  ------> could be minutes or years


#? select CURDATE()  ----> me saca la fecha de hoy

#? SELECT TIMESTAMPDIFF(DAY,fechanacimiento,curdate()) as dias_de_vida, concat(nombre, apellido) as nombre_alumno
#? from alumno;   ---------> cuantos dias trancurrieron desde su nacimiento hastan hoy


#SELECT TIMESTAMPDIFF(year,fechanacimiento,curdate()) as dias_de_vida, concat(nombre, apellido) as nombre_alumno  ----> ver la edad
# from alumno;

#---------------------------------------------------------------------------------------------------------------------------------------------
# CREAR UNA CONSULTA APARTIR DE OTRA CONSULTA

#CONSULTA: PROMEDIO DE ALUMNOS POR CARRERA
#?SELECT AVG(TOTAL_ALUMNOS) FROM (
#?select   count(*) as total_alumnos, ca.nombre as carrera
#?from alumno a join cohorte co
#?on (a.cohorte = co.idcohorte)   #simplemente, tengo que lograr que la primari key de una tabla coincida con la foreign de la otra y me termina saliendo una unica tabla. la segunda tabla se acopla a la primera
#?join carrera ca
#?on (co.Carrera = ca.idCarrera)   # lo mismo, hago que me coincidadn las foreign key con las primary
#?group by ca.nombre) AS T ;             # agrupamos por cantidad de alumnos


#select round(avg(diferencia_edad), 2)  as prom,    instructor 
#from (
#SELECT TIMESTAMPDIFF (day,a.fechanacimiento,i.fechanacimiento) as diferencia_edad, concat(i.nombre,i.apellido) as instructor
#FROM ALUMNO A
#JOIN COHORTE CO
#ON (CO.IDCOHORTE = A.COHORTE)
#JOIN INSTRUCTOR  I
#ON (CO.INSTRUCTOR = I.IDINSTRUCTOR)
#where year(i.fechanacimiento) >  year(a.fechanacimiento)  
#group by instructor) as t
#group by instructor













