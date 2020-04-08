# Importamos la clase Empleado
from empleado import Empleado
# Importamos el validador de datos
from persona import validador_datos_personas

class Maquilladora(Empleado):
    ''' Abstraccion que representa a un Maquilladora '''
    # Atributo estatico
    cant_maquilladores = 0
    
    # Metodos
    @validador_datos_personas
    def __init__(self, ruc, nombre, apellido, telefono, direccion):
        ''' Instancia el objeto Maquilladora '''
        Empleado.__init__(self, ruc, nombre, apellido, telefono, direccion)
        self.__class__.cant_maquilladores += 1

    # Metodos heredados
    def obtener_datos(self, condicion):
        ''' Devuelve en forma de String los datos de un empleado '''
        if condicion == False:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido
        else:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido + ' ' + str(self.telefono) + ' ' + self.direccion + ' MAQUILLADORA'