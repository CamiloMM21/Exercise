import pandas as pd

#uasando la funcion read_csv leer el archivo CSV
df = pd.read_csv("archivo\\datos.csv")
df2 = pd.read_csv("archivo\\datos.csv")


#obteniendo los datos de la columna nombre
nombre = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenando de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concadenando los 2 dataframes
def_concadenado = pd.concat([df,df2])

#accendiendo a la primer a las 3 primeras filas()
primeras_filas = df.head(3)

#accediendo a las últimas 3 filas con tail()
utimas_filas = df.tail(3)

#accediendo a la cantidad de la filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#acceniendo a todos los apellidos con  loc
apellidos_loc = df.loc[:,"apellido"]

#ccediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
filas_3 = df.loc[1,:]

#accediendo a filas 3 con iloc
fila_3 = df.iloc[1,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)

