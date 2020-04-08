# Importamos la clase Servicio
from servicio import Servicio

class Reflejo(Servicio):
    ''' Abstraccion del servicio Reflejo '''
    # Atributo estatico
    cant_reflejos = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_reflejos += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'REFLEJO'
