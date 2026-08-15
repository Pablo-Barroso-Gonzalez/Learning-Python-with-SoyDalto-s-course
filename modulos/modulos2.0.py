import sys

#print(sys.builtin_module_names)

print(sys.path) 

sys.path.append("/home/alumne/Desktop/Informatica/Curso python DALTO/modulos/funciones_buenas")

print(sys.path)

import saludar as modulo_saludo


print(modulo_saludo.saludar_raro("Emma"))