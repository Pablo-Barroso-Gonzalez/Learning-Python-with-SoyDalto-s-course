#creando funcion q muestre la serie de fibonacci desde 0 al numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    
    for i in range(num):
        print(a,b)
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b, a + b
            

resultado = fibonacci(20)
print(resultado)