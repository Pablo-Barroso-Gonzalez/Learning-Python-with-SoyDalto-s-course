lista = list()
lista2 = [42,73,True,True,False,False,15,17,84,29.29,60]
print(lista2)

print(type(lista))
print(f"La lista tiene {len(lista)} elementos")

#Añadiendo elementos con los tres difrentes metodos: append,extend,insert.
lista.append(16) 
lista.extend(["Taekwondo","Ajedrez","Pablo","Barroso","UltraTech",True])
lista.insert(3, "silicon valley")
print(lista)
print("Voy a el elemento Taekwondo de la lista:")
lista.pop(1)
print(lista)

#Metodos de eliminacion de elementos: pop,remove,clear.
print("Ahora voy a eliminar el ultimo elemento de la lista:")
lista.pop()
print(lista)
print("Ahora voy a eliminar mi seudonimo de UltraTech:")
lista.remove("UltraTech")
print(lista)
print("Ahora voy a dejar vacia la lista:")
lista.clear()
print(lista)
print("Ordenado en orden descendente la lista2:")
lista2.sort(reverse=True)
print(lista2)
print("Modifcado el orden en ascendente en la lista2:")
lista2.reverse()
print(lista2)
