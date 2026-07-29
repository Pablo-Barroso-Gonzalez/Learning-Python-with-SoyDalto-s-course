datos = {
    "nombre" : "Pablo",
    "edad" : 16,
    "suscriptores" : 1000000, #Ojala...
    "ambicion" : True
}

#Para imprimir solo las calves:
for key in datos:
    print(key)

#Que es lo mismo que:
print("-" * 40)
for key in datos.keys():
    print(key) 

#Si quieres solo el valor:
print("-" * 40)
for key in datos.values():
    print(key) 

#Pero si quiers los dos:
print("-" * 40)
for key, value in datos.items():
    print(f"La key es {key} y el value es {value}") 

