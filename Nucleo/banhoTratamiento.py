# Importamos la clase Servicio
from servicio import Servicio

class BañoTratamiento(Servicio):
    ''' Abstraccion del servicio Baño con Tratamiento '''
    # Atributo estatico
    cant_baños_trat = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_baños_trat += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'BAÑOTRATAMIENTO'