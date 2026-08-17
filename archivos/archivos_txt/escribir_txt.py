with open ("archivos/documento.txt","w") as archivo:
    archivo.write("Los perros son animales.\n")
    archivo.write("La odisea es un gran obra.\n")
    archivo.write("Los delfines son muy inteligentes.\n")

with open("archivos/documento.txt","r") as archivo:
    archivo = archivo.read()
    print(archivo)