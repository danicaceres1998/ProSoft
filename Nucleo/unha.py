# Importamos la clase Servicio
from servicio import Servicio

class Unha(Servicio):
    ''' Abstraccion del servicio de Unhas'''
    # Atributo estatico
    cant_unhas = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_unhas += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'UÑAS'