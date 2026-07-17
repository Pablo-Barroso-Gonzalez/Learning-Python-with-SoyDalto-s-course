# Definiendo variables
cadena1 = "Hola mundo\nsean bienvenidos al script de Pablo (UltraTech)"
cadena2 = "Bienvenido maquinola"
string_listoso = "Oso,Merendar,Oro,dos"
# Convierte a mayusculas.
mayusculas = cadena1.upper()

# Convierte a minusculas.
minusculas = cadena1.lower()

# Convierte primera letra en mayuscula.
cadena1 = cadena1.capitalize()
print(cadena1)

#Buscamos una cadena en otra cadena
busqueda_find = cadena1.find("a")
print(busqueda_find)

#Buscamos una cadena en otra cadena, si no encuentra nada da una excepcion
busqueda_index = cadena1.index("a")
print(f"Index dice q la letra a esta en la posicion {busqueda_index}")

## Devulve True si todos los caracteres son numericos osino devulve False
is_numerico = cadena1.isnumeric()
print(f"Es puramente numerico?\n{is_numerico}")
is_alpha = cadena1.isalpha()
print(f"Contiene puramente letras del Alphabet?\n{is_alpha}")

# Cuenta el numero de veces q sale un coincidenica.
contar_coincidencias = cadena1.count("do")
print(contar_coincidencias)

# Cuenta cuantos caracteres tiene un cadena de texto
contrar_caracteres = len(cadena1)
print(f"Este string tiene:\n{contrar_caracteres} caracteres")


# Comprueba si una cadena comienza con
empieza_con = cadena2.startswith("a")
termina_con = cadena2.endswith("a")
print(f"La cadena2 comienza con a:\n{empieza_con}\nY termina con a:\n{termina_con}")
# Busca en el string si existe x caracter en el string y si existe lo remplaza por x.
cadena_modificada = cadena1.replace("mundo", "gente")
print(cadena_modificada)
string_lista = cadena1.split("a")
print(string_lista)
lista_random = string_listoso.split(",")
print(lista_random)
print(lista_random[3])