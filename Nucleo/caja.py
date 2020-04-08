# Importamos las clases de tipo Factura
from facturaContado import FacturaContado
from facturaCredito import FacturaCredito
# Importamos las clases de formas de pago
from cheque import Cheque
from dolar import Dolar
from efectivo import Efectivo
from tarjeta import Tarjeta
from transferencia import Transferencia
# Importamos reduce
from functools import reduce


class Caja:
    ''' Abstraccion de una caja registradora '''
    # Metodos
    def __init__(self):
        self.facturas = []
        self.total_efectivo = 0
        self.total_tarjeta = 0
        self.total_cheque =  0
        self.total_transfer = 0
        self.total_usd = 0

    # Metodos propios de la clase Caja
    def cobrar_cliente(self, lista_cuentas, pos_in_lista_cl, cajero):
        ''' Accion de cobrar a un cliente '''
        # Hacemos los procedimientos para cobrar a un cliente
        cajero.cobrar_cliente(lista_cuentas[pos_in_lista_cl])

    def generar_factura(self, condicion_factura, items, cliente, formas_pago):
        ''' Accion de generar una factura ''' # (tipo_factura, items, cliente_factura, formas_pago)
        # Primero vemos si es una factura contado o una a credito
        if condicion_factura is True:
            factura_nueva = FacturaContado(items)
        else:
            factura_nueva = FacturaCredito(items)
        # Ahora agregamos el cliente
        factura_nueva.agregar_cliente(cliente)
        # Si es una factura contado 
        if condicion_factura is True:
            # Preguntamos si tiene mas de una forma de pago
            if len(formas_pago) != 1:
                monto_pagado = 0
                # Agregamos la forma de pago
                factura_nueva.agregar_formas_pago(formas_pago)
                # Vamos guardando todos los montos
                for fp in formas_pago:
                    if fp.obtener_tipo_pago() == 'CHEQUE':
                        self.total_cheque += fp.obtener_monto()
                        monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'EFECTIVO':
                        self.total_efectivo += fp.obtener_monto()
                        monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TARJETA':
                        self.total_tarjeta += fp.obtener_monto()
                        monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TRANSFERENCIA':
                       self.total_transfer += fp.obtener_monto()
                       monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'USD':
                        self.total_usd += fp.obtener_monto()
                        monto_pagado += factura_nueva.calcular_total_pagar()
                # Preguntamos si pago toda la deuda
                if factura_nueva.calcular_total_pagar() > monto_pagado:
                    raise Exception('EL MONTO PAGADO NO ALCANZA A PAGAR TODA LA DEUDA')
            else:
                # Agregamos la forma de pago
                factura_nueva.agregar_formas_pago(formas_pago)
                # Guardamos el monto
                if formas_pago[0].obtener_tipo_pago() == 'CHEQUE':
                    self.total_cheque += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'EFECTIVO':
                    self.total_efectivo += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'TARJETA':
                    self.total_tarjeta += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'TRANSFERENCIA':
                    self.total_transfer += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'USD':
                    self.total_usd += formas_pago[0].obtener_monto()
        else:
            # Pasamos de largo debido a que no hubo una ganancia
            pass
        # Luego de todo esto agregamos esta factura a la lista de facturas
        self.facturas.append(factura_nueva)
        # Retornamos la factura
        return factura_nueva
    
    def generar_factura_anulacion(self, condicion_factura, items, cliente, formas_pago):
        ''' Accion de generar una factura ''' # (tipo_factura, items, cliente_factura, formas_pago)
        # Primero vemos si es una factura contado o una a credito
        if condicion_factura is True:
            factura_nueva = FacturaContado(items)
        else:
            factura_nueva = FacturaCredito(items)
        # Ahora agregamos el cliente
        factura_nueva.agregar_cliente(cliente)
        # Si es una factura contado 
        if condicion_factura is True:
            # Preguntamos si tiene mas de una forma de pago
            if len(formas_pago) != 1:
                monto_pagado = 0
                # Agregamos la forma de pago
                factura_nueva.agregar_formas_pago(formas_pago)
                # Vamos guardando todos los montos
                for fp in formas_pago:
                    if fp.obtener_tipo_pago() == 'CHEQUE':
                        self.total_cheque += fp.obtener_monto()
                        monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'EFECTIVO':
                        self.total_efectivo += fp.obtener_monto()
                        monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TARJETA':
                        self.total_tarjeta += fp.obtener_monto()
                        monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TRANSFERENCIA':
                       self.total_transfer += fp.obtener_monto()
                       monto_pagado += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'USD':
                        self.total_usd += fp.obtener_monto()
                        monto_pagado = factura_nueva.calcular_total_pagar()
                # Preguntamos si pago toda la deuda
                if factura_nueva.calcular_total_pagar() > monto_pagado:
                    raise Exception('EL MONTO PAGADO NO ALCANZA A PAGAR TODA LA DEUDA')
            else:
                # Agregamos la forma de pago
                factura_nueva.agregar_formas_pago(formas_pago)
                # Guardamos el monto
                if formas_pago[0].obtener_tipo_pago() == 'CHEQUE':
                    self.total_cheque += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'EFECTIVO':
                    self.total_efectivo += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'TARJETA':
                    self.total_tarjeta += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'TRANSFERENCIA':
                    self.total_transfer += formas_pago[0].obtener_monto()
                elif formas_pago[0].obtener_tipo_pago() == 'USD':
                    self.total_usd += formas_pago[0].obtener_monto()
        else:
            # Pasamos de largo debido a que no hubo una ganancia
            pass
        # Retornamos la factura
        return factura_nueva

    def calcular_monto_total(self):
        ''' Calcula el monto total de la caja '''
        # PROGRAMACION FUNCIONAL
        # Utilizamos Reduce y Lamnbda
        return (reduce(lambda x, y: x + y, (self.total_efectivo, self.total_tarjeta, self.total_cheque, self.total_transfer))) - 100000 

    def arquear_caja(self):
        ''' Cierra la contabilidad de la caja '''
        self.total_efectivo = 100000
        self.total_cheque = self.total_tarjeta = self.total_transfer = 0
        self.facturas = []

    def anular_factura(self, cajero, pos_in_lista_fact):
        ''' Anula una factura '''
        cajero.anular_factura(self.facturas, pos_in_lista_fact)

