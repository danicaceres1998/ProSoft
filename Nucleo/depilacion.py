# Importamos la clase Servicio
from servicio import Servicio

class Depilacion(Servicio):
    ''' Abstraccion del servicio Depilacion '''
    # Atributo estatico
    cant_depilaciones = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)        
        self.__class__.cant_depilaciones += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'DEPILACION'
