#contar la cantidad de alumno de henry
#select count(*) as total from alumno

#----------------------------------------------------------------------------------------------------------------------------------------
# contar la cantidad de alumnos por cohorte
#select *  
#from alumno
#group by cohorte;    #si no le especifico la funcion asociada al groupby, me saca por defecto la primer fila

#select count(*) as total, cohorte  #count(*) me toma todas las filas
#from alumno
#group by cohorte;


#----------------------------------------------------------------------------------------------------------------------------------------
# contar la cantidad de apellidos que empiezan con la p por cohorte
#select count(*) as total_apellido_p, cohorte
#from alumno
#where apellido like 'p%'
#group by cohorte;

#----------------------------------------------------------------------------------------------------------------------------------------
# PROMEDIO DE ALUMNOS POR CARRERA
#SELECT AVG(TOTAL_ALUMNOS) FROM (
#select   count(*) as total_alumnos, ca.nombre as carrera
#from alumno a join cohorte co
#on (a.cohorte = co.idcohorte)   #simplemente, tengo que lograr que la primari key de una tabla coincida con la foreign de la otra y me termina saliendo una unica tabla. la segunda tabla se acopla a la primera
#join carrera ca
#on (co.Carrera = ca.idCarrera)   # lo mismo, hago que me coincidadn las foreign key con las primary
#group by ca.nombre) AS T ;             # agrupamos por cantidad de alumnos

#----------------------------------------------------------------------------------------------------------------------------------------
# cantidad de alumnos que tiene a cargo cada instructor
#select count(*) as total_alumnos, i.idinstructor, i.nombre, i.apellido
#from alumno a join cohorte co
#on (a.cohorte = co.idcohorte)
#join instructor i 
#on (co.instructor = i.idinstructor)
#group by i.idinstructor

#----------------------------------------------------------------------------------------------------------------------------------------
# cuantes alumnos son mas grandes en edad que el instructor
#select count(*) as total, i.nombre, i.apellido
#from alumno a join cohorte co
#on (a.cohorte = co.idcohorte)
#join instructor i 
#on (co.instructor = i.idinstructor)
#where a.fechanacimiento > i.fechanacimiento
#group by i.idinstructor;

#----------------------------------------------------------------------------------------------------------------------------------------
# hacer una consulta donde se cree una columna que sean los dias que transcurrieron desde que nacieron hasta hoy
#SELECT TIMESTAMPDIFF(year,fechanacimiento,curdate()) as dias_de_vida, concat(nombre, apellido) as nombre_alumno
#from alumno;



#----------------------------------------------------------------------------------------------------------------------------------------
# DE LOS ALUMNOS QUE SON MAS GRANDES QUE EL PROFESOR, CUAL ES EL PROMEDIO DE DIAS . POR CUANTOS DIAS SON MAS GRANDES QUE EL PROFESOR EN PROMEDIO?
#select round(avg(diferencia_edad), 2)  as prom,    instructor 
#from (
#SELECT TIMESTAMPDIFF (day,a.fechanacimiento,i.fechanacimiento) as diferencia_edad, concat(i.nombre,i.apellido) as instructor
#FROM ALUMNO A
#JOIN COHORTE CO
#ON (CO.IDCOHORTE = A.COHORTE)
#JOIN INSTRUCTOR  
#ON (CO.INSTRUCTOR = I.IDINSTRUCTOR)
#where year(i.fechanacimiento) >  year(a.fechanacimiento)  
#group by instructor) as t
#group by instructor