# Importamos la libreria Abstrack Base Class
from abc import ABCMeta, abstractmethod

# Decorador para validar datos 
def validador_datos_personas(function):
    ''' Valida los datos para instanciar Empleado '''
    def new_funtion(self, ruc, nombre, apellido, telefono, direccion):
        ''' Hace los debidos cambios de los datos '''
        # Primero vemos si tenemos datos numericos
        if isinstance(ruc, str) is False or isinstance(telefono, str) is False:
            ruc = str(ruc)
            telefono = str(telefono)
        # Luego ponemos todos los datos en mayusculas
        nombre = nombre.upper()
        apellido = apellido.upper()
        direccion = direccion.upper()
        # Retornamos todos los datos ya validados
        return function(self, ruc, nombre, apellido, telefono, direccion)
    return new_funtion

class Persona(metaclass = ABCMeta):
    ''' Clase padre de Empleado y Persona '''
    def __init__(self, ruc, nombre, apellido, telefono, direccion):
        self.ruc = ruc
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion

    @abstractmethod
    def obtener_datos(self):
        ''' Retorna en forma de String los datos '''
        pass
