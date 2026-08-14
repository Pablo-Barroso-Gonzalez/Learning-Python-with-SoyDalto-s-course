# ===============================================================================
# EJERCICIO PRÁCTICO 1
# ===============================================================================
#
# DATOS DEL PROBLEMA:
# -------------------------------------------------------------------------------
# 1. Duración de los videos finales (editados):
#    - Curso más rápido (Mínimo): 2.5 horas
#    - Este curso: 1.5 horas
#    - Promedio de otros cursos: 4 horas
#    - Curso más lento (Máximo): 7 horas
#
# 2. Duración del material grabado sin editar (crudo):
#    - Crudo del promedio de otros cursos: 5 horas
#    - Crudo de este curso: 3.5 horas
#
# CONSIGNAS:
# -------------------------------------------------------------------------------
# a) Diferencia en porcentaje entre el curso actual y:
#    - El más rápido de otros cursos.
#    - El más lento de otros cursos.
#    - El promedio de los cursos.
#
# b) Porcentaje de material inservible que se reduce en:
#    - El promedio de los cursos.
#    - El curso actual (este curso).
#
# c) Ver 10 horas de este curso:
#    - ¿A cuántas horas de otros cursos equivale?
#    - ¿Y al revés?
# ===============================================================================

#Difinir variables
duracion_h_curso_min = 2.5
duracion_h_curso_actual = 1.5
duracion_h_curso_promedio = 4.0
duracion_h_curso_max = 7
#crudos
duracion_h_curso_crudo_promedio = 5
duracion_h_curso_crudo_actual = 3.5

#a)
print("-------------------------------------------------------")
print("EJERCICIO A")
diferencia_actual_con_min = (1 - duracion_h_curso_actual / duracion_h_curso_min) * 100
diferencia_actual_con_promedio = (1 - duracion_h_curso_actual / duracion_h_curso_promedio) * 100
diferencia_actual_con_max = (1 - duracion_h_curso_actual / duracion_h_curso_max) * 100
print("Diferencia del curso actual con otros cursos es:")
print(f"Diferencia con el min: {diferencia_actual_con_min:.2f}%")
print(f"Diferencia con el promedio: {diferencia_actual_con_promedio:.2f}%")
print(f"Diferencia con el max: {diferencia_actual_con_max:.2f}%")

#b)
print("-------------------------------------------------------")
print("EJERCICIO B ")
diferencia_bruto_con_neto_actual = (1 - duracion_h_curso_actual / duracion_h_curso_crudo_actual) * 100
diferencia_bruto_con_neto_promedio = (1 - duracion_h_curso_promedio / duracion_h_curso_crudo_promedio) * 100

print("La diferencia de la version bruta a la la limpia (editada):")
print(f"Diferencia con el actual: {diferencia_bruto_con_neto_actual:.2f}% menos al editar el video.")
print(f"Diferencia con el promedio: {diferencia_bruto_con_neto_promedio:.2f}% menos al editar el video.")
#c)
print("-------------------------------------------------------")
print("EJERCICIO C")

# Factor de equivalencia
factor_equivalencia = duracion_h_curso_promedio / duracion_h_curso_actual
factor_equivalencia_inverso = duracion_h_curso_actual / duracion_h_curso_promedio

# Equivalencias
equivalente_otros_cursos = 10 * factor_equivalencia
equivalente_curso_actual = 10 * factor_equivalencia_inverso

print("Equivalencia entre cursos:")
print(f"10 horas de este curso equivalen a {equivalente_otros_cursos:.2f} horas de otros cursos.")
print(f"10 horas de otros cursos equivalen a {equivalente_curso_actual:.2f} horas de este curso.")