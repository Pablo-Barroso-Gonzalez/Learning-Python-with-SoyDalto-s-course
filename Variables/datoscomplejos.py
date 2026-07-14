#Los datos complejos son un tipo de datos q sirven para alamacenar varios datos simples o otros datos complejos pero basicamente sirve para agurpar datos
#Creando una lista
lista = ["Pablo",True,1,85,"España",False]
lista[2] = "roberto"
print(lista[2])
print(lista)
#Creando una tupla
tupla = ("Pablo",True,1,85,"España",False)
print(tupla)
print(tupla[4])
# Creando un diccionario
diccionario = {
    "nombre" : "Pablo",
    "edad" : 16,
    "esta_motivado" : True,
}
print(diccionario)
print(f"Hola\nMi nombre es {diccionario['nombre']} y tengo {diccionario['edad']} años.")



