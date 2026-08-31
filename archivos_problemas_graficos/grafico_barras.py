import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos/cofla_ingresos.csv")
total_ingresos = df["ingresos"].sum()
print(f"El total de ingresos es:\n{total_ingresos}")
sns.barplot(x="fuente",y="ingresos",data=df)

plt.show()