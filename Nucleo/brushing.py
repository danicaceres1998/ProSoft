# Importamos la clase Servicio
from servicio import Servicio

class Brushing(Servicio):
    ''' Abstraccion del servicio Brushing '''
    # Atributo estatico
    cant_brushing = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_brushing += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'BRUSHING'
        