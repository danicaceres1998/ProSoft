# Importamos la clase FormaPago
from formaPago import FormaPago

class Cheque(FormaPago):
    ''' Abstraccion de un Cheque '''
    # Metodos
    def __init__(self, monto, num_cheque):
        FormaPago.__init__(self, monto)
        self.num_cheque = num_cheque
    
    # Metodo propio de Cheque
    def obtener_num_cheque(self):
        ''' Retorna el numero de cheque '''
        return self.num_cheque

    def obtener_tipo_pago(self):
        ''' Retorna el tipo de pago '''
        return 'CHEQUE'
        
    # Metodo sobreescrito
    def mostrar_detalle_pago(self):
        ''' Muestra el detalle del pago '''
        return 'Cheque' + ' ' + str(self.obtener_monto()) + ' ' + str(self.obtener_num_cheque())