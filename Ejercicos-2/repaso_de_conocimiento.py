# A pasado un dia desde q he hecho los ejercios 2 y quiro hacer un repaso si despues de 24 horas me acuerdo realmente de las cosas, lo voy a hacer de pura memoria sin revisar nada.

def es_primo(num):
    for divisor in range(2, num):
        if num % divisor == 0: return False
    return True


numero = int(input("introduzca un numero:\n"))
print(f"{numero} es un numero primo?\n{es_primo(numero)}")
