# Importamos la clase Servicio
from servicio import Servicio

class Lavado(Servicio):
    ''' Abstraccion del servicio Brushing '''
    # Atributo estatico
    cant_lavados = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_lavados += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'LAVADO'
