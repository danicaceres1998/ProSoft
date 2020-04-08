# Importamos la clase Servicio
from servicio import Servicio

class Planchita(Servicio):
    ''' Abstraccion del servicio de Planchita'''
    # Atributo estatico
    cant_planchitas = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_planchitas += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'PLANCHITA'