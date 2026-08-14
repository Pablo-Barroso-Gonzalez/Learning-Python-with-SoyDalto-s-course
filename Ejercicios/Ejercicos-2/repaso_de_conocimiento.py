# A pasado un dia desde q he hecho los ejercios 2 y quiro hacer un repaso si despues de 24 horas me acuerdo realmente de las cosas, lo voy a hacer de pura memoria sin revisar nada.

def es_primo(num):
    for divisor in range(2, num):
        if num % divisor == 0: return False
    return True


numero = int(input("introduzca un numero:\n"))
resultado = es_primo(numero)
if resultado == True:
    print(f"El numero {numero} es primo.")
else:
     print(f"El numero {numero} no es primo.")