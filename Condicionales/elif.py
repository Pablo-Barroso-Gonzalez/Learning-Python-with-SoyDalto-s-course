nombre = "Pablo"
edad = 16
nivel = 35
victorias = 80
baneado = False

print(f"BIENVENDIO {nombre} A ESTE TORNEO\nEspere un momento q necesitamos hacer unas compobaciones")
if baneado == True:
    print("Estas baneado no puedes participar")
elif edad >= 18:
    print(f"Tu {edad} es legal para particpar.")
    if victorias >= 50:
        print("Como q tienes mas de 50 victorias pudes participar.")
        if nivel >= 30:
            print("Enhorabuena has pasado todos los filtros de seleccion corectamente.\n¡Bienvenido al torneo!")
        else:
            print("Tu nivel es demasiado bajo.")
    else:
        print("Necesitas al menos 50 victorias para participar.")

elif edad >= 16:
    print("No pudes participar en el torneo pero si puedes venir a mirar") 
        
else:
    print("Debes de ser mayor de 16 para poder participar en el torneo")   