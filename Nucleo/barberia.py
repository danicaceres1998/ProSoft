# Importamos la clase Servicio
from servicio import Servicio

class Barberia(Servicio):
    ''' Abstraccion del servicio Barberia '''
    # Atributo estatico
    cant_barb = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_barb += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'BARBERIA'