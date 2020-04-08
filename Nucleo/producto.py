# Importamos la clase Item
from item import Item
# Importamos la libreria 
from datetime import datetime

class Producto(Item):
    ''' Abstraccion que representa a un servicio '''

    # Metodos
    def __init__(self, codigo, descripcion, precio_unitario, porcent_comision, porcent_impuesto, marca):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.porcent_comision = porcent_comision
        self.porcent_impuesto = porcent_impuesto
        self.fecha_consumicion_cliente = None
        self.lista_proveedores = []
        self.marca = marca

    # Metodo heredados e implementados de la clase Item
    def obtener_datos_item(self, condicion):
        ''' Retorna los datos item '''
        if condicion == False:
            return str(self.codigo) + ' ' + self.marca.obtener_datos() + ' ' + str(self.precio_unitario)
        else:
            return str(self.codigo) + ' ' + self.marca.obtener_datos() + ' ' + self.descripcion + ' ' + str(self.precio_unitario) + ' ' + str(self.porcent_comision) + ' ' + str(self.porcent_impuesto) + ' ' + str(self.fecha_consumicion_cliente) 

    def vender(self):
        ''' Accion de vender un producto '''
        pass

    # Metodos propios
    def agregar_vendible(self):
        ''' Agregamos las acciones para que un producto sea vendible '''
        pass

    def agregar_proveedores(self, proveedor):
        ''' Accion que agrega un proveedor a los productos '''
        self.lista_proveedores.append(proveedor)
