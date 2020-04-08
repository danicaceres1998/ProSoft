# Importamos el path
from sys import path
path.append('./Nucleo')
# Importamos ZODB y transaction
from mizodb import MiZODB, transaction
# Importamos la clase Peluqueria
from peluqueria import Peluqueria # NO ES UN ERROR

# Clase principal
class Model: 
    ''' Clase que Persiste los objetos '''
    # Atributo estatico
    # Opcion con FileStorage
    #addr = './Data.fs'
    # Opcion con ClientStorage
    addr = 'localhost', 8090

    ### METODOS ###
    # Metodos Principales: Guardar, Listar y Actualizar
    def guardar_peluqueria(self, peluqueria):
        ''' Guarda el objeto recibido '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        dbroot = db.raiz
        # Guardamos el objeto
        dbroot[peluqueria.NUM_SUCUR] = peluqueria
        # Realizamos la transacsion y cerramos la base de datos
        transaction.commit()
        db.close()

    def devolver_peluqueria(self, num_sucur):
        ''' Devuelve la peluqueria de acuerdo al numero de sucrusal '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        dbroot = db.raiz
        # Obtenemos la peluqueria
        peluqueria = None
        for key in dbroot.keys():
            # Obtenemos el objeto de la lista
            objeto = dbroot[key]
            # Preguntamos si es del tipo Peluqueria
            if isinstance(objeto, Peluqueria):
                # Preguntamos si es la sucursal que queremos
                if int(objeto.NUM_SUCUR) == num_sucur:
                    peluqueria = objeto
        # Cerramos la base de datos
        db.close()
        # Transformamos a un objeto
        pelu_bd = Peluqueria()
        pelu_bd.clientes = peluqueria.clientes
        pelu_bd.empleados = peluqueria.empleados
        pelu_bd.usuarios = peluqueria.usuarios
        pelu_bd.cajas = peluqueria.cajas
        pelu_bd.facturas = peluqueria.facturas
        pelu_bd.items = peluqueria.items
        pelu_bd.marcas = peluqueria.marcas
        pelu_bd.proveedores = peluqueria.proveedores
        pelu_bd.lista_clientes_cuenta = peluqueria.lista_clientes_cuenta
        # Retornamos el objeto peluqueria
        return pelu_bd

    ### FUNCIONES QUE SE ENCARGAN DE UNA LISTA ENTERA DE LA BD ###
    def actualizar_clientes(self, clientes_act, num_sucur):
        ''' Actualiza la lista de clientes de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        peluqueria.clientes = clientes_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_empleados(self, emp_act, num_sucur):
        ''' Actualiza la lista de empleados de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de empleados
        peluqueria.empleados = emp_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_usuarios(self, usuarios_act, num_sucur):
        ''' Actualiza la lista de usuarios de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de usuarios
        peluqueria.usuarios = usuarios_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_cajas(self, cajas_act, num_sucur):
        ''' Actualiza las cajas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de cajas
        peluqueria.cajas = cajas_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_facturas(self, facturas_act, num_sucur):
        ''' Actualiza las facturas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de facturas
        peluqueria.facturas = facturas_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_items(self, items_act, num_sucur):
        ''' Actualiza los items de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de items
        peluqueria.items = items_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_marcas(self, marcas_act, num_sucur):
        ''' Actualiza las marcas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de marcas
        peluqueria.marcas = marcas_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_proveedores(self, proveedores_act, num_sucur):
        ''' Actualiza a los proveedores de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de proveedores
        peluqueria.proveedores = proveedores_act
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_lista_cl_cuenta(self, lista_cuentas, num_sucur):
        ''' Actualiza la lista de cuentas abiertas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        # Iniciamos la transaccion
        transaction.begin()
        # Actualizamos la lista de lista de cuentas
        peluqueria.lista_clientes_cuenta = lista_cuentas
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    ### FUNCIONES PARA GUARDAR ESPECIFICAMENTE ###
    def agregar_cl_in_cuentas(self, cliente, num_sucur):
        ''' Funcion que agrega un cliente a la lista de cuentas '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Agregamos al cliente en la lista de cuentas
        peluqueria.lista_clientes_cuenta.append(cliente)
        peluqueria.lista_clientes_cuenta = peluqueria.lista_clientes_cuenta
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def cerrar_cuenta_cliente(self, pos_in_lista, num_sucur):
        ''' Cierra la cuenta de un cliente '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Cerramos la cuenta
        peluqueria.lista_clientes_cuenta.pop(pos_in_lista)
        peluqueria.lista_clientes_cuenta = peluqueria.lista_clientes_cuenta
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def agregar_cliente_nuevo(self, cliente, num_sucur):
        ''' Funcion que agrega un cliente nuevo '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Agregamos al cliente en la lista de clientes
        peluqueria.clientes.append(cliente)
        peluqueria.clientes = peluqueria.clientes
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()  
    
    def actualizar_dat_cuenta_cl(self, pos_cl, items, num_sucur):
        ''' Actualiza los datos de una sola cuenta '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Actualizamos la cuenta
        peluqueria.lista_clientes_cuenta[pos_cl].cargar_items(items)
        peluqueria.lista_clientes_cuenta = peluqueria.lista_clientes_cuenta
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()  
    
    def guardar_fact_cliente_in_clientes(self, factura_nueva, pos_cliente, num_sucur):
        ''' Actualiza los datos del cliente '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Actualizamos al cliente
        peluqueria.clientes[pos_cliente].guardar_factura(factura_nueva)
        peluqueria.clientes = peluqueria.clientes
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_datos_caja(self, caja_act, pos_caja, num_sucur):
        ''' Actualizamos los datos de una caja '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Guardamos la caja
        peluqueria.cajas[pos_caja] = caja_act
        peluqueria.cajas = peluqueria.cajas
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def emplado_dat_actualizar(self, empleado, pos_in_lista, num_sucur):
        ''' Actuliza los datos de un solo empleado '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Actualizamos los datos del empleado
        peluqueria.empleados[pos_in_lista] = empleado
        peluqueria.empleados = peluqueria.empleados
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()  

    def guardar_nuevo_item(self, item, num_sucur):
        ''' Agregamos un nuevo item a la lista de items '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Agregamos el nuevo item
        peluqueria.items.append(item)
        peluqueria.items = peluqueria.items
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()  

    def guardar_nueva_factura(self, factura, num_sucur):
        ''' Guarda una nueva factura '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Guardamos la nueva factura
        peluqueria.facturas.append(factura)
        peluqueria.facturas = peluqueria.facturas
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()  
    
    def reemplazar_factura_anulada_pelu(self, factura_nueva, pos_factura, num_sucur):
        ''' Reemplaza la factura anulada en la lista de facturas de la Peluqueria'''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Reemplazamos la factura
        peluqueria.facturas[pos_factura] = factura_nueva
        peluqueria.facturas = peluqueria.facturas
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def reemplazar_factura_anulada_cliente(self, pos_cl, factura_nueva, num_factura, num_sucur):
        ''' Reemplaza la factura anulada para el cliente '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Eliminamos la factura del cliente
        for fact in peluqueria.clientes[pos_cl].facturas:
            if fact.num_factura == num_factura:
                peluqueria.clientes[pos_cl].facturas.remove(fact)
                break
        # Le agregamos la factura al nuevo cliente
        for cl in peluqueria.clientes:
            if cl.ruc == factura_nueva.cliente.ruc:
                cl.guardar_factura(factura_nueva)
                break
        peluqueria.clientes = peluqueria.clientes
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def reemplazar_factura_anulada_caja(self, pos_caja, factura_nueva, num_factura, num_sucur):
        ''' Reemplaza la factura anulada para la caja '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Cambiamos la factura de la caja
        index = 0
        for fact in peluqueria.cajas[pos_caja].facturas:
            if fact.num_factura == num_factura:
                # Guardamos las formas de pago
                form_pago = fact.formas_pago
                # Restamos la ganancia de la factura anulada
                for fp in form_pago:
                    if fp.obtener_tipo_pago() == 'CHEQUE':
                        peluqueria.cajas[pos_caja].total_cheque -= fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'EFECTIVO':
                        peluqueria.cajas[pos_caja].total_efectivo -= fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TARJETA':
                        peluqueria.cajas[pos_caja].total_tarjeta -= fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TRANSFERENCIA':
                        peluqueria.cajas[pos_caja].total_transfer -= fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'USD':
                        peluqueria.cajas[pos_caja].total_usd -= fp.obtener_monto()
                # Sumamos la ganancia de la factura nueva
                form_pago = factura_nueva.formas_pago
                for fp in form_pago:
                    if fp.obtener_tipo_pago() == 'CHEQUE':
                        peluqueria.cajas[pos_caja].total_cheque += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'EFECTIVO':
                        peluqueria.cajas[pos_caja].total_efectivo += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TARJETA':
                        peluqueria.cajas[pos_caja].total_tarjeta += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'TRANSFERENCIA':
                        peluqueria.cajas[pos_caja].total_transfer += fp.obtener_monto()
                    elif fp.obtener_tipo_pago() == 'USD':
                        peluqueria.cajas[pos_caja].total_usd += fp.obtener_monto()
                # Rompemos el ciclo
                break
            index += 1
        # Cambiamos la factura
        peluqueria.cajas[pos_caja].facturas[index] = factura_nueva
        peluqueria.cajas = peluqueria.cajas
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def arquear_caja(self, num_caja, num_sucur):
        ''' Arquea una caja especifica '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Realizamos el arqueo
        peluqueria.cajas[num_caja].arquear_caja()
        peluqueria.cajas = peluqueria.cajas
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def agregar_nuevo_empleado(self, empleado_nuevo, num_sucur):
        ''' Funcion que agrega un nuevo empleado '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Agregamos al empleado
        peluqueria.empleados.append(empleado_nuevo)
        peluqueria.empleados = peluqueria.empleados
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def agregar_nuevo_usuario(self, usuario_nuevo, num_sucur):
        ''' Funcion que agrega un nuevo Usuario '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Agregamos el nuevo usuario
        peluqueria.usuarios.append(usuario_nuevo)
        peluqueria.usuarios = peluqueria.usuarios
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def pagar_sueldo_emp(self, pos_emp, num_sucur):
        ''' Funcion que paga al usuario '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Pagamos al empleado
        peluqueria.empleados[pos_emp].cobrar_sueldo()
        peluqueria.empleados = peluqueria.empleados
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    def actualizar_ganancia_emp(self, pos_emp, list_tipo_ganancia, list_montos, num_sucur):
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los viejos datos
        peluqueria = dbroot[num_sucur]
        transaction.begin()
        # Realizamos los cambios
        for i in range(len(list_tipo_ganancia)):
            # Si es porcentaje cambia la lista de porcentajes
            if list_tipo_ganancia[i] == 'PORCENTAJE':
                peluqueria.empleados[pos_emp].porcent_servicios[i] = list_montos[i]
                # Colocamos 0 en el otro tipo de ganancia
                peluqueria.empleados[pos_emp].montos_fijos_servicios[i] = 0
            # Si es por monto fijo cambia la lista de montos fijos
            elif list_tipo_ganancia[i] == 'MONTO':
                peluqueria.empleados[pos_emp].montos_fijos_servicios[i] = list_montos[i]
                # Colocamos 0 en el otro tipo de ganancia
                peluqueria.empleados[pos_emp].porcent_servicios[i] = 0
            # Si es vacio, no cambia nada
            elif list_tipo_ganancia[i] == '':
                pass
        # Guardamos la lista de empleados
        peluqueria.empleados = peluqueria.empleados
        # Realizamos la transaccion y cerramos la conexion
        transaction.commit()
        db.close()

    ### FUNCIONES QUE SE ENCARGAN DE PROVEER DATOS AL SISTEMA ###
    def obtener_clientes(self, num_sucur):
        ''' Obtiene la lista de clientes de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_cl = list()
        for cl in peluqueria.clientes:
            list_cl.append(cl)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_cl

    def obtener_empleados(self, num_sucur):
        ''' Obtiene la lista de empleados de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_emp = list()
        for emp in peluqueria.empleados:
            list_emp.append(emp)
        # Cerramos la base de datos
        db.close() 
        # Retornamos la lista
        return list_emp

    def obtener_usuarios(self, num_sucur):
        ''' Obtiene la lista de usuarios de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_usu = list()
        for usu in peluqueria.usuarios:
            list_usu.append(usu)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_usu

    def obtener_cajas(self, num_sucur):
        ''' Obtiene las cajas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_caj = list()
        for cj in peluqueria.cajas:
            list_caj.append(cj)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_caj

    def obtener_una_caja(self, pos_caja, num_sucur):
        ''' Obtiene una caja de la base de datos '''
         # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Obtenemos la caja
        caja = peluqueria.cajas[pos_caja]
        # Cerramos la base de datos
        db.close()
        # Retornamos la caja
        return caja

    def obtener_facturas(self, num_sucur):
        ''' Obtiene las facturas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_fact = list()
        for fact in peluqueria.facturas:
            list_fact.append(fact)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_fact

    def obtener_facturas_caja(self, num_caja, num_sucur):
        ''' Devuelve todas las facturas de la caja '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_fact = list()
        for fact in peluqueria.cajas[num_caja].facturas:
            list_fact.append(fact)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_fact

    def obtener_items(self, num_sucur):
        ''' Obtiene los items de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_items = list()
        for itm in peluqueria.items:
            list_items.append(itm)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_items

    def obtener_marcas(self, num_sucur):
        ''' Obtiene las marcas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_marcas = list()
        for marca in peluqueria.marcas:
            list_marcas.append(marca)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_marcas

    def obtener_proveedores(self, num_sucur):
        ''' Obtiene a los proveedores de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        dbroot = db.raiz
        # Minimizamos el cache
        db.db.cacheMinimize()
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_prov = list()
        for cj in peluqueria.proveedores:
            list_prov.append(cj)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_prov

    def obtener_lista_cl_cuenta(self, num_sucur):
        ''' Obtiene la lista de cuentas abiertas de la Base de Datos '''
        # Establecemos la conexion con la base de datos
        db = MiZODB(self.addr)
        # Minimizamos el cache
        db.db.cacheMinimize()
        dbroot = db.raiz
        # Traemos los datos
        peluqueria = dbroot[num_sucur]
        # Los metemos dentro de una lista
        list_cl_cuenta = list()
        for cl_cuenta in peluqueria.lista_clientes_cuenta:
            list_cl_cuenta.append(cl_cuenta)
        # Cerramos la base de datos
        db.close()
        # Retornamos la lista
        return list_cl_cuenta
