def frase(nombre, apellido, adjetivo = "Tonto"):
    return f"Mi nombre y apellido es {nombre} {apellido} y soy muy {adjetivo}."

frase_resultante = frase(adjetivo= "crack",nombre="Pablo",apellido="Barroso")
print(frase_resultante)