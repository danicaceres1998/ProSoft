# Importamos la clase Servicio
from servicio import Servicio

class Manicura(Servicio):
    ''' Abstraccion del servicio Manicura '''
    # Atributo estatico
    cant_manicuras = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_manicuras += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'MANICURA'
