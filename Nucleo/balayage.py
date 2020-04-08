# Importamos la clase Servicio
from servicio import Servicio

class Balayage(Servicio):
    ''' Abstraccion del servicio Balayage '''
    # Atributo estatico
    cant_balayage = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_balayage += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'BALAYAGE'
