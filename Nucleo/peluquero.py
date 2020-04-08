# Importamos la clase Empleado
from empleado import Empleado

class Peluquero(Empleado):
    ''' Abstraccion que representa a un Peluquero '''
    # Atributo estatico
    cant_peluqueros = 0

    # Metodos
    def __init__(self, ruc, nombre, apellido, telefono, direccion):
        ''' Instancia el objeto Administrador '''
        Empleado.__init__(self, ruc, nombre, apellido, telefono, direccion)
        self.__class__.cant_peluqueros += 1

    # Metodos heredados
    def obtener_datos(self, condicion):
        ''' Devuelve en forma de String los datos de un empleado '''
        if condicion == False:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido
        else:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido + ' ' + str(self.telefono) + ' ' + self.direccion + ' PELUQUERO'
