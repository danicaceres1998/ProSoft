# Importamos la libreria abc
from abc import ABCMeta

class Comprobante(metaclass = ABCMeta):
    ''' Abstraccion de un comprobante '''
    # Atributo estatico
    numero_comprobante = 0