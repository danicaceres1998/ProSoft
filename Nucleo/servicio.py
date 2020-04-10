# Importamos la clase Item
from item import Item, validador_de_items
# Importamos la fecha
from datetime import datetime
# Importamos la libreria abc
from abc import ABCMeta, abstractmethod

class Servicio(Item, metaclass = ABCMeta):
    ''' Abstraccion de un Servicio '''
    # Metodos
    @validador_de_items
    def __init__(self, codigo, descripcion, precio_unitario):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.porcent_impuesto = 0.10 # Definido por el programador
        self.fecha_consumision_cliente = None

    def vender(self):
        ''' Accion de vender un Servicio '''
        self.fecha_consumision_cliente = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_precio(self):
        ''' Devuelve el precio unitario del servicio '''
        return self.precio_unitario

    def obtener_datos_item(self, condicion):
        ''' Obtiene todos los datos del Item '''
        if condicion == False:
            return str(self.codigo) + ' ' + self.descripcion + ' ' + str(self.precio_unitario)
        else:
            return str(self.codigo) + ' ' + self.descripcion + ' ' + str(self.precio_unitario) + ' ' + str(self.porcent_impuesto) + ' ' + str(self.fecha_consumision_cliente)

    @abstractmethod
    def obtener_clase(self):
        pass