
class Marca:
    ''' Abstraccion de una Marca '''
    # Metodos
    def __init__(self, nombre, clase_producto):
        self.nombre = nombre
        self.cantidad_ejemplares = 1
        self.clase_producto = clase_producto

    def ver_disponibilidad(self):
        ''' Retorna la disponibilidad de los ejemplares '''
        return self.cantidad_ejemplares
    
    def obtener_datos(self):
        ''' Retona los datos de la Marca '''
        return self.nombre + ' ' + self.clase_producto

    def colocar_marca_producto(self):
        ''' Coloca la marca al producto '''
        self.cantidad_ejemplares += 1
