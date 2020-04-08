# Importamos la clase Servicio
from servicio import Servicio

class Decoloracion(Servicio):
    ''' Abstraccion del servicio Decoloracion '''
    # Atributo estatico
    cant_decoloraciones = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_decoloraciones += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'DECOLORACION'
        