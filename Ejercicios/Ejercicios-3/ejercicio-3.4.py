# EJERCICIO 3.4 — Leer desde una posición concreta
#
# Lee "prueba.txt" comenzando desde una posición determinada y muestra
# el contenido restante por pantalla.
#
# Objetivo:
# Practicar el desplazamiento del cursor a una posición concreta del archivo.

#Crear archivo txt o abrirlo si existe
with open ("Ejercicios/Ejercicios-3/prueba.txt","w",encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")

with open ("Ejercicios/Ejercicios-3/prueba.txt", "a", encoding="UTF-8") as archivo:
    archivo.write("Esta es la segunda linea.")

with open("Ejercicios/Ejercicios-3/prueba.txt","r", encoding="UTF-8") as archivo:
    archivo.seek(4)
    contenido = archivo.read()
print(contenido)