# Importamos la clase Servicio
from servicio import Servicio

class Corte(Servicio):
    ''' Abstraccion del servicio Corte '''
    # Atributo estatico
    cant_cortes = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_cortes += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'CORTE'