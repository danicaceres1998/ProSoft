# Importamos la clase Servicio
from servicio import Servicio

class ApliqueKeratina(Servicio):
    ''' Abstraccion del servicio Aplique de Keratina '''
    # Atributo estatico
    cant_apliques = 0

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario):
        Servicio.__init__(self, codigo, descripcion, precio_unitario)
        self.__class__.cant_apliques += 1

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'APLIQUEKERATINA'