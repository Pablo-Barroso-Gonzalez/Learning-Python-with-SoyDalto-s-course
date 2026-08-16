# EJERCICIO 3.9 — Contar palabras de un archivo
#
# Abre "prueba.txt" y muestra por pantalla cuántas palabras contiene en total.
#
# Objetivo:
# Practicar el procesamiento del contenido de un archivo.

with open("Ejercicios/Ejercicios-3/prueba.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")
    archivo.write("Escribiendo la segunda linea.")

with open("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    contenido = archivo.read()
    palabras = (len(contenido.split()))
print(f"Esta archivo .txt contiene {palabras} palabras.")