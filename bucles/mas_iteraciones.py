frutas = ["manzana","pera","ciruela","melocoton","sandia","melon"]

for fruta in frutas:
    if fruta == "ciruela":
        continue
    print(f"Me he comido una {fruta}")

print("-" * 40)

for fruta in frutas:
    print(f"Has comido una {fruta}")
    if fruta == "melocoton":
        print("Ya no puedes comer mas frutas porque has comido una melocoton.")
        break
else:
    print("El bucle a terminado sin break")
