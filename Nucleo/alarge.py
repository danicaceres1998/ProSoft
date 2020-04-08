# Importamos la clase Servicio
from servicio import Servicio

class Alarge(Servicio):
    ''' Abstraccion del servicio Alarge '''
    # Atributo estatico
    cant_alarges = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_alarges += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'ALARGE'
