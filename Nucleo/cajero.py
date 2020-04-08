# Importamos la clase Empleado
from empleado import Empleado
# Importamos el validador de datos
from persona import validador_datos_personas

class Cajero(Empleado):
    ''' Abstraccion que representa a un Cajero '''
    # Atributo estatico
    cant_cajeros = 0

    # Metodos
    @validador_datos_personas
    def __init__(self, ruc, nombre, apellido, telefono, direccion,):        
        ''' Instancia el objeto Cajero '''
        Empleado.__init__(self, ruc, nombre, apellido, telefono, direccion)
        self.__class__.cant_cajeros += 1
    
    # Metodos propios de la clase Cajero
    def cobrar_cliente(self, cliente):
        ''' Accion de cobrar al cliente, y encerar la cuenta '''
        # Va a reiniciar la lista de items
        cliente.pagar()

    def guardar_factura(self, cliente, factura):
        ''' Accion de guardar la factura dentro del objeto cliente'''
        cliente.guardar_factura(factura)

    def arquear_caja(self, caja): 
        ''' Accion que arquea una caja de cobros '''
        return caja.arquear_caja()

    def cerrar_cuenta_cliente(self, lista_cuenta_clientes, cliente_cuenta_pos):
        ''' Accion que cierra la cuenta de un cliente '''
        # Le sacamos de la lista de los que Deben
        lista_cuenta_clientes.remove(lista_cuenta_clientes[cliente_cuenta_pos])
        # Retornamos la lista
        return lista_cuenta_clientes

    def anular_factura(self, lista_facturas, factura_pos):
        ''' Anula una factura '''
        # Eliminamos la factura
        lista_facturas.remove(lista_facturas[factura_pos])
        # Retornamos la lista
        return lista_facturas

    # Metodos heredados
    def obtener_datos(self, condicion):
        ''' Devuelve en forma de String los datos de un empleado '''
        if condicion == False:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido
        else:
            return str(self.usuario.obtener_codigo()) + ' ' + self.nombre + ' ' + self.apellido + ' ' + str(self.telefono) + ' ' + self.direccion + ' CAJERO'

    # Metodo Heredado y sobreescrito
    def cargar_cuenta_cliente(self, items, codigos_dados, lista_cuenta_clientes, posicion_en_lista):
        ''' Carga los items al cliente '''
        # Debemos de econtrar los items
        items_a_agregar = [it for cod in codigos_dados for it in items if it.codigo == cod]
        # Condiciones
        if len(items_a_agregar) == len(codigos_dados): # Encontramos todos los articulos
            # Procedemos a cargar los items al cliente
            lista_cuenta_clientes[posicion_en_lista].cargar_items(items_a_agregar)
            # Marcamos como vendido los items
            for it in items:
                it.vender()
            # Retornamos la lista
            return lista_cuenta_clientes
        elif len(items_a_agregar) < len(codigos_dados): # No se encontraron todos los articulos
            # Retornamos una lista vacia
            return []