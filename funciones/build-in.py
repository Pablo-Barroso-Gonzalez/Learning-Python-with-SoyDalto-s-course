
from numpy import number


numbers = [34,12,32,85,23,53,63,46,52,73,52,93,21]

numero_mas_alto = max(numbers)
numero_mas_bajo = min(numbers)

print(f"El numero mas bajo de la lista es {numero_mas_bajo} y el mas alto es {numero_mas_alto}.")

resultado_bool = bool(None or 0 or "" or [] or False) #Devuelve False
resultado_bool2 = bool("Cualquir otra cosa") #Devuelve True
print(resultado_bool)
print(resultado_bool2)

all_resultado = all([[], None, 0, False])
all_resultado2 = all([[["Solo recore el primer del iterable igualmente q contega un elemento vacio de segundo nivel lo detecta como objeto y da true"]]])

print(f"El restulado de la funcion all() es {all_resultado}.")
print(f"El restulado de la segunda funcion all() es {all_resultado2}.")

numbers.append(200)
print(numbers)

sum_numbers = sum(numbers, 100) #Si no pones ,numero_inicial_suma por defecto es 0 y es opcional ponerlo
print(sum_numbers)