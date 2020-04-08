# Importamos la clase FormaPago
from formaPago import FormaPago

class Transferencia(FormaPago):
    ''' Abstraccion de una Transferencia Bancaria '''
    # Metodos
    def __init__(self, monto, num_transfer):
        FormaPago.__init__(self, monto)
        self.num_transfer = num_transfer

    # Metodo propio de Transferencia
    def obtener_num_trans(self):
        ''' Retorna el numero de transferencia Bancaria '''
        return self.num_transfer

    def obtener_tipo_pago(self):
        ''' Retorna el tipo de pago '''
        return 'TRANSFERENCIA'

    # Metodo sobreescrito
    def mostrar_detalle_pago(self):
        ''' Muestra el detalle del pago '''
        return 'Transferencia' + ' ' + str(self.obtener_monto()) + ' ' + str(self.obtener_num_trans())