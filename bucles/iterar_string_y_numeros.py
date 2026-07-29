string = "Hola q tal"
numeros = [10,43,3,50,25]

for letra in string:
    print(letra)

numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2)
print(numeros_duplicados)

#Pero esta es una manera mas optima
numeros_duplicados_optimizado = [x*2 for x in numeros]
print(numeros_duplicados_optimizado)