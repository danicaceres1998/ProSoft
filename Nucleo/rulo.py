# Importamos la clase Servicio
from servicio import Servicio

class Rulo(Servicio):
    ''' Abstraccion del servicio de Rulos'''
    # Atributo estatico
    cant_rulos = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_rulos += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'RULOS'