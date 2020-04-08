# Importamos la clase Servicio
from servicio import Servicio

class Alisado(Servicio):
    ''' Abstraccion del servicio Alisado '''
    # Atributo estatico
    cant_alisados = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_alisados += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'ALISADO'
