# Importamos la clase Servicio
from servicio import Servicio

class Onda(Servicio):
    ''' Abstraccion del servicio de Ondas en el Cabello'''
    # Atributo estatico
    cant_ondas = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_ondas += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'ONDAS'