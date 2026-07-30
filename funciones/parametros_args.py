def suma(nombre,*numeros):
    suma_total = sum(numeros)
    return f"{nombre} el total de tu suma es {suma_total}."
resultado = suma("Pablo",43,23,46,32,32,74,64,12,32)
print(resultado)