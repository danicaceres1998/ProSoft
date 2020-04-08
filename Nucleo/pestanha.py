# Importamos la clase Servicio
from servicio import Servicio

class Pestaña(Servicio):
    ''' Abstraccion del servicio Pestaña '''
    # Atributo estatico
    cant_pestañas = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_pestañas += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'PESTAÑA'