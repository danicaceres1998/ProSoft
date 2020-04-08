# Importamos la clase FormaPago
from formaPago import FormaPago

class Dolar(FormaPago):
    ''' Abstraccion del Dolar '''
    # Metodos
    def __init__(self, monto):
        FormaPago.__init__(self, monto)

    def obtener_tipo_pago(self):
        ''' Retorna el tipo de pago '''
        return 'USD'

    # Metodo sobreescrito
    def mostrar_detalle_pago(self):
        ''' Muestra el detalle del pago '''
        return 'Dolar' + ' ' + str(self.obtener_monto())