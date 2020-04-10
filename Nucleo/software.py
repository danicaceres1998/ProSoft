# Importamos clase sys
from sys import path
from functools import reduce
# Agregamos la carpeta de Persistencia
path.append('./Persistencia')
# Importamos la clase model
from Persistencia.model import Model
# Importamos la peluqueria
from peluqueria import Peluqueria
# Importamos las clases necesarias para el control
from cajero import Cajero
from administrador import Administrador
# Importamos las clases de formas de pago
from cheque import Cheque
from dolar import Dolar
from efectivo import Efectivo
from tarjeta import Tarjeta
from transferencia import Transferencia

# Clase que hace el papel de Controlador
class Software:
    ''' Abstraccion del Software Controlador'''
    # Atributos estaticos
    __name__ = 'ProSoft'
    __author__ = 'Juan Daniel Ojeda'
    __license__ = 'Private Domain'
    __version__ = '1.0.0'
    __email__ = 'jdoc.298@gmail.com'
    __status__ = 'Prototype'
    # Numero Sucursal de la peluqueria
    NUM_SUCUR = 0

    #### MODELO CON ZODB ####
    def __init__(self):
        self.peluquerias = []
        self.model = Model()
        self.num_sucur = 0 # Numero de Sucursal por defecto
        pelu = self.model.devolver_peluqueria(self.NUM_SUCUR)
        self.asociar_peluqueria(pelu)

    # Metodos propios
    def asociar_peluqueria(self, peluqueria):
        ''' Asocia una peluqueria al Software '''
        self.peluquerias.append(peluqueria)

    def obtener_informacion_software(self):
        ''' Obtiene toda la informacion del software '''
        lista_datos = []
        lista_datos.append(self.__name__)
        lista_datos.append(self.__class__.__author__)
        lista_datos.append(self.__class__.__license__)
        lista_datos.append(self.__class__.__version__)
        lista_datos.append(self.__class__.__email__)
        lista_datos.append(self.__class__.__status__)
    
    # Funciones para Area principal
    def abrir_cuenta_cliente(self, emp, ruc_cliente):
        ''' A traves del Empleado se abre una cuenta '''
        ### ANTES DE HACER ESTA ACCION DEBEMOS DE PEDIR EL RUC DEL CLIENTE Y EL EMPLEADO ###
        try:
            ### Antes de realizar la accion, obtenemos los datos actualizados de la BD ###
            # Actualizamos la lista de cuentas abiertas
            self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta = self.model.obtener_lista_cl_cuenta(self.NUM_SUCUR)
            # Actualizamos la lista de clientes
            self.peluquerias[self.NUM_SUCUR].clientes = self.model.obtener_clientes(self.NUM_SUCUR)
            # Verificamos que haya clientes
            if len(self.peluquerias[self.NUM_SUCUR].clientes) == 0:
                raise Exception('NO EXISTE NINGUN CLIENTE EN LA BASE DE DATOS')
            cliente_a_agregar = self.peluquerias[self.NUM_SUCUR].verificar_cliente(ruc_cliente)
            # Si no existe el cliente lanzamos una excepcion
            if cliente_a_agregar is None:
                raise Exception('NO EXISTE EL CLIENTE')
            # Preguntamos si ya esta en la lista
            if self.peluquerias[self.NUM_SUCUR].cuenta_abierta(cliente_a_agregar) is True:
                raise Exception ('YA ESTA ABIERTA LA CUENTA')
        except:
            raise # Propagamos la excepcion
        else:
            # Agregamos a la lista de cuentas
            self.model.agregar_cl_in_cuentas(cliente_a_agregar, self.NUM_SUCUR)
            return (cliente_a_agregar.nombre) + ' ' + (cliente_a_agregar.apellido)

    def cargar_cuenta_cliente(self, emp, pos_cliente, codigos):
        '''' A traves del Empleado se carga la cuenta de un cliente ''' 
        ## DEBEMOS DE RECIBIR COMO PARAMETRO LA POS IN LISTA DEL CLIENTE Y LOS CODIGOS DE LOS ITEMS QUE CONSUMIO (EMP tambien) ##
        ## Verificamos los datos ##
        try:
            # SNPIL: Sin Numero de Pos In Lista
            if pos_cliente == 'SNPIL':
                raise Exception('NO SE PUEDE UBICAR AL CLIENTE SIN LA CUENTA')
            # Vemos si la lista esta vacia
            if len(codigos) == 0:
                raise Exception('LA LISTA DE CODIGOS ESTA VACIA')
        except:
            # Propagamos la excepcion
            raise
        ## Antes de realizar la accion, obtenemos los datos actualizados de la BD ##
        # Actualizamos la lista de cuentas abiertas
        self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta = self.model.obtener_lista_cl_cuenta(self.NUM_SUCUR)
        # Actualizamos la lista de items
        self.peluquerias[self.NUM_SUCUR].items = self.model.obtener_items(self.NUM_SUCUR)
        # Actualizamos la lista de clientes
        self.peluquerias[self.NUM_SUCUR].clientes = self.model.obtener_clientes(self.NUM_SUCUR)
        # Actualizamos la lista de empleados
        self.peluquerias[self.NUM_SUCUR].empleados = self.model.obtener_empleados(self.NUM_SUCUR)
        # Verificamos que todo ha salido bien
        try:
            # Conseguimos la ubicacion del empleado en la lista
            pos_emp = self.pos_emp_in_lista(emp)
            # Verificamos los codigos de items
            list_items = self.peluquerias[self.NUM_SUCUR].cargar_cuenta_cliente(pos_emp, codigos)
            # Lanzamos una excepcion si no se encotraron todos los items
            if len(list_items) == 0:
                raise Exception('OCURRIO UN ERROR AL CARGAR LOS ITEMS\nOBS: Puede ser que no se encotraron todos los items')
        except:
            # Propagamos la excepcion
            raise
        # Si todo esta bien continuamos
        else:
            ## Actualizamos la Base de Datos ##
            try:
                # Actualizamos la lista de Cuentas, Clientes y Empleados
                self.model.actualizar_dat_cuenta_cl(pos_cliente, list_items, self.NUM_SUCUR)
                self.model.emplado_dat_actualizar(self.peluquerias[self.NUM_SUCUR].empleados[pos_emp],
                pos_emp, self.NUM_SUCUR)
            except:
                # Propagamos la excepcion
                raise
            else:
                # Retornamos el nombre y apellido del cliente
                cliente = self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta[pos_cliente]
                datos_cl = cliente.nombre + ' ' + cliente.apellido
                return datos_cl
    
    def crear_cliente(self, emp, lista_datos):
        ''' A traves del Empleado se crea un nuevo cliente '''
        ### DEBEMOS DE RECIBIR COMO PARAMETRO TODOS LOS DATOS DEL CLIENTE ###
        # Vemos que no tenga caracteres vacios
        for dat in lista_datos:
            if dat == '':
                raise Exception('NO DEBE DE ESTAR VACIO NINGUN CAMPO, FAVOR COMPLETE TODOS LOS DATOS')
        # Antes de continuar verificamos que no tenga valores vacios
        # Antes de realizar la accion obtenemos los datos actualizados de la BD
        self.peluquerias[self.NUM_SUCUR].clientes = self.model.obtener_clientes(self.NUM_SUCUR)
        # Vemos si ya existe el cliente
        try:
            # lista_datos[0]: Es el ruc del cliente a agregar al sistema
            if self.peluquerias[self.NUM_SUCUR].cliente_existente(lista_datos[0]) is True:
                raise Exception('YA EXISTE EL CLIENTE CON EL RUC: ' + str(lista_datos[0]))
        except:
            raise # Propagamos la excepcion
        # Si todo esta bien continuamos
        else:
            # A traves del empleado creamos un nuevo cliente
            cliente_nuevo =self.peluquerias[self.NUM_SUCUR].crear_cliente(emp, lista_datos)
            # Actualizamos la Base de Datos
            self.model.agregar_cliente_nuevo(cliente_nuevo, self.NUM_SUCUR)

    def crear_item(self, emp, lista_datos):
        ''' A traves del Empleado se crea un nuevo item '''
        ### DEBEMOS DE RECIBIR COMO PARAMETRO TODOS LOS DATOS PARA LA CREACION DE UN NUEVO ITEM ###
        # Verificamos que no se haya puesto bien el precio
        if isinstance(lista_datos[3], int) is False:
            raise Exception('EL PRECIO DEBE DE SER NUMERICO')
        # Antes de continuar verificamos que no haiga ningun campo vacio
        for dat in lista_datos:
            if dat == '':
                raise Exception('NO DEBE DE ESTAR VACIO NINGUN CAMPO, FAVOR COMPLETE TODOS LOS DATOS')    
        # Antes de realizar la accion obtenemos los datos actualizados de la BD
        self.peluquerias[self.NUM_SUCUR].items = self.model.obtener_items(self.NUM_SUCUR)
        # Vemos si ya existe el item
        try:
            # lista_datos[1]: corresponde al codigo del item
            if self.peluquerias[self.NUM_SUCUR].item_existente(lista_datos[1]) is True:
                raise Exception('YA EXISTE UN ITEM CON EL CODIGO: ' + str(lista_datos[1]))
        except:
            raise # Propagamos la excepcion
        # Si todo salio bien continuamos
        else:
            # Validamos el tipo de servicio para que no lanze un error; lista_datos[0]: corresponde al Tipo de Servicio
            lista_datos[0] = lista_datos[0].upper()
            # A traves del empleado creamos el nuevo item
            nuevo_item = self.peluquerias[self.NUM_SUCUR].crear_item(emp, lista_datos)
            # Actualizamos la Base de Datos
            self.model.guardar_nuevo_item(nuevo_item, self.NUM_SUCUR)

    ### FUNCIONES PARA COBRO DE CLIENTES ###
    def cobrar_cliente(self, emp, pos_cliente, ruc_factura, tipo_factura, formas_pago):
        ''' Muestra el menu para cobrar a un cliente '''
        ### DEBEMOS DE RECIBIR COMO PARAMETRO AL EMPLEADO (YA VALIDADO QUE SEA DEL TIPO NECESARIO), 
        # LA POS IN LISTA DEL CLIENTE, LOS MEDIOS DE PAGO
        # Antes de realizar la accion obtenemos los datos actualizados de la BD
        self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta = self.model.obtener_lista_cl_cuenta(self.NUM_SUCUR)
        cliente_a_cobrar = self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta[pos_cliente]
        # Actualizamos la lista de clientes
        self.peluquerias[self.NUM_SUCUR].clientes = self.model.obtener_clientes(self.NUM_SUCUR)
        # Actualizamos la lista de cajas
        self.peluquerias[self.NUM_SUCUR].cajas = self.model.obtener_cajas(self.NUM_SUCUR)
        # Antes de generar la factura, actualizamos la lista de facturas
        self.peluquerias[self.NUM_SUCUR].facturas = self.model.obtener_facturas(self.NUM_SUCUR)
        try:
            # Generamos la factura: (tipo_factura, cuenta, ruc_factura, formas_pago)
            factura_gen = self.peluquerias[self.NUM_SUCUR].generar_factura(tipo_factura, cliente_a_cobrar, ruc_factura, formas_pago)
        except:
            # Propagamos la Excepcion
            raise
        else:
            # Cobramos al cliente y lo sacamos de la lista de cuentas abiertas -> datos_cl_cobrado = [cliente, pos_cl]
            pos_list_clientes = self.peluquerias[self.NUM_SUCUR].cobrar_cliente(emp, pos_cliente, ruc_factura, factura_gen)
            ## ACTUALIZAMOS LA BASE DE DATOS ##
            # Primeramente las facturas
            self.model.guardar_nueva_factura(factura_gen, self.NUM_SUCUR)
            # La lista de cuentas
            self.model.cerrar_cuenta_cliente(pos_cliente, self.NUM_SUCUR)
            # La lista de clientes
            self.model.guardar_fact_cliente_in_clientes(factura_gen, pos_list_clientes, self.NUM_SUCUR)
            # La lista de cajas
            self.model.actualizar_datos_caja(self.peluquerias[self.NUM_SUCUR].cajas[0], 0, self.NUM_SUCUR) # 0 -> Pos Caja

    def obtener_factura(self, num_fact):
        ''' Funcion que Obtiene una factura a traves de el numero de la misma '''
        if num_fact == '':
            raise Exception('NO INGRESO EL NUMERO DE FACTURA')
        # Obtenemos las facturas actualizadas
        self.peluquerias[self.NUM_SUCUR].facturas = self.model.obtener_facturas(self.NUM_SUCUR)
        # Vemos si el num de factura se encuentra dentro de la lista
        if (num_fact+1) > len(self.peluquerias[self.NUM_SUCUR].facturas):
            raise Exception('EL NUMERO DE COMPROBANTE NO EXISTE')
        else:
            factura = self.peluquerias[self.NUM_SUCUR].facturas[num_fact]
            # Retornamos la factura
            return factura

    def generar_factura(self, condicion_factura, items, ruc_cliente, formas_pago, emp):
        ''' Genera una nueva factura  para el caso de anulacion de una '''
        # Antes de realizar cualquier accion nos actualizamos
        self.peluquerias[self.NUM_SUCUR].clientes = self.model.obtener_clientes(self.NUM_SUCUR)
        # Generamos la factura: (condicion_factura, cod_items, ruc_cliente, formas_pago)
        cliente = self.peluquerias[self.NUM_SUCUR].verificar_cliente(ruc_cliente)
        # Preguntamos si encotro al cliente
        if cliente is None:
            raise Exception('NO ESTA REGISTRADO EL CLIENTE CON EL RUC: ' + str(ruc_cliente))
        # Generamos la factura: (condicion_factura, items, cliente, formas_pago)
        factura_nueva = self.peluquerias[self.NUM_SUCUR].cajas[0].generar_factura_anulacion(condicion_factura, items, cliente, formas_pago)
        # Retornamos la nueva factura
        return factura_nueva

    def anular_factura(self, num_factura, factura_gen):
        # Le damos el numero a la factura
        factura_gen.agregar_num_factura(num_factura+1)
        ## Realizamos el cambio en las facturas de la peluqueria ##
        # Actualizamos la caja #
        self.model.reemplazar_factura_anulada_caja(0, factura_gen, (num_factura+1), self.NUM_SUCUR) # 0 Numero de Caja
        # Actualizamos la lista de facturas #
        self.model.reemplazar_factura_anulada_pelu(factura_gen, num_factura, self.NUM_SUCUR)
        # Buscamos al cliente y lo actualizamos #
        pos_cl = self.peluquerias[self.NUM_SUCUR].verificar_num_pos_cliente(self.peluquerias[self.NUM_SUCUR].facturas[num_factura].cliente.ruc)
        self.model.reemplazar_factura_anulada_cliente(pos_cl, factura_gen, (num_factura+1), self.NUM_SUCUR)
        
    def obtener_caja(self, num_caja):
        ''' Funcion que retorna la caja solicitada '''
        # Obtenemos la informacion actualizada de la base de datos #
        try:
            caja = self.model.obtener_una_caja(num_caja, self.NUM_SUCUR)
        except:
            raise Exception('OCURRIO UN ERROR AL TRAER LA CAJA DE LA BASE DE DATOS')
        else:
            return caja
    
    def arquear_caja(self, num_caja):
        ''' Funcion que arquea una caja '''
        self.model.arquear_caja(num_caja, self.NUM_SUCUR)

    # FORMA MEJORADA
    def crear_formas_pago(self, opciones, montos, datos):
        formas_pago = []
        for i in range(len(opciones)):
            if opciones[i] == 'CHEQUE':
                ch = Cheque(montos[i], datos[i])
                formas_pago.append(ch)
            elif opciones[i] == 'EFECTIVO':
                efe = Efectivo(montos[i])
                formas_pago.append(efe)
            elif opciones[i] == 'TARJETA':
                tarj = Tarjeta(montos[i], datos[i])
                formas_pago.append(tarj)
            elif opciones[i] == 'TRANSFERENCIA':
                trans = Transferencia(montos[i], datos[i])
                formas_pago.append(trans)
            elif opciones[i] == 'USD':
                dolares = Dolar(montos[i])
                formas_pago.append(dolares)
        # Al terminar todo retornamos las formas de pago
        return formas_pago

    ### FUNCIONES EN CUANTO A LA ADMINISTRACION DE EMPLEADOS ###
    def crear_emp(self, emp, datos_emp):
        ''' Crear un Empleado con Usuario'''
        ##### DEBEMOS DE RECIBIR COMO PARAMETRO TODOS LOS DATOS DEL EMPLEADO ######
        ### Antes de realizar la accion obtenemos los datos actualizados de la BD ###
        try:
            # Verificamos que no este ningun campo vacio
            for dat in datos_emp:
                if dat == '':
                    raise Exception('NO DEBE DE HABER NINGUN CAMPO VACIO')
            # Actualizamos la lista de Empleados
            self.peluquerias[self.NUM_SUCUR].empleados = self.model.obtener_empleados(self.NUM_SUCUR)
            # Actualizamos la lista de Usuarios
            self.peluquerias[self.NUM_SUCUR].usuarios = self.model.obtener_usuarios(self.NUM_SUCUR)
            # Identacion de los datos recogidos:
            # datos_emp[0]: RUC/CEDULA ; datos_emp[1]: Nombre ; datos_emp[2]: Apellido ; datos_emp[6]: Tipo empleado
            # datos_emp[3]: Telefono ; datos_emp[4]: Direccion ; datos_emp[5]: Codigo Usuario
            ## Validamos que el codigo del usuario sea unico en la BD ##
            if self.peluquerias[self.NUM_SUCUR].verificar_codigo_usu(datos_emp[5]) is True:
                raise Exception('YA EXISTE UN USUARIO CON EL CODIGO: ' + datos_emp[5])
            ## Validamos que no exista un empleado con el mismo numero de cedula ##
            if self.peluquerias[self.NUM_SUCUR].verificar_empleado_unico(datos_emp[0]) is True:
                raise Exception('YA EXISTE UN EMPLEADO CON EL RUC: ' + datos_emp[0])
            ## Creamos y Guardamos el nuevo Empleado ##
            empleado_nuevo = self.peluquerias[self.NUM_SUCUR].crear_empleado(emp, datos_emp)
        except:
            raise # Propagamos la excepcion
        else:
            # Actualizamos la Base de Datos
            self.model.agregar_nuevo_empleado(empleado_nuevo, self.NUM_SUCUR)
            self.model.agregar_nuevo_usuario(empleado_nuevo.usuario, self.NUM_SUCUR)

    def mostrar_lista_empleados(self, emp):
        ''' Muestra la lista de emplados '''
        try:
            ## Antes de realizar la accion obtenemos los tados actualizados de la BD ##
            self.peluquerias[self.NUM_SUCUR].empleados = self.model.obtener_empleados(self.NUM_SUCUR)
            # Pasamos la lista de empleados a la vista para poder mostrar en pantalla
            return self.peluquerias[self.NUM_SUCUR].empleados
        except:
            raise # Propagamos la excepcion

    def admin_ganancia_emp(self, emp, list_tipo_ganancia, list_montos):
        ''' Funcion que puede alterar la lista de porcentajes de un empleado '''
        try:
            # Validamos los datos
            for i in range(len(list_montos)):
                # Transformamos los montos a float
                list_montos[i] = float(list_montos[i])
            # Buscamos la pos del empleado
            pos_emp = self.pos_emp_in_lista(emp)
            # Le pasamos a la base de datos para que nos actualice los datos
            self.model.actualizar_ganancia_emp(pos_emp, list_tipo_ganancia, list_montos, self.NUM_SUCUR)
        except:
            raise # Propagamos la excepcion

    def pagar_sueldo_emp(self, pos_emp):
        ''' Funcion que paga a un empleado el sueldo '''
        # Le pasamos al modelo la posicion y el paga el empleado
        self.model.pagar_sueldo_emp(pos_emp, self.NUM_SUCUR)

    def administrar_clientes(self):
        ''' Muestra el menu para administrar a los clientes '''
    
    # Funciones auxiliares #
    def mostrar_clientes(self):
        ''' Muestra los clientes '''
        pass

    def editar_clientes(self):
        ''' Edita los datos de un cliente '''
        pass

    def administrar_facturacion(self):
        ''' Muestra el menu para administrar las cajas y la facturacion '''
        pass

    def administrar_stock(self):
        ''' Muestra el menu para administrar el stock '''
        pass

    ### VERIFICADORES ###
    def ingreso_usu_emp(self, codigo_usuario):
        ### DEBEMOS DE RECIBIR EL USUSARIO PARA PODER PROCESARLO ###
        # Obtenemos la informacion actualizada de la base de datos
        self.peluquerias[self.NUM_SUCUR].empleados = self.model.obtener_empleados(self.NUM_SUCUR)
        self.peluquerias[self.NUM_SUCUR].usuarios = self.model.obtener_usuarios(self.NUM_SUCUR)
        # Verificamos al usuario
        try:
            if self.peluquerias[self.NUM_SUCUR].verificar_usuario(codigo_usuario) is False:
                raise Exception('NO EXISTE EL USUARIO')
            # Buscamos al empleado
            emp = self.peluquerias[self.NUM_SUCUR].verificar_empleado(codigo_usuario)
            if emp == None:
                raise Exception('NO SE ECONTRO, O HAY MAS DE UN MISMO EMPLEADO')
            else:
                return emp
        except:
            # Propagamos la excepcion
            raise

    def verificar_tipo_empleado_cobros(self, empleado):
        ''' Verifica los permisos correspondientes '''
        try:
            if isinstance(empleado, Cajero) is False:
                raise Exception('USTED NO ESTA AUTORIZADO\nA UTILIZAR ESTA FUNCION')
        except:
            raise # Propagamos la excecion

    def verificar_tipo_empleado_administracion(self, empleado):
        ''' Verifica los permisos correspondientes '''
        try:
            if isinstance(empleado, Administrador) is False:
                raise Exception('USTED NO ESTA AUTORIZADO\nA UTILIZAR ESTA FUNCION')
        except:
            raise # Propagamos la excecion

    def verificar_lista_cuentas(self):
        ''' Funcion que verifica si la lista de cuentas esta vacia '''
        try:
            # Actualizamos la lista de cuentas abiertas
            self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta = self.model.obtener_lista_cl_cuenta(self.NUM_SUCUR)
            # Vemos si la lista de cuentas esta vacia
            if len(self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta) == 0:
                raise Exception('NO HAY CLIENTES EN LA LISTA DE CUENTAS ABIERTAS\n')
        except:
            raise # Propagamos la excepcion

    def pos_emp_in_lista(self, emp):
        ''' Retorna la pos in lista del empleado '''
        pos_emp = [i for i in range(len(self.peluquerias[self.NUM_SUCUR].empleados)) if emp.ruc == self.peluquerias[self.NUM_SUCUR].empleados[i].ruc]
        return pos_emp[0]

    def emp_in_lista_ruc(self, ruc_emp):
        ''' Retorna la pos in lista del empleado y al empleado mismo'''
        # Buscamos al empleado
        pos_emp = [i for i in range(len(self.peluquerias[self.NUM_SUCUR].empleados)) if ruc_emp == self.peluquerias[self.NUM_SUCUR].empleados[i].ruc]
        # Preguntamos si encontro al empleado
        if len(pos_emp) == 0:
            raise Exception('NO EXISTE EL EMPLEADO CON EL RUC: ' + ruc_emp)
        elif len(pos_emp) != 1:
            raise Exception('HAY MAS DE UN EMPLEADO CON EL RUC: ' + ruc_emp)
        else:
            # Retornamos las posicion y al empleado
            lista_datos = [pos_emp[0], self.peluquerias[self.NUM_SUCUR].empleados[pos_emp[0]]]
            return lista_datos

    def validar_datos_fact(self, list_datos):
        ''' Verifica que todos los datos esten correctos para la creacion de una Factura '''
        # Sin Numero de Pos In Lista
        if list_datos[0] == 'SNPIL':
        # list_datos[0]: corresponde a la pos in lista 
            raise Exception('NO SE PUEDE CREAR LA FACTURA SIN LA CUENTA')
        # Vemos que tenga un cliente
        if list_datos[1] == '':
        # list_datos[1]: corresponde al ruc del cliente
            raise Exception('NO SE PUEDE CREAR LA FACTURA SI NO ESTA A NOMBRE DE UN CLIENTE')
        # Vemos que el tipo de factura no este vacio
        if list_datos[2] == '':
        # list_datos[2]: corresponde al tipo de factura
            raise Exception('NO SE PUEDE CREAR LA FACTURA\nSI NO SE ESPECIFICA EL TIPO DE LA MISMA')
        # Verificamos que exista el cliente
        cliente_a_agregar = self.peluquerias[self.NUM_SUCUR].verificar_cliente(list_datos[1])
        # Si no existe el cliente lanzamos una excepcion
        if cliente_a_agregar is None:
            raise Exception('NO EXISTE EL CLIENTE CON EL RUC: ' + list_datos[1])
        # Si su lista de items esta vacia lanzamos una excepcion
        if len(self.peluquerias[self.NUM_SUCUR].lista_clientes_cuenta[list_datos[0]].items_consumidos) == 0:
            raise Exception('NO PUEDE COBRAR AL CLIENTE\nPOR QUE NO TIENE NIGUN ITEM CARGADO')

    def obtener_items(self, codigos_items):
        ''' Busca los items de acuerdo a los codigos '''
        if len(codigos_items) == 0:
            raise Exception('LA LISTA DE CODIGOS DE ITEMS ESTA VACIA')
        # Buscamos los items
        items_a_agregar = [it for cod in codigos_items for it in self.peluquerias[self.NUM_SUCUR].items if it.codigo == cod]
        # Preguntamos si se encontraron todos los items
        if len(items_a_agregar) < len(codigos_items):
            raise Exception('NO SE ECONTRARON TODOS LOS ITEMS')
        # Preguntamos si es diferente
        elif len(items_a_agregar) != len(codigos_items):
            raise Exception('HAY CODIGOS DUPLICADOS EN LA BASE DE DATOS')
        else:
            # Si todo esta bien retornamos los items
            return items_a_agregar

    def calcular_total_pagar(self, items):
        ''' Calcula el total a pagar por los items '''
        # PROGRAMACION FUNCIONAL
        precios = (it.get_precio() for it in items) # Listas por Compresion
        return reduce(lambda x, y: x + y, precios) # Funcion Reduce y lambda

    def obtener_empleado(self, ruc_emp):
        ''' Funcion que obtiene al empleado '''
        # Actualizamos la lista de empleados
        self.peluquerias[self.NUM_SUCUR].empleados = self.model.obtener_empleados(self.NUM_SUCUR)
        # Buscamos al empleado
        empleado = [emp for emp in self.peluquerias[self.NUM_SUCUR].empleados if emp.ruc == ruc_emp]
        if len(empleado) == 1:
            return empleado[0]
        elif len(empleado) == 0:
            raise Exception('NO EXISTE EL EMPLEADO CON EL RUC: ' + ruc_emp)
        else:
            raise Exception('HAY MAS DE UN EMPLEADO CON EL RUC: ' + ruc_emp)
