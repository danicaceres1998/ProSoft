# Importamos la clase Servicio
from servicio import Servicio

class Maquillaje(Servicio):
    ''' Abstraccion del servicio de Maquillaje'''
    # Atributo estatico
    cant_maquillaje = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_maquillaje += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'MAQUILLAJE'