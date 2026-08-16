# EJERCICIO 3.2 — Añadir contenido a un archivo
#
# Modifica el archivo "prueba.txt" para añadir una segunda línea sin borrar
# el contenido que ya existe.
#
# El archivo debe terminar conteniendo:
# "Escribiendo en el archivo de prueba."
# "Esta es la segunda línea."
#
# Después, abre el archivo en modo lectura y muestra todo su contenido por pantalla.
#
# Objetivo:
# - Practicar el modo "a" (append).
# - Entender cómo añadir contenido al final de un archivo.
# - Practicar los saltos de línea con "\n".



#Crear archivo txt o abrirlo si existe
with open ("Ejercicios/Ejercicios-3/prueba.txt","w",encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")

with open ("Ejercicios/Ejercicios-3/prueba.txt", "a", encoding="UTF-8") as archivo:
    archivo.write("Esta es la segunda linea.")

#Lo vovemos a abrir con el permiso de r de read y lo guardamos en una variable
with open ("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    contenido = archivo.read()
print(contenido)