# EJERCICIO 3.8 — Contar líneas de un archivo
#
# Abre "prueba.txt" y muestra por pantalla cuántas líneas contiene.
#
# Objetivo:
# Practicar el recorrido de un archivo y trabajar con la información
# obtenida de cada línea.

with open("Ejercicios/Ejercicios-3/prueba.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")
    archivo.write("Escribiendo la segunda linea.")
    
with open("Ejercicios/Ejercicios-3/prueba.txt", "r", encoding="UTF-8") as archivo:
    lineas = 0
    for linea in archivo:
        lineas += 1
print(f"El archivo prueba.txt tiene {lineas} lineas.")