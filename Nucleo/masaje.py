# Importamos la clase Servicio
from servicio import Servicio

class Masaje(Servicio):
    ''' Abstraccion del servicio Masaje '''
    # Atributo estatico
    cant_masajes = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_masajes += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'MASAJE'
