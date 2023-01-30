#importando un modulo y asignando el nombre "m_saludar"
#import module_saludar as m_saludar

#desde ese module, importamos dos funciones
from modulo_saludar import saludar,saludar_raro

#creamos las variables con los saludos
saludo = saludar("carlos")
saludar1 = saludar_raro("pepito")

#mostramos los resultados
print(saludo)
print(saludar1)