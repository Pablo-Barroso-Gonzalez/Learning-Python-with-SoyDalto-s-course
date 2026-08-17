import csv

with open ("archivos/archivos_csv/datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)