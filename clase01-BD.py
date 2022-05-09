
#? Primer paso: Tener en cuenta el modelo de negocios
#El modelado de datos es el proceso mediante el cual se definen los requisitos de negocio y se diseñan las mejores estructuras de datos para soportarlos.
#El modelo de datos es el equivalente al plano de un edificio, y representa de forma conceptual aquello que se pretende diseñar. 
# Durante cada etapa de madurez de datos que atraviesa una empresa, pueden existir distintos modelos que describan la realidad del negocio.
# En este módulo en particular nos centraremos en los inicios de un proyecto de tecnología, 
# en el cual se debe definir la estructura de la base de datos de una aplicación
# (como concepto amplio que incluye tanto apps 

#? bases de datos
#Una base de datos “es una colección de datos almacenados de forma coherente y permanente”, 
# estos datos provienen de entidades, objetos o hechos de la realidad


#? relacion entidad-relacion
#Para poder modelar la realidad y traducirla en una estructura coherente, uno de los modelos más utilizados, 
# es el modelo relacional, basado principalmente en el modelo ENTIDAD-RELACIÓN. 
# La información necesaria para su construcción se basa en el relevamiento del modelo de negocios de la organización 
# a través de entidades, atributos y relaciones
#el relevamiento del modelo de negocios de la organización a través de entidades, atributos y relaciones.<br>
#La interacción de estas entidades en la realidad con los atributos que las describen, determinan las “relaciones”


#? Que es una entidad 
#Una entidad es un "objeto" de la realidad que se puede describir a través de sus "atributos",
# a su vez cada entidad interactúa con otras entidades lo que se denomina "relación".
#Cabe destacar que tanto las entidades como sus relaciones se definen a partir del grado de relevancia que tienen para el negocio


#? Modelo Entidad-Relacion
#El modelo entidad-relación, nos permite representar estos objetos de forma visual y ordenada, 
# en el las entidades se representan con rectángulos, los atributos como elipses y 
# las relaciones con líneas y rombos que grafi el tipo de relación

#ejemplo
'''
Entidad: Alumno.<br>
Atributos: Cédula de identidad, Nombre, Apellido, Fecha de Nacimiento, Fecha de Ingreso, Carrera, ect.<br>
Relaciones: Un alumno “cursa” una cohorte.

Entidad: Cohorte.<br>
Atributos: Número, Fecha de Inicio, Carrera, ect.<br>
Relaciones: Una cohorte "pertene" a una carrera. Una cohorte "posee" alumnos.

Entidad: Carrera.<br>
Atributos: Nombre, Estado, ect.<br>
Relaciones: Una carrera "tiene" cohortes.
'''

#! Las relaciones aportan dos grandes características a una base datos, la no duplicidad y la integridad referencial
#Se representan mediante dos elementos denominados "primary key" y "foreing key"
#una primary key, es un atributo que representa de manera única e inequívoca a un elemento (registro) de la entidad
#en el caso del alumno una primary key puede ser su N° de cédula de identidad o N° de Inscripción
# Si se desea representar a ese mismo alumno en otra entidad como por ejemplo una cohorte,
# basta con incluir dentro de la tabla a la primary key como uno de sus campos, 
# quedando representando ese alumno a través de su cédula de identidad/N° de Inscripción como una Foreing Key
# una Foreing Key es generalemente una Primary Key en otra tabla.


#? cardinalidad
# Las relaciones a su vez pueden ser 1-1 (uno-uno), 1-M (uno-muchos), N-M (muchos-muchos)lo que se denomina como cardinalidad.
#En nuestro ejemplo, un alumno de Henry solo puede cursar en una cohorte, por lo que tenemos una relación de 1-1;
# esta restricción es generalmente impuesta por el modelo de negocios. En otros modelos de negocios como el de los cursos On-Demand, 
# un alumno podría hacer varios cursos a la vez por lo que la relación sería de 1-M 


#? Tipos de Datos
# Una base de datos puede guardar diferentes tipos de datos: caracteres, numéricos, fechas, texto, booleanos, decimales, etc.
#El nombre específico que se le da a un tipo de datos, varia en cada sistema de gestión de bases de datos

#[Tipos de datos en MySQL](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)
#[Tipos de datos en PostgreSQL](https://www.postgresql.org/docs/current/datatype.html)
#[Tipos de datos en SQL Server](https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver15)

#? SQL
#(Structured Query Language)
#es un lenguaje diseñado para interactuar con las bases de datos relacionales.
# SQL se subdivide a su vez entre distintos tipos de sublenguajes:

#* DDL: Data Definition Language. (CREATE, ALTER, TRUNCATE, DROP)
#* DML: Data Manipulation Language. (SELECT, INSERT, UPDATE, DELETE)
#* DCL: Data Control Language. (GRANT, REVOKE)
#* TCL: Transacition Control Language. (COMMIT, ROLLBACK)


#Todos los sistemas de gestión de bases de datos relacionales (RDMS) como MySQL, SQL Server, Oracle,
#o Postgres utilizan SQL como su lenguaje estándar.


#? LENGUAJE
#Son sentencias que permiten definir la estructura de una base de datos, esta estructura esta compuesta por “objetos” 
# (no confundir con POO en Python) que se desean gestionar. Los tipos de objetos que se pueden gestinar son: 
# bases de datos, tablas, vistas o procedimientos. Las acciones que se pueden ejecutar son CREAR, MODIFICAR o ELIMINAR. <br>

#CREATE permite crear objetos en la base de datos, incluyendo la base de datos en si misma
'''
Crear base de datos
```SQL
CREATE DATABASE henry – Crear.
ALTER DATABASE henry – Modificar.
DROP DATABASE henry – Borrar.
```

Tablas
```SQL
CREATE TABLE alumno (
cedulaIdentidad INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(20),
apellido VARCHAR(20),
fechaInicio DATE,
PRIMARY KEY (cedulaIdentidad)
)


ALTER TABLE alumno (
direccion VARCHAR(20)
)

DROP TABLE alumno
```

Vistas
```SQL
CREATE VIEW datosAlumnos AS  
SELECT *
FROM alumnos

ALTER VIEW datosAlumnos

DROP VIEW datosAlumnos
```

Procedimientos
```SQL
CREATE PROCEDURE contarAlumnos (OUT param1 INT)
     BEGIN
       SELECT COUNT(*) INTO param1 FROM alumnos;
     END

ALTER PROCEDURE contarAlumnos (OUT param1 INT)
     BEGIN
       SELECT COUNT(*) INTO param1 FROM alumnos;
     END

DROP PROCEDURE contarAlumnos

'''
#? INTRODUCCION A BASES DE DATOS
#El principal objetivo de cualquier base de datos es almacenar información, 
# pero existen otros objetivos relacionados que llevan a un desarrollados elegir una u otra.
# Las primeras bases de datos se basaron en el modelo relacional, evolucionando con el surgimiento de las redes sociales y otras aplicaciones a modelos no relacionales


#? BD On-Premise o Cloud
# ON PROMISE
# se denominan de esta manera debido a que los servidores se encuentran físicamente alojados en instalaciones pertenecientes a la organización. 
# Esto implica que tanto el crecimiento en capacidad y mantenimiento, están a la cargo de la organización
# lo que convierte en un costo significativo. En Argentina esto es muy común en bancos, debido a que la normativa les exige adoptar esta opción


#? CLOUD
# Cuando hablamos de bases de datos en la nube, se trata de servidores que pertenecen a terceros (AWS, Azure, GCP, etc.
#En este caso tanto la capacidad como el mantenimiento esta a cargo de prestador,
#En el entorno empresarial actual de rápido crecimiento, las empresas necesitan tener acceso en tiempo real a sus datos para poder tomar decisiones
# a tiempo y aprovechar las nuevas oportunidades. Por lo que las startups optan por escalar gracias a estos servicios


#?Bases de datos relaciones vs Bases de datos no relaciones
# Los datos generalemente se suelen almacenar en estructuras de filas y columnas a través de una seria de tablas, 
# esto permite para aumentar la eficacia del procesamiento y la consulta de datos. 
# Así, se puede acceder, gestionar, modificar, actualizar, controlar y organizar fácilmente los datos. 
# La mayoría de las bases de datos utilizan un lenguaje de consulta estructurada (SQL) para escribir y consultar datos.
#
#Las bases de datos NoSQL pueden estar basadas en documentos, grafos, clave-valor u otras variantes.
# Algunas de las más conocidas son Cassandra, MongoDB, Firebase o DynamoDB.
#
#Estas bases de datos están optimizadas específicamente para aplicaciones que requieren grandes volúmenes de datos, 
# baja latencia y modelos de datos flexibles, lo que se logra mediante la flexibilización de algunas de las restricciones de coherencia de datos
# en otras bases de datos


#? Bases de datos transaccionales vs Bases de datos analíticas:
#


























