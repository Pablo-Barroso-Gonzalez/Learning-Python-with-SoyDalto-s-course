"""
Creacion de una funcion que al pasarle un numero nos genere numeros primos primos hasta llegar a ese numero.
"""

def es_primo(input_num):
    for divisor in range(2, input_num):
        if input_num % divisor == 0: return False
    return True

def primos_hasta(limite):
    primos = []
    for numero in range(2, limite + 1):
        resultado = es_primo(numero)
        if resultado == True:
            primos.append(numero)
    return primos

print("--- CALCULADORA DE PRIMOS ---")
numero = int(input("De 0 hasta el numero que indiques a continuacion:\n"))

resultado = primos_hasta(numero)
print(resultado)