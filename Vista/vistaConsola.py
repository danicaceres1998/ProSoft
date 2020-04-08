# Importamos os y sys
from os import system
from sys import path
path.append('./Nucleo')
# Importamos otras clases
from facturaContado import FacturaContado # No es un error

# Se encarga de la vista para la consola
class ViewConsola:
    def pedir_codigo_usuario(self):
        ''' Pide datos a un empleado para realizar alguna opcion '''
        self.limpiar_pantalla()
        print('\t----- Ingreso al Sistema -----\n')
        codigo_usuario = str(input('Ingrese su codigo de usuario: '))
        return codigo_usuario 

    def pedir_opcion_usuario(self):
        ''' Pide el codigo del usuario para poder ingresar '''
        opcion = int(input('Ingrese la opcion que desee: '))
        return opcion

    def imprimir_menu_principal(self):
        ''' Imprime el menu principal '''
        menu = ('\t----- Menu INA STYLE -----\n'
                + '\n1-) Atender Cliente'
                + '\n2-) Cobrar Cliente'
                + '\n3-) Administrar Empleados'
                + '\n4-) Administrar Facturacion'
                + '\n5-) Administrar Clientes'
                + '\n6-) Administrar Stock'
                + '\n7-) Informacion de ProSoft'
                + '\n8-) Salir de ProSoft')
        print(menu)

    def imprimir_menu_atencion_cliente(self):
        ''' Imprime el menu de atencion '''
        menu = ('\t----- Opciones de Atencion al cliente -----\n'
                + '\n1-) Abrir Cuenta Cliente'
                + '\n2-) Cargar Cuenta Cliente'
                + '\n3-) Crear Cliente'
                + '\n4-) Crear Item'
                + '\n5-) Salir del menu\n')
        print(menu)

    def imprimir_admin_emp(self):
        ''' Imprime el menu de administracion de empleados '''
        menu = ('\t----- Administracon de Empleados -----\n'
                + '\n1-) Crear nuevo Empleado'
                + '\n2-) Eliminar Empleado'
                + '\n3-) Mostrar Lista de Empleados'
                + '\n4-) Colocar Porcentaje de Ganancia'
                + '\n5-) Calcular Sueldo de un Empleado'
                + '\n6-) Pagar Empleado'
                + '\n7-) Salir del Menu')
        print(menu)

    def imprimir_admin_facturacion(self):
        ''' Imprime el menu de administracion de facturas '''
        menu = ('\t----- Administracion de Facturas -----\n'
                + '\n1-) Ver Todas las facturas'
                + '\n2-) Ver Facturas de la caja'
                + '\n3-) Ver Facturas de un Cliente'
                + '\n4-) Anular Factura'
                + '\n5-) Salir del menu')
        print(menu)

    def imprimir_error(self, cadena):
        ''' Imprime el error '''
        print('ERROR: ', cadena)

    def pedir_datos_cliente(self):
        ''' Pide el ruc del cliente '''
        ruc = str(input('Ingrese el ruc/cedula del cliente: '))
        return ruc
    
    def pedir_ruc_emp(self):
        ''' Pide el ruc del empleado '''
        ruc = str(input('Ingrese el ruc/cedula del empleado: '))
        return ruc

    def pedir_datos_crear_cliente(self):
        ''' Pide todos los datos para crear un cliente '''
        self.limpiar_pantalla()
        # Lista de todos los datos
        lista_datos = []
        print('----- Datos del Cliente -----\n')
        lista_datos.append(input('Ingrese el RUC/Cedula: '))
        lista_datos.append(input('Ingrese el Nombre: '))
        lista_datos.append(input('Ingrese el Apellido: '))
        lista_datos.append(input('Ingrese el numero de Telefono: '))
        lista_datos.append(input('Ingrese la Direccion/Ciudad: '))
        # Retornamos todos los datos
        return lista_datos

    def limpiar_pantalla(self):
        ''' Limpia la pantalla '''
        system('clear')

    def imprimir_aviso(self, cadena):
        ''' Imprime los avisos '''
        print('AVISO: ', cadena)

    def imprimir_lista_cuentas(self, clientes):
        ''' Imprime la lista de clientes que tienen una cuenta abierta '''
        self.limpiar_pantalla()
        print('----- Cuentas abiertas -----\n')
        for i in range(len(clientes)):
            print((i+1), '-) ', clientes[i].obtener_datos(False))

    def imprimir_lista_items(self, items):
        ''' Imprime la lista de items '''
        self.limpiar_pantalla()
        print('----- Lista Items -----\n')
        for i in range(len(items)):
            print((i+1), '-) ', items[i].obtener_datos_item(False))

    def imprimir_lista_clientes(self, clientes):
        ''' Imprime la lista de items '''
        self.limpiar_pantalla()
        print('----- Lista Clientes -----\n')
        for i in range(len(clientes)):
            print((i+1), '-) ', clientes[i].obtener_datos(False))
        print()

    def pedir_pos_lista(self):
        ''' Pide una posicion en la lista '''
        pos_in_lista = int(input('\nIngrese de la posicion in lista del Cliente: '))
        return (pos_in_lista-1)

    def pedir_datos_crear_item(self):
        ''' Pide todos los datos para crear un item '''
        self.limpiar_pantalla()
        # Lista de todos los datos
        lista_datos = []
        print('----- Datos del Item -----\n')
        lista_datos.append(input('Ingrese el Tipo de Servicio (Corte, Peinado, etc.): '))
        lista_datos.append(input('Ingrese el Codigo: '))
        lista_datos.append(input('Ingrese la Descripcion: '))
        lista_datos.append(int(input('Ingrese el Precio Unitario: ')))
        # Retornamos todos los datos
        return lista_datos

    def imprimir_datos_software(self, lista):
        ''' Imprime los datos del Software '''
        self.limpiar_pantalla()
        print('----- DATOS DEL SISTEMA -----\n')
        print('Nombre: ', lista[0]
                + '\nAutor: ', lista[1]
                + '\nLicencia: ', lista[2]
                + '\nVersion: ', lista[3]
                + '\nEmail: ', lista[4]
                + '\nStatus: ', lista[5])

    def pedir_codigos_items(self):
        ''' Pide todos los codigos que seran cargados en la cuenta de un cliente '''
        # Variables
        codigos = []
        respuesta = 0
        # Imprimimos el menu
        print('\n\t----- Ingreso de Codigos -----\nOBS: Si ya no quiere ingresar mas Items, ingrese: "1"\n')
        while respuesta != '1':
            respuesta = str(input('Ingrese el Codigo del item que desee: '))
            if respuesta != '1':
                codigos.append(respuesta)
        # Retornamos la lista de codigos
        return codigos

    def mostrar_dueda_cliente(self, cliente):
        ''' Muestra la deuda de un cliente '''
        self.limpiar_pantalla()
        print('----- Total a Pagar -----\n')
        print('Cliente: ', cliente.obtener_datos(False)
            + '\tTotal Deuda: ', cliente.calcular_deuda())

    def preguntar_forma_pago(self):
        ''' Pide las formas de pago al cliente '''
        print('OBS: Si desea pagar solamente en efectivo coloque: 1')
        condicion = int(input('Desea pagar solo en efectivo ?: '))
        if condicion == 1:
            return False
        else:
            return True

    def pedir_formas_pago(self):
        ''' Pide las formas de pago '''
        print('----- FORMAS PAGO -----\n')
        respuesta = 0
        lista_formas = []
        montos = []
        while respuesta != 5:
            print('Lista de formas de pago(puede tener mas de una):'
                + '\n1-)Cheque'
                + '\n2-)Efectivo'
                + '\n3-)Tarjeta'
                + '\n4-)Transferencia'
                + '\n5-)Continuar con el Cobro')
            respuesta = int(input('\nIngrese su opcion (El numero de la lista): '))
            if respuesta != 5:
                lista_formas.append(respuesta)
                montos.append(int(input('Ingrese el monto: ')))
        # Retornamos las respuestas
        return [lista_formas, montos]

    def pedir_datos_pago(self):
        ''' Pide el voucher, num_cheque, num_transferencia '''
        return input('\nOBS: Puede ser el voucher, numero de cheque o de transferencia\n'
                    + 'Ingrese el dato del pago: ')

    def mostrar_datos_factura(self, factura):
        ''' Muestra los datos de una factura '''
        # Vector que posee los datos de la factura
        datos_fact = factura.mostrar_datos_factura()
        # Primero agarramos los datos del cliente (pos: [0])
        print('\t----- DATOS DE LA FACTURA -----\n')
        print('1-) Datos del Cliente: ', str(datos_fact[0])
            + '\n2-) Detalle del pago: ', str(datos_fact[1]))
        # Mostramos si es una factura contado o credito
        if factura.__class__ is FacturaContado:
            print('3-) Fecha de pago: ', datos_fact[2])
        else:
            print('3-) Fecha de deuda: ', datos_fact[2])
        # Mostramos los items consumidos
        print('4-) ITEMS CONSUMIDOS:')
        items = factura.ver_items()
        for i in range(len(items)):
            print('\t', (i+1), '-) ', items[i].obtener_datos_item(True))
        print('\n5-) TOTAL A PAGAR: ', factura.calcular_total_pagar())
        print()

    def pedir_datos_empleado(self):
        ''' Pide los datos para la creacion de un empleado '''
        print('----- DATOS DEL EMPLEADO -----\n')
        # Lista de datos
        lista_datos = []
        # Pedimos los datos
        lista_datos.append(input('Ingrese el RUC/Cedula: '))
        lista_datos.append(input('Ingrese el Nombre: '))
        lista_datos.append(input('Ingrese el Apellido: '))
        lista_datos.append(input('Ingrese el numero de Telefono: '))
        lista_datos.append(input('Ingrese la Direccion/Ciudad: '))
        lista_datos.append(input('Ingrese el codigo de Usuario: '))
        lista_datos.append(input('Igrese el tipo de Empleado (Peluquero, Manicurista, etc): '))
        # Retornamos los datos
        return lista_datos

    def mostrar_lista_empleados(self, list_emp):
        ''' Imprime en pantalla la lista de empleados '''
        self.limpiar_pantalla()
        print('----- LISTA DE EMPLEADOS -----\n')
        for i in range(len(list_emp)):
            print((i+1), '-) ', list_emp[i].obtener_datos(True))
        print()

    def pedir_porcent_emp(self):
        ''' Pide los porcentajes para el empleado '''
        print('----- PORCENTAJES DE GANANCIA -----\n'
            + '\nOBS: Orden de los porcentajes es el sgte:\n'
            + '1- Alarge 2- Alisado 3- Aplique de Keratina 4- Balayage\n'
            + '5- Baño Tratamiento 6- Barberia 7- Brushing 8- Corte\n'
            + '9- Decoloracion 10- Depilacion 11- Extraccion de Extension\n'
            + '12- Facial 13- Lavado 14- Manicura 15- Masaje\n'
            + '16- Peinado 17- Pestaña 18- Reflejo 19- Tinte\n')
        # Lista de porcentajes
        list_porcent = []
        # Cantidad de Servicios
        cant_service = 19
        # Pedimos los porcentajes
        for i in range(cant_service):
            print((i+1), ': ', end='')
            list_porcent.append(float(input()))
        # Retornamos la lista
        return list_porcent

