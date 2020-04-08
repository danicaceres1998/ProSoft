# Importamos la clase Empleado 
from empleado import Empleado
# Importamos el validador
from persona import validador_datos_personas

class Administrador(Empleado):
    ''' Abstraccion que representa a un Administrador '''
    # Atributo estatico
    cant_administradores = 0

    # Metodos
    @validador_datos_personas
    def __init__(self, ruc, nombre, apellido, telefono, direccion):
        ''' Instancia el objeto Administrador '''
        Empleado.__init__(self, ruc, nombre, apellido, telefono, direccion)
        self.__class__.cant_administradores += 1

    # Metodos propios de la clase Administrador
    def controlar_stock(self):
        ''' Accion que da informacion del stock '''
        pass

    def cargar_stock(self):
        ''' Carga los nuevos elementos para el stock '''
        pass

    def descontar_stock(self):
        ''' Descuenta los elementos del stock utilizados por el personal '''
        pass

    def colocar_porcent_empleados(self, lista_empleados, lista_porcentajes, pos_in_lista_emp):
        ''' Coloca los porcentajes a los empleados '''
        # Colocamos como variable
        emp_a_colocar = lista_empleados[pos_in_lista_emp]
        # Le asignamos todos los porcentajes correspondientes
        emp_a_colocar.colocar_porcent(lista_porcentajes)
        # Y le retornamos a la lista
        lista_empleados[pos_in_lista_emp] = emp_a_colocar

    def colocar_porcent_productos(self):
        ''' Coloca los porcentajes a los productos '''
        pass

    # Metodos heredados
    def obtener_datos(self, condicion):
        ''' Devuelve en forma de String los datos de un empleado '''
        if condicion == False:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido
        else:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido + ' ' + str(self.telefono) + ' ' + self.direccion + ' ADMINISTRADOR'
