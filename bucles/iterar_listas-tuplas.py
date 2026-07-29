#Creando variables
animales = ("capibara","leon","tortuga","degu","hamster","mono")
numeros = (34,54,643,54,34,2,42,42,53,64)

#Bucles
for animal in animales:
    print(f"Estamos en la iteracion de el animal {animal}")
print("ya se han iterado todos los animales")

suma_numeros = 0
for numero in numeros:
    print(numero)
    suma_numeros += numero 
print(f"La suma de todos los numeros es {suma_numeros}")

alumnos = ["Juan", "Maria", "Carlos", "Ana", "Pedro", "Laura", "Miguel", "Sofia", "Diego", "Elena", "Roberto", "Carmen", "Fernando", "Lucia", "Antonio", "Isabel", "Manuel", "Rosa", "Jesus"]
notas = [8.5, 9.2, 7.8, 8.8, 9.5, 7.6, 8.9, 9.1, 8.3, 8.7, 9.0, 8.2, 7.9, 9.4, 8.8, 7.7, 8.6, 9.3, 8.1]

for alumno,nota in zip(alumnos,notas):
    print(f"{alumno} saco en el examen {nota}.")
else:
    print("Ya se entregaron todas las notas de los examenes")
    
variable = "hola buenos dias"
print(list(enumerate(variable)))

for num in range(10,100,15):
    print(num)

#Forma no optima (pero posible) de recorer una lista
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma semicorrecta de recorer una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es {indice} y el valor es {valor}.")

#La enterior es buena pero se pude hacer mejor con un desempaquetado en el propio for
for indice, valor in enumerate(numeros):
    print("-" * 40)
    print(f"El indice es {indice} y el valor es {valor}.")
    if indice == 7:
        break
else:
    print("El bucle for termino sin ningun break")