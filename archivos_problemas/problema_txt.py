# Tenemos dos listas con nombre y apellido una tiene nombre otra tiene apellido tenemos de escribir los datos en un archivo de texto de forma optima con un for.

nombre = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", "Miguel", "Sofía"]
apellido = ["García", "Rodríguez", "Martínez", "López", "Hernández", "González", "Pérez", "Sánchez"]

with open ("archivos_problemas_resueltos/archivo.txt","w",encoding="UTF-8") as archivo:
    for nombre,apellido in zip(nombre,apellido):
        print(f"{nombre} {apellido}")
        archivo.write(f"{nombre} {apellido}\n")