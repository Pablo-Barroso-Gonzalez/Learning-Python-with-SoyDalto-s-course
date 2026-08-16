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
    palabras = 0
    
    archivo.seek(0)
    
    for lineas in archivo:
        palabras += 1
    
    for caracter in contenido:
        if caracter == " ":
            palabras += 1
            
print(f"El numero de palabras en este texto son: {palabras}.")