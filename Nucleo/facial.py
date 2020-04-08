# Importamos la clase Servicio
from servicio import Servicio

class Facial(Servicio):
    ''' Abstraccion del servicio Facial '''
    # Atributo estatico
    cant_faciales = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_faciales += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'FACIAL'
