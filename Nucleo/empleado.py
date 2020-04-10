# Importamos la libreria Abstrack Base Class
from abc import ABCMeta, abstractmethod
# Importamos la clase Usuario
from usuario import Usuario
# Importamos la libreria Functools
from functools import reduce
# Importamos la clase Cliente
from cliente import Cliente
# Importamos el validador de datos
from persona import validador_datos_personas
# Importamos todos los servicios y la clase Propina
from alarge import Alarge
from alisado import Alisado
from apliqueKeratina import ApliqueKeratina
from balayage import Balayage
from banhoTratamiento import BañoTratamiento
from barberia import Barberia
from brushing import Brushing
from corte import Corte
from decoloracion import Decoloracion
from depilacion import Depilacion
from duchaSolar import DuchaSolar
from extension import Extension
from facial import Facial
from lavado import  Lavado
from manicura import Manicura
from maquillaje import Maquillaje
from masaje import Masaje
from mecha import Mecha
from onda import Onda
from pedicura import Pedicura
from peinado import Peinado
from pestanha import Pestaña
from planchita import Planchita
from propina import Propina
from reflejo import Reflejo
from rulo import Rulo
from tinte import Tinte
from unha import Unha

# Comiezo de la clase Empleado
class Empleado(metaclass = ABCMeta):
    ''' Abstraccion que representa a un Empleado '''
    # Atributo estatico
    cant_empleados = 0
    
    # Metodos
    @validador_datos_personas
    def __init__(self, ruc, nombre, apellido, telefono, direccion):
        self.ruc = ruc
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.porcent_servicios = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.montos_fijos_servicios = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.items_realizados = []
        self.productos_vendidos = []
        self.sueldo = 0
        self.propina = 0
        self.usuario = Usuario(None)
        self.__class__.cant_empleados += 1

    # Metodos sobre el sueldo del empleado
    def colocar_porcent(self, porcentajes):
        ''' Coloca los porcentajes al empleado ''' 
        # Guardamos la lista entera de porcentajes
        self.porcent_servicios = porcentajes

    def agregar_items(self, items_agregados):
        ''' Agrega los items realizados por el empleado '''
        # Vamos agregando a la lista de items
        for item in items_agregados:
            self.items_realizados.append(item)

    # Metodos Propios
    def colocar_propina(self, monto_propina, cliente_dado):
        ''' Coloca la propina al empleado '''
        propina = Propina(cliente_dado)
        propina.colocar_total(monto_propina)
        self.propina += monto_propina
        self.items_realizados.append(propina)

    def calcular_sueldo(self):
        ''' Calcula el sueldo del empleado '''
        # PROGRAMACION FUNCIONAL
        # Diccionario de Servicios
        def switch(argument):
            switcher = {
                'ALARGE': 0,
                'ALISADO': 1,
                'APLIQUEKERATINA': 2,
                'BALAYAGE' : 3,
                'BAÑOTRATAMIENTO': 4,
                'BARBERIA' : 5,
                'BRUSHING': 6,
                'CORTE':  7,
                'DECOLORACION': 8,
                'DEPILACION': 9,
                'DUCHASOLAR': 10,
                'EXTENSION': 11,
                'FACIAL': 12,
                'LAVADO': 13,
                'MANICURA': 14,
                'MAQUILLAJE': 15,
                'MASAJE': 16,
                'MECHAS': 17,
                'ONDAS': 18,
                'PEDICURA': 19,
                'PEINADO': 20,
                'PESTAÑA': 21,
                'PLANCHITA': 22,
                'REFLEJO' : 23,
                'RULOS': 24,
                'TINTE' : 25,
                'UÑAS': 26
            }
            return switcher.get(argument, 20) # 2 Por que aplique keratina es = 0
            
        # Metodo principal #
        # Validamos que tenga algun item
        if len(self.items_realizados) == 0:
            raise Exception('EL EMPLEADO NO TIENE NINGUN TRABAJO HASTA LA FECHA')
        else:
            self.sueldo = 0
            ## GANANCIA POR COMICION ##
            # Utilizamos listas por comprension
            ganancia_comision = ((item.get_precio() * self.porcent_servicios[switch(item.obtener_clase())]) for item in self.items_realizados if self.porcent_servicios[switch(item.obtener_clase())]>0)
            # Sumamos la ganancia
            ganancia_cn = list(ganancia_comision)
            if len(ganancia_cn) == 1:
                self.sueldo += ganancia_cn[0]
            elif len(ganancia_cn) > 1:
                self.sueldo += reduce(lambda x, y: x+y, ganancia_cn) # Utilizamos lambda y reduce
            ## GANANCIA POR MONTO FIJO ##
            # Listas por comprension
            ganancia_monto = (self.montos_fijos_servicios[switch(item.obtener_clase())] for item in self.items_realizados if self.montos_fijos_servicios[switch(item.obtener_clase())]>0)
            # Sumamos la ganancia
            ganancia_mt = list(ganancia_monto)
            if len(ganancia_mt) == 1:
                self.sueldo += ganancia_mt[0]
            elif len(ganancia_mt) > 1:
                self.sueldo += reduce(lambda x, y: x+y, ganancia_mt) # Utilizamos lambda y reduce
            return int(reduce(lambda x, y: x + y, (self.sueldo, self.propina)))

    def cobrar_sueldo(self):
        ''' Accion de cobrar el sueldo, reinica el monto de sueldo '''
        self.sueldo = self.propina = 0
        self.items_realizados = []

    def abrir_cuenta_cliente(self, cliente):
        ''' Abre la cuenta de un cliente '''
        return cliente

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
        
    def crear_cliente(self, ruc, nombre, apellido, telefono, direccion):
        ''' Accion que crea un objeto "cliente" nuevo dentro del sistema'''
        cliente_nuevo = Cliente(ruc, nombre, apellido, telefono, direccion)
        return cliente_nuevo

    def crear_item(self, nombre_servicio, codigo, descripcion, precio_unitario):
        ''' Accion que crea un objeto item "nuevo" dentro del sistema '''
        # FUNCIONES PARA LA CREACION DE ITEMS
        def crear_lavado(codigo, descripcion, precio_unitario):
            nuevo_lavado = Lavado(codigo, descripcion, precio_unitario)
            return nuevo_lavado

        def crear_brushing(codigo, descripcion, precio_unitario):
            nuevo_brushing = Brushing(codigo, descripcion, precio_unitario)
            return nuevo_brushing
        
        def crear_baño_trat(codigo, descripcion, precio_unitario):
            nuevo_baño_trat = BañoTratamiento(codigo, descripcion, precio_unitario)
            return nuevo_baño_trat

        def crear_corte(codigo, descripcion, precio_unitario):
            nuevo_corte = Corte(codigo, descripcion, precio_unitario)
            return nuevo_corte

        def crear_barb(codigo, descripcion, precio_unitario):
            nuevo_barb = Barberia(codigo, descripcion, precio_unitario)
            return nuevo_barb

        def crear_alisado(codigo, descripcion, precio_unitario):
            nuevo_alisado = Alisado(codigo, descripcion, precio_unitario)
            return nuevo_alisado

        def crear_peinado(codigo, descripcion, precio_unitario):
            nuevo_peinado = Peinado(codigo, descripcion, precio_unitario)
            return nuevo_peinado

        def crear_depilacion(codigo, descripcion, precio_unitario):
            nuevo_depilacion = Depilacion(codigo, descripcion, precio_unitario)
            return nuevo_depilacion

        def crear_tinte(codigo, descripcion, precio_unitario):
            nuevo_tinte = Tinte(codigo, descripcion, precio_unitario)
            return nuevo_tinte

        def crear_balayage(codigo, descripcion, precio_unitario):
            nuevo_balayage = Balayage(codigo, descripcion, precio_unitario)
            return nuevo_balayage

        def crear_decoloracion(codigo, descripcion, precio_unitario):
            nuevo_decoloracion = Decoloracion(codigo, descripcion, precio_unitario)
            return nuevo_decoloracion

        def crear_aplique_kerat(codigo, descripcion, precio_unitario):
            nuevo_apl_keratina = ApliqueKeratina(codigo, descripcion, precio_unitario)
            return nuevo_apl_keratina

        def crear_pestaña(codigo, descripcion, precio_unitario):
            nuevo_pestaña = Pestaña(codigo, descripcion, precio_unitario)
            return nuevo_pestaña

        def crear_extension(codigo, descripcion, precio_unitario):
            nuevo_extraccion_ext = Extension(codigo, descripcion, precio_unitario)
            return nuevo_extraccion_ext        
        
        def crear_manicura(codigo, descripcion, precio_unitario):
            nueva_manicura = Manicura(codigo, descripcion, precio_unitario)
            return nueva_manicura

        def crear_alarge(codigo, descripcion, precio_unitario):
            nuevo_alarge = Alarge(codigo, descripcion, precio_unitario)
            return nuevo_alarge
        
        def crear_facial(codigo, descripcion, precio_unitario):
            nuevo_facial = Facial(codigo, descripcion, precio_unitario)
            return nuevo_facial

        def crear_masaje(codigo, descripcion, precio_unitario):
            nuevo_masaje = Masaje(codigo, descripcion, precio_unitario)
            return nuevo_masaje

        def crear_reflejo(codigo, descripcion, precio_unitario):
            nuevo_reflejo = Reflejo(codigo, descripcion, precio_unitario)
            return nuevo_reflejo

        def crear_pedicura(codigo, descripcion, precio_unitario):
            nueva_pedicura = Pedicura(codigo, descripcion, precio_unitario)
            return nueva_pedicura

        def crear_ducha_solar(codigo, descripcion, precio_unitario):
            nueva_ducha = DuchaSolar(codigo, descripcion, precio_unitario)
            return nueva_ducha

        def crear_maquillaje(codigo, descripcion, precio_unitario):
            nuevo_maquillaje = Maquillaje(codigo, descripcion, precio_unitario)
            return nuevo_maquillaje

        def crear_mecha(codigo, descripcion, precio_unitario):
            nueva_mecha = Mecha(codigo, descripcion, precio_unitario)
            return nueva_mecha

        def crear_onda(codigo, descripcion, precio_unitario):
            nueva_onda = Onda(codigo, descripcion, precio_unitario)
            return nueva_onda

        def crear_planchita(codigo, descripcion, precio_unitario):
            nueva_planchita = Planchita(codigo, descripcion, precio_unitario)
            return nueva_planchita

        def crear_rulo(codigo, descripcion, precio_unitario):
            nuevo_rulo = Rulo(codigo, descripcion, precio_unitario)
            return nuevo_rulo

        def crear_unha(codigo, descripcion, precio_unitario):
            nueva_unha = Unha(codigo, descripcion, precio_unitario)
            return nueva_unha

        def error(codigo, descripcion, precio_unitario):
            raise Exception('El Item con el codigo: ' + codigo + ' No se puede crear')

        # Diccionario de Servicios
        def switch(argument):
            switcher = {
                'ALARGE': crear_alarge,
                'ALISADO': crear_alisado,
                'APLIQUEKERATINA': crear_aplique_kerat,
                'BALAYAGE' : crear_balayage,
                'BAÑOTRATAMIENTO': crear_baño_trat,
                'BARBERIA' : crear_barb,
                'BRUSHING': crear_brushing,
                'CORTE':  crear_corte,
                'DECOLORACION': crear_decoloracion,
                'DEPILACION': crear_depilacion,
                'DUCHASOLAR': crear_ducha_solar,
                'EXTENSION': crear_extension,
                'FACIAL': crear_facial,
                'LAVADO': crear_lavado,
                'MANICURA': crear_manicura,
                'MAQUILLAJE': crear_maquillaje,
                'MASAJE': crear_masaje,
                'MECHAS': crear_mecha,
                'ONDAS': crear_onda,
                'PEDICURA': crear_pedicura,
                'PEINADO': crear_peinado,
                'PESTAÑA': crear_pestaña,
                'PLANCHITA': crear_planchita,
                'REFLEJO' : crear_reflejo,
                'RULOS': crear_rulo,
                'TINTE' : crear_tinte,
                'UÑAS': crear_unha
            }
            return switcher.get(argument, error)
            
        # Metodo Principal
        funcion = switch(nombre_servicio)
        return funcion(codigo, descripcion, precio_unitario)

    def crear_usuario(self, codigo_dado):
        ''' Crea y asigna un codigo para que pueda ser usuario '''
        self.usuario = Usuario(codigo_dado)

    def obtener_nombres(self):
        ''' Funcion que retorna el nombre y el apellido del empleado '''
        return self.nombre + ' ' + self.apellido

    # Metodos heredados
    @abstractmethod
    def obtener_datos(self, condicion):
        ''' Devuelve en forma de String los datos de un empleado '''
        pass

