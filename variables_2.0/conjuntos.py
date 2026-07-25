# Probando el orden de un conjunto
conjunto = set("Buenas")
print(conjunto)
print(conjunto)
conjunto.add("Pablo")
print(conjunto)
conjunto.add("UltraTech")
print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({"Rojo","Amarillo"})
conjunto2 = {conjunto1,"Azul","Verde"}
print(f" El conjunto dos es:\n{conjunto2}")

# Superconjuntos y subconjuntos
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#Subconjunto
resultado = conjunto4.issubset(conjunto3)
print(f"Conjunto 4 es subcojunto de conjunto 3?:\n{resultado}")

#Superconjunto
resultado = conjunto4.issuperset(conjunto3)
print(f"Conjunto 4 es un superconjunto del conjunto 3?:\n{resultado}")
