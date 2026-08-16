#Crear archivo txt o abrirlo si existe
with open ("Ejercicios/Ejercicios-3/prueba.txt","w",encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.")

#Lo vovemos a abrir con el permiso de r de read y lo guardamos en una variable
with open ("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    contenido = archivo.read()
print(contenido)
