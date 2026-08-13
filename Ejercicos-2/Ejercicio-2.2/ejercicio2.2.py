"""
Creacion de una funcion que al pasarle un numero nos genere numeros primos primos hasta llegar a ese numero.
"""
#Vamos a intentar hacer q creo q entedi ahora mejor

def es_primo(input_num):
    for numero in range(2, input_num):
        if input_num % numero == 0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3, num + 1):
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)
    return primos

print("--- CALCULADORA DE PRIMOS ---")
num = int(input("De 0 hasta el numero que indiques a continuacion:\n"))

resultado = primos_hasta(num)
print(resultado)