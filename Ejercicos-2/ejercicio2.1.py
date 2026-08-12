alumnos = {}

print("Hoy no vino el profesor y necesitamos 2 alumnos uno q haga de profesor y otro de asitente.")
print("Comenzemos el proceso de selecion para hacerlo necestio q los datos de cada alumno su nombre y edad:")

cantidad_alumnos = input("Introduzca la cantidad de alumnos en la clase:\n")

for alumno in range(int(cantidad_alumnos)):
    nombre_alumno = input(f"Dime el nombre del alumno {alumno + 1}:\n")
    edad_alumno = int(input(f"Dime la edad de {nombre_alumno}:\n"))
    alumnos[nombre_alumno] = edad_alumno
    print(f"Registo de {nombre_alumno} con {alumnos[nombre_alumno]} años completado.")

for nombre_alumno, edad_alumno in alumnos.items():
    print(f"{nombre_alumno} tiene {edad_alumno}.")
alumnos_ordeanadas = sorted(alumnos.items(), key= lambda alumnos: alumnos[1])
print(alumnos_ordeanadas)

alumno_mayor_nombre, alumno_mayor_edad = alumnos_ordeanadas[-1]
alumno_menor_nombre, alumno_menor_edad = alumnos_ordeanadas[0]

print(f"El alumno {alumno_mayor_nombre} debe de ser el profesor porque es el alumno mayor con {alumno_mayor_edad} años.")

print(f"Y su asistente debe de ser {alumno_menor_nombre} porque es el menor con {alumno_menor_edad} años.")
