# Importamos la clase Administrador y las demas clases que decienden de empleado
from administrador import Administrador
from cajero import Cajero
from manicurista import Manicurista
from maquilladora import Maquilladora
from peluquero import Peluquero
# Importamos la clase Usuario
from usuario import Usuario
# Importamos el validador de datos
from persona import validador_datos_personas

class SuperAdministrador(Administrador, Cajero):
    ''' Abstraccion que representa a un super administrador '''
    # Atributos estaticos
    cant_super_admin = 0

    # Metodos
    @validador_datos_personas
    def __init__(self, ruc, nombre, apellido, telefono, direccion):
        ''' Instancia el objeto SuperAdministrador'''
        # Utilizo el __init__ de Adminstrador
        Administrador.__init__(self, ruc, nombre, apellido, telefono, direccion)
        self.__class__.cant_super_admin += 1

    def crear_empleado(self, tipo_emp, cod_usu, ruc, nombre, apellido, telefono, direccion):
        ''' Funcion que crea un Empleado y un Usuario '''
        # Funciones auxiliares de creacion de empleado #
        def crear_admin(self, cod_usu, ruc, nombre, apellido, telefono, direccion):
            ''' Funcion que crea un Administrador '''
            # Creamos al empleado
            new_emp = Administrador(ruc.upper(), nombre.upper(), apellido.upper(), telefono, direccion.upper())
            # Creamos su usuario
            new_emp.crear_usuario(cod_usu)
            # Retornamos al objeto
            return new_emp

        def crear_cajero(self, cod_usu, ruc, nombre, apellido, telefono, direccion):
            ''' Funcion que crea un Cajero '''
            # Creamos al empleado
            new_emp = Cajero(ruc, nombre, apellido, telefono, direccion)
            # Creamos su usuario
            new_emp.crear_usuario(cod_usu)
            # Retornamos al objeto
            return new_emp

        def crear_manicurista(self, cod_usu, ruc, nombre, apellido, telefono, direccion):
            ''' Funcion que crea un Manicurista '''
            # Creamos al empleado
            new_emp = Manicurista(ruc, nombre, apellido, telefono, direccion)
            # Creamos su usuario
            new_emp.crear_usuario(cod_usu)
            # Retornamos al objeto
            return new_emp

        def crear_maquilladora(self, cod_usu, ruc, nombre, apellido, telefono, direccion):
            ''' Funcion que crea una Maquilladora '''
            # Creamos al empleado
            new_emp = Maquilladora(ruc, nombre, apellido, telefono, direccion)
            # Creamos su Usuario
            new_emp.crear_usuario(cod_usu)
            # Retornamos al objeto
            return new_emp

        def crear_peluquero(self, cod_usu, ruc, nombre, apellido, telefono, direccion):
            ''' Funcion que crea un Peluquero '''
            # Creamos al empleado
            new_emp = Peluquero(ruc, nombre, apellido, telefono, direccion)
            # Creamos su usuario
            new_emp.crear_usuario(cod_usu)
            # Retornamos al objeto
            return new_emp

        def crear_superadmin(self, cod_usu, ruc, nombre, apellido, telefono, direccion):
            ''' Funcion que crea un SuperAdministrador '''
            # Creamos al empleado
            new_emp = SuperAdministrador(ruc, nombre, apellido, telefono, direccion)
            # Creamos su usuario
            new_emp.crear_usuario(cod_usu)
            # Retornamos al objeto
            return new_emp

        # Diccionario de acciones #
        def switch(argument):
            switcher = {
                'ADMINISTRADOR': crear_admin,
                'CAJERO': crear_cajero,
                'MANICURISTA': crear_manicurista,
                'MAQUILLADORA': crear_maquilladora,
                'PELUQUERO': crear_peluquero,
                'SUPERADMINISTRADOR': crear_superadmin
            }
            return switcher.get(argument, lambda: None)

        ### METODO PRINCIPAL ###
        # Vemos que tipo de empleado se quiere crear
        funcion = switch(tipo_emp)
        # Creamos el empleado
        emp_nuevo = funcion(self, cod_usu, ruc, nombre, apellido, telefono, direccion)
        # Retornamos el Objeto
        return emp_nuevo

    # Metodos heredados
    def obtener_datos(self, condicion):
        ''' Devuelve en forma de String los datos de un empleado '''
        if condicion == False:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido
        else:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido + ' ' + str(self.telefono) + ' ' + self.direccion + ' SUPERADMINISTRADOR'

    # Metodo heredado y sobrescrito para pruebas ELIMINAR LUEGO DE UTILIZAR 
    def cargar_cuenta_cliente(self, items, codigos_dados):
        ''' Carga los items al cliente '''
        # Debemos de econtrar los items
        items_a_agregar = [it for cod in codigos_dados for it in items if it.codigo == cod]
        # Condiciones
        if len(items_a_agregar) == len(codigos_dados): # Encontramos todos los articulos
            # Marcamos como vendido los items
            for it in items:
                it.vender()
            # Y cargamos los mismos items al empleado que realizo
            self.agregar_items(items_a_agregar)
            # Retornamos la lista de items
            return items_a_agregar
        elif len(items_a_agregar) < len(codigos_dados): # No se encontraron todos los articulos
            # Retornamos una lista vacia
            return []
        elif len(items_a_agregar) != len(codigos_dados): # Si es distinto
            # Retornamos una lista vacia
            return []