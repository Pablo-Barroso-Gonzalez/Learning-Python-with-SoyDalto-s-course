#Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos/datos.csv")
print(df)
df["edad"] = df["edad"].astype(str)
print(df["edad"][0])