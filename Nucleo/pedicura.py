# Importamos la clase Servicio
from servicio import Servicio

class Pedicura(Servicio):
    ''' Abstraccion del servicio Pedicura '''
    # Atributo estatico
    cant_pedicuras = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_pedicuras += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'PEDICURA'
