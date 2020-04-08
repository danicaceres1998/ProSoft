# Importamos la clase persistent
from persistent import Persistent
# Importamos la clase Empresa
from empresa import Empresa
# Importamos al super administrador
from superAdministrador import SuperAdministrador
from caja import Caja

# Clase que hace el papel de modelo
class Peluqueria(Persistent, Empresa):
    ''' Abstraccion de una Peluqueria '''

    NUM_CAJA = 0
    NUM_SUCUR = 0

    # Metodos
    def __init__(self):
        self.clientes = []
        self.empleados = []
        self.usuarios = []
        self.cajas = []
        self.facturas = []
        self.items = []
        self.marcas = []
        self.proveedores = []
        self.lista_clientes_cuenta = []

    # Metodos propios
    ### METODOS QUE SON DE ATENDER AL CLIENTE ###
    def cuenta_abierta(self, cliente):
        ''' Verifica si ya esta abierta la cuenta del cliente '''
        # Utilizamos listas por compresion para buscar al cliente
        verificador = [cc for cc in self.lista_clientes_cuenta if cliente.ruc == cc.ruc]
        # Vemos si encontro
        if len(verificador) == 1:
            return True
        else:
            return False

    def cargar_cuenta_cliente(self, pos_emp, codigos):
        '''' A traves del Empleado se carga la cuenta de un cliente ''' 
        # Mediante el empleado se le cargan los items
        lista_items = self.empleados[pos_emp].cargar_cuenta_cliente(self.items, codigos)
        # Si no encontro todos los items me retornara una lista vacia
        if len(lista_items) == 0:
            # Retornamos una lista vacia para decirle al controlador que ocurrio un fallo
            return lista_items
        else:
            # Si todo salio bien retornamos la lista al controlador
            return lista_items

    def crear_cliente(self, empleado, lista_datos):
        ''' A traves del Empleado se crea un nuevo cliente '''
        # El empleado crea un cliente
        nuevo_cliente = empleado.crear_cliente(lista_datos[0], lista_datos[1], lista_datos[2], lista_datos[3], lista_datos[4])
        # Se retorna el cliente
        return nuevo_cliente

    def crear_item(self, empleado, lista_datos):
        ''' A traves del Empleado se crea un nuevo item '''
        # El empleado crea un nuevo item (servicio)
        nuevo_item = empleado.crear_item(lista_datos[0], lista_datos[1], lista_datos[2], lista_datos[3])
        # Retornamos el nuevo item
        return nuevo_item

    def generar_factura(self, condicion_factura, cuenta, ruc_factura, formas_pago):
        ''' Genera una factura '''
        pos_cl = self.verificar_num_pos_cliente(ruc_factura)
        cliente = self.clientes[pos_cl]
        try:
            # Generamos la factura (tipo_factura, items, cliente_factura, formas_pago)
            factura_nueva = self.cajas[self.NUM_CAJA].generar_factura(condicion_factura, cuenta.items_consumidos, cliente, formas_pago)       
        except:
            # Propagamos la excepcion
            raise
        else:
            # Agregamos a la lista de facturas de la peluqueria
            factura_nueva.agregar_num_factura(len(self.facturas)+1)
            # Retornamos la nueva factura
            return factura_nueva
        
    def cobrar_cliente(self, empleado, pos_in_lista_cl, ruc_factura, factura):
        ''' Accion de cobrar a un cliente '''
        pos_cliente = self.verificar_num_pos_cliente(ruc_factura)
        # Cobramos y damos la factura al cliente
        self.cajas[self.NUM_CAJA].cobrar_cliente(self.lista_clientes_cuenta, pos_in_lista_cl, empleado)
        # Retornamos la pos del cliente en la lista de clientes
        return pos_cliente

    def crear_empleado(self, empleado, datos_emp):
        ''' A traves de un SuperAdmin se crea un empleado '''
        ### Identacion de los datos recogidos ###
        # datos_emp[0]: RUC/CEDULA ; datos_emp[1]: Nombre ; datos_emp[2]: Apellido ; datos_emp[6]: Tipo empleado
        # datos_emp[3]: Telefono ; datos_emp[4]: Direccion ; datos_emp[5]: Codigo Usuario
        ## El empleado crea un cliente ##
        nuevo_emp = empleado.crear_empleado(datos_emp[6].upper(), datos_emp[5], 
        datos_emp[0], datos_emp[1], datos_emp[2], datos_emp[3], datos_emp[4])
        # Retornamos el nuevo empelado
        return nuevo_emp

    def admin_list_porcent_emp(self, emp, lista_porcent, ruc_emp):
        ''' Funcion que puede alterar la lista de porcentajes de un empleado '''
        
    def administrar_facturacion(self):
        ''' Metodo que permite administrar la facturacion '''
        pass

    def administrar_clientes(self):
        ''' Metodo que permite la administracion de los clientes '''
        pass

    def administrar_stock(self):
        ''' Metodo que permite eliminar, agregar y adminstrar el stock '''
        pass

    #### VERIFICACIONES DE EXISTENCIA ####
    def verificar_usuario(self, codigo_dado):
        ''' Verifica si existe el usuario '''
        # Utilizamos listas por compresion para buscar al usuario
        verificador = [usu.obtener_codigo() for usu in self.usuarios if usu.obtener_codigo() == codigo_dado]
        # Vemos si encontro
        if len(verificador) == 1:
            return True
        else:
            return False

    def verificar_empleado_unico(self, ruc_emp):
        ''' Verifica si ya existe un empleado con el mismo ruc '''
        # Utilizamos listas por comprension
        verificador = [emp for emp in self.empleados if emp.ruc == ruc_emp]
        if len(verificador) == 1:
            return True
        elif len(verificador) == 0:
            return False
        else:
            return True

    def verificar_empleado(self, codigo_usu):
        ''' Verifica si existe un empleado '''
        # Utilizamos listas por comprension para buscar al empleado
        verificador = [emp for emp in self.empleados if emp.usuario.obtener_codigo() == codigo_usu]
        if len(verificador) == 1:
            # Retornamos el empleado
            return verificador[0]
        else:
            # Retornamos vacio
            return None

    def verificar_cliente(self, ruc_cl):
        ''' Verifica si existe un cliente '''
        # Utilizamos listas por comprension para buscar al cliente
        verificador = [cl for cl in self.clientes if cl.ruc == ruc_cl]
        if len(verificador) == 1:
            # Retornamos al cliente
            return verificador[0]
        else:
            # Retornamos vacio
            return None

    def verificar_num_pos_cliente(self, ruc_cl):
        ''' Devuelve el numero de posicion en la lista de clientes de la peluqueria '''
        # Utilizamos listas por comprension para buscar al cliente
        pos_cl = [i for i in range(len(self.clientes)) if ruc_cl == self.clientes[i].ruc]
        return pos_cl[0]

    def cliente_existente(self, ruc):
        ''' Verifica si ya existe el cliente '''
        # Utilizamos listas por compresion para buscar al cliente
        verificador = [cl for cl in self.clientes if cl.ruc == ruc]
        # Vemos si encontro
        if len(verificador) == 1:
            return True
        else:
            return False

    def verificar_codigo_usu(self, codigo_usu):
        ''' Verifica que el codigo del usuario sea unico '''
        # Urilizamos listas por compresion para buscar al cliente
        verificador = [usu for usu in self.usuarios if usu.obtener_codigo() == codigo_usu]
        # Vemos si encontro otro codigo igual
        if len(verificador) == 1:
            return True
        else:
            return False

    def item_existente(self, codigo_item):
        ''' Verifica si ya existe un item '''
        # Utilizamos listas por compresion para buscar el item
        verificador = [it for it in self.items if it.codigo == codigo_item]
        # Vemos si encontro
        if len(verificador) == 1:
            return True
        else:
            return False
