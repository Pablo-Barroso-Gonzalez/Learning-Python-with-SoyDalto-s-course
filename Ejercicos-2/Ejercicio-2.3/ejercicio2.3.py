#creando funcion q muestre la serie de fibonacci desde 0 al numero dado

# Esta es mi version del scipt antes de ver la solucion de dalto con mis concimientos y con el apoyo didactico de ia con intenciones de aprendizaje.

def crear_fibonacci(limite):
    
    sucesión_Fibonacci = [0]
    
    a = 0
    b = 1
    
    while limite > a + b:
        temporal_a = a
        a = b
        b = temporal_a + b
        sucesión_Fibonacci.append(b)
    return sucesión_Fibonacci

limite = int(input(f"Introduzca el numero limite para la serie de fibonacci:\n"))

resultado = crear_fibonacci(limite)

print(f"La sucesión de Fibonacci con limite de {limite} da como resultado:\n{resultado}")