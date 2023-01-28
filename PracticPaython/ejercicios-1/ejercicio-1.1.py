otros_cursos_min = 2.6
otros_curso_max = 7
otros_cursos_promedio = 4
curso= 1.5

#Duracion de crudos
crudo_prmedio = 5
crudo_curso = 3.5

#el restante de crudo que quedo
diferencia_con_crudo = 100 - ( curso *1000 // crudo_curso /10)

#Diferencia de duracion

diferencia_con_min = 100 - ( curso *1000 // otros_cursos_min /10)

print(f"El curso dura {diferencia_con_min}% menos que el más rapido")
print(f"El crudo es {diferencia_con_crudo}% ")