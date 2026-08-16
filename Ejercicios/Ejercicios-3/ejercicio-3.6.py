# EJERCICIO 3.6 — Sobrescribir una parte de un archivo
#
# Modifica "prueba.txt" para reemplazar una parte concreta de su contenido.
# El resto del contenido debe mantenerse sin cambios.
#
# Objetivo:
# Practicar la escritura en una posición concreta del archivo.

with open("Ejercicios/Ejercicios-3/prueba.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")
    archivo.write("Escribiendo la segunda linea.")

with open("Ejercicios/Ejercicios-3/prueba.txt", "r+", encoding="UTF-8") as archivo:
    contenido = archivo.read()
    archivo.seek(30)
    contenido_puntero_movido = archivo.read()
    archivo.seek(30)
    archivo.write("rene")
    archivo.seek(0)
    contendio_modificado = archivo.read()

print(f"Este es el contenido original del archivo:\n{contenido}\nEste es el contenido despues de moverlo a la posicion 30{contenido_puntero_movido}\nY este es el contenido al final despues de sustituir una parte del texto:\n{contendio_modificado}")


    