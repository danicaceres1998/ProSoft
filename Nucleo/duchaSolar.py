# Importamos la clase Servicio
from servicio import Servicio

class DuchaSolar(Servicio):
    ''' Abstraccion del servicio de DuchaSolar'''
    # Atributo estatico
    cant_duch_solar = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_duch_solar += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'DUCHASOLAR'