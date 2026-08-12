"""
EJERCICIO: Selección de profesor y asistente

Hoy el profesor no ha venido a clase y necesitamos seleccionar a dos
alumnos para desempeñar los siguientes roles:

- El alumno de mayor edad será el profesor.
- El alumno de menor edad será el asistente.

Para ello, el programa debe:

1. Preguntar cuántos alumnos hay en la clase.
2. Pedir el nombre y la edad de cada alumno.
3. Guardar los datos de los alumnos en un diccionario.
4. Mostrar los alumnos registrados.
5. Ordenar los alumnos según su edad.
6. Seleccionar al alumno de mayor edad como profesor.
7. Seleccionar al alumno de menor edad como asistente.
8. Mostrar el resultado final indicando quién desempeñará cada función.
"""

alumnos = {}

print("Hoy no vino el profesor y necesitamos 2 alumnos uno q haga de profesor y otro de asitente.")
print("Comenzemos el proceso de selecion para hacerlo necestio q los datos de cada alumno su nombre y edad:")

cantidad_alumnos = int(input("Introduzca la cantidad de alumnos en la clase:\n"))

for alumno in range(cantidad_alumnos):
    nombre_alumno = input(f"Dime el nombre del alumno {alumno + 1}:\n")
    edad_alumno = int(input(f"Dime la edad de {nombre_alumno}:\n"))
    alumnos[nombre_alumno] = edad_alumno
    print(f"Registo de {nombre_alumno} con {alumnos[nombre_alumno]} años completado.")

for nombre_alumno, edad_alumno in alumnos.items():
    print(f"{nombre_alumno} tiene {edad_alumno}.")
alumnos_ordenados = sorted(alumnos.items(), key= lambda alumno: alumno[1])
print(alumnos_ordenados)

alumno_mayor_nombre, alumno_mayor_edad = alumnos_ordenados[-1]
alumno_menor_nombre, alumno_menor_edad = alumnos_ordenados[0]

print(f"El alumno {alumno_mayor_nombre} debe de ser el profesor porque es el alumno mayor con {alumno_mayor_edad} años.")

print(f"Y su asistente debe de ser {alumno_menor_nombre} porque es el/la menor con {alumno_menor_edad} años.")
