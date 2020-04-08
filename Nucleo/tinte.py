# Importamos la clase Servicio
from servicio import Servicio

class Tinte(Servicio):
    ''' Abstraccion del servicio Tinte '''
    # Atributo estatico
    cant_tintes = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_tintes += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'TINTE'