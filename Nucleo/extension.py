# Importamos la clase Servicio
from servicio import Servicio

class Extension(Servicio):
    ''' Abstraccion del servicio de Extension de Cabello'''
    # Atributo estatico
    cant_extensiones = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_extensiones += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'EXTENSION'