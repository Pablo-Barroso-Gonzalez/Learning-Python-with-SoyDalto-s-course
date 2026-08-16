# EJERCICIO 3.1 — Crear y leer un archivo de texto
#
# Crea un archivo llamado "prueba.txt" (o ábrelo si ya existe) y escribe
# en él el siguiente texto:
# "Escribiendo en el archivo de prueba."
#
# Después, vuelve a abrir el archivo en modo lectura, obtén su contenido
# y muéstralo por pantalla.
#
# Objetivo:
# - Practicar el modo "w" (write).
# - Practicar el modo "r" (read).
# - Practicar .write() y .read().
# - Entender el uso de with open().

#Crear archivo txt o abrirlo si existe
with open ("Ejercicios/Ejercicios-3/prueba.txt","w",encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.")

#Lo vovemos a abrir con el permiso de r de read y lo guardamos en una variable
with open ("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    contenido = archivo.read()
print(contenido)