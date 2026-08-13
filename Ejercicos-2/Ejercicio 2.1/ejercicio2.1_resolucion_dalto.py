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

def obtener_compañeros(cantidad_compañeros):
    compañeros = []
    for i in range(cantidad_compañeros):
        nombre = input("Ingrese el nombre del compañero:\n")
        edad = input("Ingrese la edad del compañero:\n")
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x: x[1])
    print(compañeros)
    profesor = compañeros[-1][0]
    asistente = compañeros[0][0]
    return profesor,asistente

teacher, assistent = obtener_compañeros(5)
print(f"En el dia de hoy el profesor va a ser teacher {teacher} y su asistente {assistent}.")