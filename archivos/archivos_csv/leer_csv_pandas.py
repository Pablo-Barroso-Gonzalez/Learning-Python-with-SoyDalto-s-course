import pandas as pd

df1 = pd.read_csv("archivos/archivos_csv/datos.csv")
df2 = pd.read_csv("archivos/archivos_csv/datos2.csv")
df3 = pd.read_csv("archivos/archivos_csv/datos3.csv")

nombres = df1["nombre"]

nombres_ordenados_ascendentemente = df1.sort_values("edad")
nombres_ordenados_descendentemente = df1.sort_values("edad",ascending=False)

df_concatenado = pd.concat([df1,df2,df3])

primera_5_filas = df_concatenado.head()

primeras_3_filas = df_concatenado.head(3)

ultimas_5_filas = df_concatenado.tail()
ultimas_3_filas = df_concatenado.tail(3)

filas_totales, columnas_totales = df_concatenado.shape

df_info = df_concatenado.describe()

# accediendo a un elemento especifico del dataframe con loc
elemento_especificio_loc = df1.loc[3, "apellido"]
elemento_especificio_iloc = df1.iloc[3,2]

apellidos = df1.loc[:,"apellido"]
apellidos = df1.iloc[:,1]

fila2 = df1.loc[1,:]
fila2 = df1.iloc[1,:]

mayor_que_30 = df_concatenado.loc[df_concatenado["edad"]<30 ,:]

print(f"En el dataframe hay {filas_totales} filas y {columnas_totales} columnas.")
print(df1)
print(df1.__class__)
print(df1.values)
print(elemento_especificio_loc)
print(elemento_especificio_iloc)
print(f"Los apellidos son:\n{apellidos}.")
print("La fila 2 es:")
print(fila2)
print("mayores de 30:")
print(mayor_que_30)