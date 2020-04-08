# Importamos la libreria Abstrack Base Class
from abc import ABCMeta, abstractmethod

# Decorador para validar datos
def validador_de_items(function):
    ''' Valida los datos de los items '''
    def new_function(self, codigo, descripcion, precio_unitario):
        # Vemos que nuestro codigo sea de tipo string
        if isinstance(codigo, str) is False:
            codigo = str(codigo)
        # Validamos nuestro precio
        if isinstance(precio_unitario, int) is False:
            # Lanzamos la excepcion
            raise Exception('OCURRIO UN ERROR AL CARGAR EL PRECIO')
        # Luego ponemos todos los datos en mayusculas
        descripcion = descripcion.upper()
        # Retornamos los datos ya validados
        return function(self, codigo, descripcion, precio_unitario)

    return new_function

class Item(metaclass = ABCMeta):
    ''' Clase padre de Servicio y Persona '''
    
    @abstractmethod
    def vender(self):
        ''' Accion de vender un item '''
        pass

    @abstractmethod
    def obtener_datos_item(self):
        ''' Retorna los datos del Item '''
        pass
