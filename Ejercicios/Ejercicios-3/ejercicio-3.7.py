with open("Ejercicios/Ejercicios-3/prueba.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")
    archivo.write("Escribiendo la segunda linea.")

with open ("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    for linea in archivo:
        print(linea)