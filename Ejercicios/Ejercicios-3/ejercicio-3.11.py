# EJERCICIO 3.11 — Filtrar líneas de un archivo
#
# Abre "prueba.txt" y muestra únicamente las líneas que contengan
# una palabra determinada.
#
# Objetivo:
# Practicar el recorrido línea por línea y la búsqueda de texto
# dentro de cada línea.

with open("Ejercicios/Ejercicios-3/prueba.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Escribiendo en el archivo de prueba.\n")
    archivo.write("Escribiendo la segunda linea.\n")
    archivo.write("El perro de mi vecino sabe abrir puertas.\n")
    archivo.write("Ayer encontré una cuchara en el bolsillo de mi chaqueta.\n")
    archivo.write("Los pingüinos probablemente serían pésimos camareros\n")
    archivo.write("Mi ordenador lleva tres días mirándome con desprecio.\n")
    archivo.write("Una nube con forma de patata cruzó el cielo.")

key_word = input("Introduzca una palabra, te devolveremos todas la frases del texto qye tengan esa palabra:\n")

with open("Ejercicios/Ejercicios-3/prueba.txt", "r",encoding="UTF-8") as archivo:
    resultado = []
    for frase in archivo:
        frase_dividida = frase.split()
        for palabra in frase_dividida:
            if palabra == key_word:
                frase = frase.strip()
                resultado.append(frase)

print(f"Las frases que salen en el texto con {key_word} son:")


for frase in resultado:
    print(f"- {frase}")