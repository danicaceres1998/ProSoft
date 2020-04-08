# Importamos la clase Servicio
from servicio import Servicio

class Mecha(Servicio):
    ''' Abstraccion del servicio de Mechas'''
    # Atributo estatico
    cant_mechas = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_mechas += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'MECHAS'