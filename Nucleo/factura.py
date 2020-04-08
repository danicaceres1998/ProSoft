# Importamos la clase Compobante
from comprobante import Comprobante
# Importamos la libreria Functools
from functools import reduce
# Importamos la clase Servicio
from servicio import Servicio
# Importamos las clases Efectivo
from efectivo import Efectivo
# Importamos la libreria abc
from abc import ABCMeta
# Importamos la clase cliente
from cliente import Cliente
# Importamos la libreria de fechas
from datetime import datetime


class Factura(Comprobante, metaclass = ABCMeta):
    ''' Abstraccion de una Factura '''
    # Atributos estaticos
    cant_facturas = 0
    
    # Metodos
    def __init__(self, items):
        self.cliente = None
        self.items = items
        self.formas_pago = []
        self.total_pagar = 0
        Comprobante.numero_comprobante += 1
        self.num_factura = None
        self.fecha_emision = datetime.now()
        self.__class__.cant_facturas += 1

    # Metodos propios de Factura
    def agregar_items(self, items_agregados):
        ''' Agrega items a la factura'''
        for item in items_agregados:
            self.items.append(item)

    def agregar_formas_pago(self, formas_pago):
        ''' Agrega las formas de pago a la factura '''
        for f_p in formas_pago:
            self.formas_pago.append(f_p)

    def mostrar_datos_factura(self):
        ''' Emita la factura creada '''
        # Primero preguntamos si la factura esta vacia
        if len(self.items) == 0:
            # Retornamos directamente
            return []
        else:
            # Si no continuamos y pasamos todos los datos de la factura en forma de cadena
            detalle = ''
            # Preguntamos si no tiene forma de pago
            if len(self.formas_pago) == 0: 
                forma = Efectivo(self.calcular_total_pagar())
                self.formas_pago.append(forma)
                detalle = self.formas_pago[0].mostrar_detalle_pago()
            else: # Si tiene
                for fp in self.formas_pago:
                    detalle = detalle + ' ' + fp.mostrar_detalle_pago()
            # Preguntamos si tiene nombre la factura
            if self.cliente == None:
                self.cliente = Cliente('55555-2', 'CLIENTE','OCASIONAL', '+595999999', 'SIN_DIRECCION') 
                return [self.cliente.obtener_datos(True), detalle]
            else:
                return [self.cliente.obtener_datos(True), detalle]

    def ver_items(self):
        ''' Retorna los items cargados dentro de la facutra '''
        return self.items

    def calcular_total_pagar(self):
        ''' Calcula el total a pagar por el cliente '''
        # PROGRAMACION FUNCIONAL
        precios = (it.get_precio() for it in self.items) # Listas por Compresion
        return reduce(lambda x, y: x + y, precios) # Funcion Reduce y lambda

    def agregar_cliente(self, cliente):
        ''' Agrega un cliente a la factura '''
        self.cliente = cliente

    def agregar_num_factura(self, numero_fact):
        ''' Agrega el numero a la factura '''
        self.num_factura = numero_fact