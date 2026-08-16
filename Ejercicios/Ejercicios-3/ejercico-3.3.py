# EJERCICIO 3.3 — Volver a leer un archivo
#
# Lee el contenido de "prueba.txt" dos veces y muestra ambas lecturas por pantalla.
# Entre ambas lecturas, consigue que la segunda comience desde el principio del archivo.
#
# Objetivo:
# Practicar la lectura de un archivo y el manejo de la posición de lectura.

with open("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    contendio = archivo.read()
print(contendio)
    
    
with open("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    contendio2 = archivo.read()
print(contendio2)