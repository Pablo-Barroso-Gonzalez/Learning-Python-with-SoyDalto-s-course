# EJERCICIO 3.5 — Comprobar la posición del cursor
#
# Abre "prueba.txt", realiza varias operaciones de lectura y movimiento
# del cursor, y muestra por pantalla la posición del cursor en distintos
# momentos.
#
# Objetivo:
# Practicar la consulta de la posición actual del cursor.

with open("Ejercicios/Ejercicios-3/prueba.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")
    archivo.write("Escribiendo la segunda linea.")
    
with open("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    print(archivo.tell())
    archivo.read()
    print(archivo.tell())
    archivo.seek(20)
    print(archivo.tell())
    contenido_parcial = archivo.read()
print(contenido_parcial)