# ===============================================================================
# EJERCICIO PRÁCTICO 2
# ===============================================================================
#
# CONSIGNAS:
# -------------------------------------------------------------------------------
# a) Pedir al usuario que ingrese un texto cualquiera y:
#    - Calcular cuánto tardaría en decir esa frase.
#    - Mostrar cuántas palabras escribió.
#
# b) Si tarda más de 1 minuto en decir la frase:
#    - Mostrar el mensaje:
#      "Para flaco, tampoco te pedí un testamento."
#
# c) Dalto habla un 30% más rápido:
#    - Calcular cuánto tardaría Dalto en decir esa misma frase.
#
# DATOS DEL PROBLEMA:
# -------------------------------------------------------------------------------
# - Se considera que una persona dice 2 palabras por segundo.
# - Dalto habla un 30% más rápido que una persona promedio.
# ===============================================================================

mensaje = input("Escriba su mesaje a continuacion:\n")
cantidad_de_palabras = len(mensaje.split(" "))
print(f"Tu mensaje contiene {cantidad_de_palabras} palabras si lo hablaras tardarias {cantidad_de_palabras / 2} segundos pero si eres dalto tardarias {cantidad_de_palabras / 2.6}")
tiempo = cantidad_de_palabras / 2
if tiempo > 60:
    print("Para flaco, tampoco te pedí un testamento.")