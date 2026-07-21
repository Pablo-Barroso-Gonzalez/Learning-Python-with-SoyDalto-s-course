diccionario = {
    "edad" : 16,
    "nombre" : "Pablo",
    "primer_apellido0" : "Barroso"
}
#Muestra las claves del diccionario.
print("Todas las claves del diccionario son:")
claves = diccionario.keys()
print(claves)

#Devuelve el valor de la `<clave>` q le pasemos.
mi_nombre = diccionario.get("nombre")
print(mi_nombre)
print(diccionario)
#Eliminando un elemento de la lista
diccionario.pop("edad","nombre")
print(diccionario)

diccionario.clear()
print(diccionario)