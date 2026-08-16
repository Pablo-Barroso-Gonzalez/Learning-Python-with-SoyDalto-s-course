archivo = open("archivos/documento2.txt")

with open("archivos/documento2.txt") as archivo:
    archivo = archivo.read()
    print(archivo)