# Importamos la clase Factura
from factura import Factura 
# Importamos la clase Cliente
from cliente import Cliente
# Importamos la clase Efectivo
from efectivo import Efectivo

class FacturaCredito(Factura):
    ''' Abstraccion que representa a una Factura que se paga al contado '''
    # Atributos estaticos
    cant_fact_credito = 0

    # Metodos
    def __init__(self, items):
        Factura.__init__(self, items)
        self.__class__.cant_fact_credito += 1

    # Metodo Heredado y sobre escrito
    def mostrar_datos_factura(self):
        ''' Emite la factura creada '''
        # Primero preguntamos si la factura esta vacia
        if len(self.items) == 0:
            # Lanzamos la Excepcion
            print('No se puede emitir la factura')
        else:
            # Si no continuamos y le pasamos todos los datos y ponemos la fecha de pago
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
                return [self.cliente.obtener_datos(True), detalle, str(self.fecha_emision)]
            else:
                return [self.cliente.obtener_datos(True),  detalle,  str(self.fecha_emision)]

    # Metodo Propio
    def pagar_dueda(self, formas_pago, monto):
        ''' Accion de pagar la deuda '''
        if formas_pago == None:
            self.total_pagar = self.total_pagar - monto
        else:
            pass