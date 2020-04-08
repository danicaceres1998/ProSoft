# Importmos la clase servicio
from servicio import Servicio

class Peinado(Servicio):
    ''' Abstraccion del servicio Peinar '''
    # Atributo estatico
    cant_peinados = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_peinados += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'PEINADO'
