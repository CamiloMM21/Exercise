#creando mi propia excepción personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
      print(f"Impresionante, cometiste el siguiente error: {err}")

#lanzando mi propia excepcion
#raise MiExcepcion("jajajjaja, persona poco culta")

#manejandola
try:
    raise MiExcepcion("jajajjaj, persona póco culta")
except:
    print("Como vas a cometer ese error")