# EJERCICIO 3.10 — Buscar información en un archivo
#
# Abre "prueba.txt" y comprueba si contiene una palabra determinada.
# Muestra por pantalla si la palabra aparece o no en el archivo.
#
# Objetivo:
# Practicar la búsqueda de información dentro del contenido de un archivo.


with open("Ejercicios/Ejercicios-3/prueba.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")
    archivo.write("Escribiendo la segunda linea.")

search_word = input("introduzca una palabra para buscar en el texto:\n")

with open ("Ejercicios/Ejercicios-3/prueba.txt","r",encoding="UTF-8") as archivo:
    contenido = archivo.read()
    lista_palabras = contenido.split()
    resultado = False
    for palabra in lista_palabras:
        if palabra == search_word:
            resultado = True
            break

            
if resultado:
    print(f"La palabra {search_word} esta en el texto.")
else:
    print(f"La palabra {search_word} no aparece en el texto.")