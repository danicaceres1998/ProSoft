# Importamos la clase Item
from item import Item
# Importamos la libreria datetime
from datetime import datetime

class Propina(Item):
    ''' Abstraccion de una Propina '''
    # Metodos
    def __init__(self, cliente):
        self.cliente = cliente
        self.codigo = 'PROP'
        self.precio_unitario = 0
        self.descripcion = 'PROPINA' + cliente.nombre + ' ' + cliente.apellido
        self.fecha_consumision_cliente = None

    # Metodos propios
    def colocar_total(self, monto):
        ''' Coloca el monto a la propina '''
        self.total = monto
        self.fecha_consumision_cliente = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def obtener_datos_item(self, condicion):
        ''' Obtiene los datos de la propina '''
        if condicion == False:
            return self.descripcion + ' ' + str(self.total)
        else:
            return self.descripcion + ' ' + self.cliente.obtener_datos(False) + ' ' + str(self.total) + ' ' + str(self.fecha_consumision_cliente)

    def get_precio(self):
        ''' Retorna el monto de la propina '''
        return self.precio_unitario

    def obtener_clase(self):
        ''' Retorna el tipo de clase '''
        return 'Propina'
        
    # Metodos heredados de Item pero NO implementados
    def vender(self):
        pass
