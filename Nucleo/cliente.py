# Importamos la clase persona
from persona import validador_datos_personas
# Importamos reduce de la libreira Functools
from functools import reduce

class Cliente:
    ''' Abstraccion que representa a un Cliente '''
    # Atributo estatico
    cant_clientes = 0
    
    # Metodos
    @validador_datos_personas
    def __init__(self, ruc, nombre, apellido, telefono, direccion):
        ''' Da valores a la instancia actual '''
        self.ruc = ruc
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.__class__.cant_clientes += 1
        self.items_consumidos = []
        self.facturas = []

    # Metodos Propios
    def cargar_items(self, items_dados):
        ''' Carga los items consumidos por el cliente '''
        for item in items_dados:
            self.items_consumidos.append(item)

    def calcular_deuda(self):
        ''' Sirve para calcular la dueda del cliente '''
        # PROGRAMACION FUNCIONAL
        if len(self.items_consumidos) > 0: # Preguntamos si tiene algun item
            montos = (it.get_precio() for it in self.items_consumidos) # Listas por compresion
            return reduce(lambda x, y: x + y, montos) # Funcion Reduce y lambda
        else:
            # Retornamos 1
            return 1

    def pagar(self):
        ''' Sirve para vaciar la cuenta del cliente
            Ya que ya ha pagado '''
        # Reiniciamos los valores
        self.items_consumidos = []
    
    def guardar_factura(self, factura):
        ''' Guarda la factura del cliente '''
        self.facturas.append(factura)

    # Metodo de la clase Persona
    def obtener_datos(self, condicion):
        ''' Retorna en forma de String '''
        if condicion == False:
            return self.ruc + ' ' + self.nombre + ' ' + self.apellido
        else:
            return self.ruc + ' ' + self.nombre + ' ' + self.apellido + ' ' + self.telefono + ' ' + self.direccion
