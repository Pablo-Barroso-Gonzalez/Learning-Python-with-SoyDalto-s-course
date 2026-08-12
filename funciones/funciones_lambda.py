# A mi manera

#numeros = [54,345,3,23,43,23,56,32,13,73,48,27]
#numeros_pares = []
#for num in numeros:
#    if num % 2 == 0:
#        numeros_pares.append(num)
#print(numeros_pares)

#Metodo dalto normal

#numeros = [54,345,3,23,43,23,56,32,13,73,48,27]

#def es_par(num):
#    if num % 2 == 0:
#        return True

#numeros_pares = filter(es_par,numeros)
#print(list(numeros_pares))

# Metodo dalto lambda

numeros = [54,345,3,23,43,23,56,32,13,73,48,27]
numeros_pares = filter(lambda num: num % 2 == 0, numeros)
print((numeros_pares))

es_par = lambda num, num2 : (num % 2 == 0, num2 % 2 == 0)
print(es_par(5,6))

presentacion = lambda nombre,apellido,edad,genero,hobby: f"Me llamo {nombre} {apellido}, tengo {edad} años soy {genero} y mi hobby es {hobby}."
presentacion_emma = presentacion("Emma","Pérez", 16, "mujer", "el anime")
print(presentacion_emma)