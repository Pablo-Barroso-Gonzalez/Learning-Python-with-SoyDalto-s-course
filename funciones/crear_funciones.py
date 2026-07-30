def saludar(nombre,genero):
    genero = genero.lower()
    
    if genero == "hombre":
        adjetivo = "rey"
        
    elif genero == "mujer":
        adjetivo = "diva"
    
    else:
        adjetivo = "amor"
        
    print(f"Hola {nombre}, mi {adjetivo} que tal.")
 
saludar("Pablo","hombre")
saludar("Emma","MUjer")
saludar("Camila","binario")

def generar_contraseña(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    primer_digito = int(numero_entero[0])
    char1 = (primer_digito - 2) % len(chars)
    char2 = (primer_digito) % len(chars)
    char3 = (primer_digito + 3) % len(chars)
    char4 = (primer_digito + 7) % len(chars)
    
    contraseña = (
        f"{chars[char1]}"
        f"{chars[char2]}"
        f"{chars[char3]}"
        f"{chars[char4]}"
        )
    
    return contraseña,num


password, num = generar_contraseña(654)
print(f"La contraseña genereada a partir de {num} es {password}.")