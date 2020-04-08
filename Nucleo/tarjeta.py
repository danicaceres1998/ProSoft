# Importamos la clase FormaPago
from formaPago import FormaPago

class Tarjeta(FormaPago):
    ''' Abstraccion de una Tarjeta '''
    # Metodos
    def __init__(self, monto, voucher):
        FormaPago.__init__(self, monto)
        self.voucher = voucher

    # Metodo propio de Tarjeta
    def obtener_voucher(self):
        ''' Retorna el numero de Voucher de la tarjeta '''
        return self.voucher

    def obtener_tipo_pago(self):
        ''' Retorna el tipo de pago '''
        return 'TARJETA'

    # Metodo sobreescrito
    def mostrar_detalle_pago(self):
        ''' Muestra el detalle del pago '''
        return 'Tarjeta' + ' ' + str(self.obtener_monto()) + ' ' + str(self.obtener_voucher())