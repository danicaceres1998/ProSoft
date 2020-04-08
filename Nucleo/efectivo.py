# Importamos la clase FormaPago
from formaPago import FormaPago

class Efectivo(FormaPago):
    ''' Abstraccion del Efectivo '''
    # Metodos
    def __init__(self, monto):
        FormaPago.__init__(self, monto)

    def obtener_tipo_pago(self):
        ''' Retorna el tipo de pago '''
        return 'EFECTIVO'

    # Metodo sobreescrito
    def mostrar_detalle_pago(self):
        ''' Muestra el detalle del pago '''
        return 'Efectivo' + ' ' + str(self.obtener_monto())