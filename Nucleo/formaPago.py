# Importamos la libreria abc
from abc import ABCMeta, abstractmethod

class FormaPago(metaclass = ABCMeta):
    ''' Abstraccion de una forma de pago '''
    # Metodos
    def __init__(self, monto):
        self.monto = monto
    
    def obtener_monto(self):
        ''' Obtiene el monto de la Forma de Pago '''
        return self.monto

    @abstractmethod
    def mostrar_detalle_pago(self):
        ''' Muestra el detalle del pago '''
        pass
        