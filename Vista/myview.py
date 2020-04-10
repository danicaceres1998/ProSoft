import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

## CONSTANTES ##
lista_servicios = ('ALARGE','ALISADO','APLIQUEKERATINA','BALAYAGE','BAÑOTRATAMIENTO','BARBERIA',
                'BRUSHING','CORTE','DECOLORACION','DEPILACION','DUCHASOLAR','EXTENSION','FACIAL','LAVADO',
                'MANICURA','MAQUILLAJE','MASAJE','MECHAS','ONDAS','PEDICURA', 'PEINADO','PESTAÑA','PLANCHITA',
                'REFLEJO','RULOS','TINTE','UÑAS')
lista_tipos_emp = ('ADMINISTRADOR','CAJERO','MANICURISTA','MAQUILLADORA','PELUQUERO','SUPERADMINISTRADOR')

## ClASES PROPIAS ##
class MyTk(tk.Tk):

    def __init__(self, titulo):
        super().__init__()
        self.title(titulo)
        self.geometry('1360x760')

class MyFrame(tk.Frame):

    def __init__(self, raiz, **options):
        super().__init__(raiz, **options)

class MyBoton (tk.Button):
    
    def __init__(self, raiz, **options):
        super().__init__(raiz, **options)
        self.config(bg='lightgray', highlightcolor='black', activeforeground='green', font='Times', cursor='hand2')
        self.config(font=('Arial',14))

class MyLabel(tk.Label):

    def __init__(self, raiz, **options):
        super().__init__(raiz, **options)
        self.config(fg='black', font=('Arial',16), anchor=tk.W)

class MyTable(ttk.Treeview):

    def __init__(self, root, **options):
        super().__init__(root, height=33)

class MyEntry(tk.Entry):
    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.var = tk.StringVar()
        self.config(justify=tk.CENTER, textvariable=self.var)
        self.var.trace_add("write", self.to_uppercase)
    
    def to_uppercase(self, *args):
        self.var.set(self.var.get().upper())

class MyEntryCodUsu(tk.Entry):
    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.config(justify=tk.CENTER)

## DIALOGOS PROPIOS ##
class MyDialogCodUsu(tk.Toplevel):
    def __init__(self, root, controlador, **options):
        def on_enter(event):
            self.put_emp_in(entry_code_usu.get())

        super().__init__(root, **options)
        self.geometry('350x100+500+200')
        self.title('Codigo de Usuario')
        # Variable a utilizar
        self.emp_retornar = None
        self.controlador = controlador
        self.root = root
        # Etiqueta
        label_1 = MyLabel(self, text='Codigo de Usuario')
        label_1.grid(row=2, column=1)
        # Entrada
        entry_code_usu = MyEntryCodUsu(self, show='*')
        entry_code_usu.grid(row=2, column=2)
        entry_code_usu.focus()
        # Boton de Confirmacion
        confirm_buttom = MyBoton(self, text='Ingresar', command=lambda: self.put_emp_in(entry_code_usu.get()))
        confirm_buttom.place(x=160, y=60)
        # Escuchamos si hay un enter
        self.bind('<Return>', on_enter)

    def show_emp(self):
        ''' Retorna el Objeto Empleado '''
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        if self.emp_retornar is None:
            raise Exception('NO EXISTE EL USUARIO')
        else:
            return self.emp_retornar

    def put_emp_in(self, cod_usu):
        try:
            # Buscamos al empleado
            self.emp_retornar = self.controlador.ingreso_usu_emp(cod_usu)
        except:
            # Le damos un valor Vacio
            self.emp_retornar = None
            # Destruimos la ventana
            self.destroy()
        else:
            # Destruimos la ventana
            self.destroy()

class MyDialogCreateClient(tk.Toplevel):
    def __init__(self, root, **options):
        # Funcion auxiliar
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('540x220+400+200')
        self.title('Datos del Cliente')
        # Variable
        self.list_data = ['']
        # Etiquetas
        label_info = MyLabel(self, text='Ingrese los Datos del Cliente:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        label_ruc = MyLabel(self, text='RUC/Cedula')
        label_ruc.grid(row=2, column=1)
        label_nombre = MyLabel(self, text='Nombre')
        label_nombre.grid(row=3, column=1)
        label_apellido = MyLabel(self, text='Apellido')
        label_apellido.grid(row=4, column=1)
        label_num_telef = MyLabel(self, text='Telefono')
        label_num_telef.grid(row=5, column=1)
        label_direccion = MyLabel(self, text='Direccion/Ciudad')
        label_direccion.grid(row=6, column=1)
        # Entradas de Texto
        self.entry_ruc = MyEntry(self)
        self.entry_ruc.grid(row=2, column=2)
        self.entry_ruc.focus()
        self.entry_nombre = MyEntry(self)
        self.entry_nombre.grid(row=3, column=2)
        self.entry_apellido = MyEntry(self)
        self.entry_apellido.grid(row=4, column=2)
        self.entry_num_telef = MyEntry(self)
        self.entry_num_telef.grid(row=5, column=2)
        self.entry_direccion = MyEntry(self)
        self.entry_direccion.grid(row=6, column=2)
        # Boton de Confirmacion
        confirm_buttom = MyBoton(self, text='Crear Cliente', command=lambda: on_enter(None))
        confirm_buttom.grid(row=8, column=2)
        # Escuchamos si hay un enter
        self.bind('<Return>', on_enter)

    def show_data(self):
        ''' Retorna el la lista de datos del cliente '''
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        list_datos = self.list_data
        return list_datos

    def save_data(self):
        ''' Funcion que guarda la lista de datos '''
        # Guardamos los datos
        self.list_data = [self.entry_ruc.get(), self.entry_nombre.get(), self.entry_apellido.get(), self.entry_num_telef.get(), self.entry_direccion.get()]
        # Destruimos la ventana
        self.destroy()

class MyDialogCreateItem(tk.Toplevel):
    def __init__(self, root, **options):
        # Metodo auxiliar
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('540x220+350+150')
        self.title('Datos del Item')
        # Variables
        self.tipo_item = tk.StringVar()
        self.list_datos = ['', '', '', 0]
        # Etiquetas
        label_info = MyLabel(self, text='Ingrese los Datos del Item:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        label_codigo = MyLabel(self, text='Codigo')
        label_codigo.grid(row=2, column=1)
        label_tipo_servicio = MyLabel(self, text='Tipo de Servicio')
        label_tipo_servicio.grid(row=3, column=1)
        label_precio = MyLabel(self, text='Precio Unitario')
        label_precio.grid(row=4, column=1)
        label_descripcion = MyLabel(self, text='Descripcion')
        label_descripcion.grid(row=5, column=1)
        label_espacio = MyLabel(self, text='Espacio')
        label_espacio.config(fg='white')
        label_espacio.grid(row=6, column=2)
        # Entradas de Texto
        self.entry_codigo = MyEntry(self)
        self.entry_codigo.grid(row=2, column=2)
        self.entry_codigo.focus()
        # Menu de Opciones
        option_list = lista_servicios
        self.option_menu = tk.OptionMenu(self, self.tipo_item, *option_list)
        self.option_menu.grid(row=3, column=2)
        # Entradas de texto
        self.entry_precio = MyEntry(self)
        self.entry_precio.grid(row=4, column=2)
        self.entry_descripcion = MyEntry(self)
        self.entry_descripcion.grid(row=5, column=2)
        
        # Boton de Confirmacion
        confirm_buttom = MyBoton(self, text='Crear Item', command=lambda: on_enter(None))
        confirm_buttom.grid(row=7, column=2)
        # Escuchamos si hay un enter
        self.bind('<Return>', on_enter)

    def save_data(self):
        ''' Guarda todos los datos correspondientes '''
        # Realizamos una validacion
        if self.entry_precio.get() == '':
            self.list_datos = ['', '', '', 0]
            self.destroy()
        else:
            try:
                # Vemos que sea de tipo numerico
                precio = int(self.entry_precio.get())
            except:
                # Si no lo es destruimos y pasamos los valores
                self.list_datos = [self.tipo_item.get(), self.entry_codigo.get(), self.entry_descripcion.get(), '']
                self.destroy()
            else:
                # Guardamos los datos
                self.list_datos = [self.tipo_item.get(), self.entry_codigo.get(), self.entry_descripcion.get(), precio]
                # Destruimos la ventana
                self.destroy()

    def show_data(self):
        ''' Retorna el Objeto Empleado '''
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        list_data = self.list_datos
        return list_data

class MyDialogChargeCl(tk.Toplevel):
    def __init__(self, root, list_cuentas, list_item, **options):
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('652x390+350+100')
        self.title('Ingreso de Codigos')
        self.focus_force()
        # Variables
        self.pos_cliente = None
        self.cuenta_cliente = tk.StringVar()
        self.tipo_servicio = tk.StringVar()
        self.list_codigos = list()
        self.list_final_datos = ['SNPIL', []]
        # Etiquetas
        label_info = MyLabel(self, text='Ingrese los Datos:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        label_nom_cliente = MyLabel(self, text='Cliente:')
        label_nom_cliente.grid(row=2, column=1)
        label_codigo_item = MyLabel(self, text='Codigo del item:')
        label_codigo_item.grid(row=3, column=1)
        label_cantidad = MyLabel(self, text='Cantidad:')
        label_cantidad.grid(row=2, column=3)
        label_tipo_serv = MyLabel(self, text='Tipo:')
        label_tipo_serv.grid(row=4, column=1)
        # Multi opciones
        # Lista de opciones
        option_list_cuentas = self.cargar_list_cuentas(list_cuentas)
        # Menu de opciones
        self.option_cuenta_cliente = tk.OptionMenu(self, self.cuenta_cliente, *option_list_cuentas)
        self.option_cuenta_cliente.grid(row=2, column=2)
        # Entradas
        self.entry_cod_item = MyEntry(self)
        self.entry_cod_item.grid(row=3, column=2)
        self.entry_cant_item = tk.Entry(self, justify=tk.CENTER, width=3)
        self.entry_cant_item.grid(row=3, column=3)
        # Multi opciones
        # Lista de opciones        
        option_list_serv = lista_servicios
        # Menu de opciones
        self.option_tipo_serv = tk.OptionMenu(self, self.tipo_servicio, *option_list_serv)
        self.option_tipo_serv.grid(row=4, column=2)
        # Botones
        boton_cargar_item = MyBoton(self, text='Cargar Item', command=lambda: self.cargar_item_cl(self.entry_cod_item.get(), self.entry_cant_item.get()))
        boton_cargar_item.grid(row=3, column=4)
        boton_buscar_serv = MyBoton(self, text='Buscar Servicio', command=lambda: self.buscar_servicio(self.tipo_servicio.get(), list_item))
        boton_buscar_serv.grid(row=4, column=3)
        # Tablas
        self.create_table_services()
        # Boton de Finalizacion
        boton_finalizar = MyBoton(self, text='FINALIZAR', command=self.save_data)
        boton_finalizar.config(font=('Times', 22))
        boton_finalizar.place(x=250, y=340)
        # Escuchamos si hay un enter
        self.bind('<Return>', on_enter)

    def cargar_list_cuentas(self, lista_cuentas):
        ''' Funcion que carga las cuentas dentro de una lista '''
        list_datos = ((str(i+1) + '. ' + lista_cuentas[i].nombre + ' ' + lista_cuentas[i].apellido + ' ' + lista_cuentas[i].ruc) for i in range(len(lista_cuentas)))
        return list_datos

    def cargar_item_cl(self, codigo_item, cant_item):
        ''' Funcion que guarda los codigos introducidos '''
        if codigo_item == '':
            return
        else:
            # Vemos la cantidad de veces
            try:
                cant_item = int(cant_item)
            except:
                # Guardamos el codigo
                self.list_codigos.append(codigo_item)
                # Reseteamos el entry
                self.entry_cod_item.delete(0, 'end')
            else:
                # Guardamos el codigo la cantidad de veces solicitada
                for _ in range(cant_item):
                    # Agregamos a la lista
                    self.list_codigos.append(codigo_item)
                # Reseteamos el entry de codigos y de cantidad
                self.entry_cod_item.delete(0, 'end')
                self.entry_cant_item.delete(0, 'end')

    def buscar_servicio(self, tipo_servicio, list_items):
        ''' Funcion que busca servicios y los coloca en una talba '''
        # Reiniciamos la tabla
        self.tabla_servicios.destroy()
        self.create_table_services()
        # Listas por comprension
        servicios_filtrados = (item for item in list_items if tipo_servicio == item.obtener_clase())
        # Cargamos la tabla
        for servicio in servicios_filtrados:
            self.tabla_servicios.insert('', tk.END, text=servicio.codigo, values=(servicio.descripcion, servicio.precio_unitario))

    def save_data(self):
        ''' Funcion que guarda todos los datos y destruye la ventana '''
        # Extraemos la pos del cliente
        cuenta = self.cuenta_cliente.get()
        try:
            pos_cl = int(cuenta[0]) - 1
        except:
            # SNPIL: Sin Numero de Pos In Lista
            pos_cl = 'SNPIL'
        else:
            # Guardamos la Pos-In-Lista y la lista de codigos
            self.list_final_datos = [pos_cl, self.list_codigos]
            # Destuimos la ventana
            self.destroy()

    def create_table_services(self):
        ''' Funcion que crea la tabla de servicios '''
        self.tabla_servicios = MyTable(self)
        self.tabla_servicios.config(height=10)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_servicios['columns'] = ('one', 'two')
        self.tabla_servicios.column('#0', width=150, minwidth=150)
        self.tabla_servicios.column('one', width=260, minwidth=260)
        self.tabla_servicios.column('two', width=220, minwidth=220)
        # Personalizamos los encabezados
        self.tabla_servicios.heading('#0', text='Codigo', anchor=tk.W)
        self.tabla_servicios.heading('one', text='Descripcion', anchor=tk.W)
        self.tabla_servicios.heading('two', text='Precio', anchor=tk.W)
        # Colocamos la tabla
        self.tabla_servicios.place(x=10, y=120)

    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        list_data = self.list_final_datos
        return list_data

class MyDialogDatFactura(tk.Toplevel):
    def __init__(self, root, list_cuentas, **options):
        # Metodos auxiliares
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('500x190+400+200')
        self.title('Datos Factura')
        self.focus_force()
        # Variables
        self.type_factura = tk.StringVar()
        self.cuenta_cliente = tk.StringVar()
        self.list_final_datos = ['SNPIL', '', '']
        # Etiquetas
        label_info = MyLabel(self, text='Datos de la Factura:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        label_cuenta_cliente = MyLabel(self, text='Cuenta:')
        label_cuenta_cliente.grid(row=2, column=1)
        label_ruc_cliente = MyLabel(self, text='RUC del Cliente:')
        label_ruc_cliente.grid(row=3, column=1)
        label_tipo_factura = MyLabel(self, text='Tipo de Factura:')
        label_tipo_factura.grid(row=4, column=1)
        label_espacio = MyLabel(self, text='Espacio')
        label_espacio.config(fg='white')
        label_espacio.grid(row=5, column=2)
        # Multi opciones
        # Lista de opciones
        option_list_cuentas = self.cargar_list_cuentas(list_cuentas)
        # Menu de opciones
        self.option_cuenta_cliente = tk.OptionMenu(self, self.cuenta_cliente, *option_list_cuentas)
        self.option_cuenta_cliente.grid(row=2, column=2)
        # Entradas
        self.entry_ruc_cliente = MyEntry(self)
        self.entry_ruc_cliente.grid(row=3, column=2)
        # Multi opciones
        # Lista de opciones
        option_list_type_facturas = ('CONTADO', 'CREDITO')
        # Menu de opciones
        self.option_tipo_factura = tk.OptionMenu(self, self.type_factura, *option_list_type_facturas)
        self.option_tipo_factura.grid(row=4, column=2)
        # Botones
        boton_cobrar_cliente = MyBoton(self, text='Cobrar Cliente', command=self.save_data)
        boton_cobrar_cliente.config(font=('Times', 18))
        boton_cobrar_cliente.grid(row=6, column=2)
        self.bind('<Return>', on_enter)

    def cargar_list_cuentas(self, lista_cuentas):
        ''' Funcion que carga las cuentas dentro de una lista '''
        list_datos = ((str(i+1) + '. ' + lista_cuentas[i].nombre + ' ' + lista_cuentas[i].apellido + ' ' + lista_cuentas[i].ruc) for i in range(len(lista_cuentas)))
        return list_datos

    def save_data(self):
        ''' Funcion que guarda todos los datos y destruye la ventana '''
        # Extraemos la pos del cliente
        cuenta = self.cuenta_cliente.get()
        try:
            pos_cl = int(cuenta[0]) - 1
        except:
            # SNPIL: Sin Numero de Pos In Lista
            pos_cl = 'SNPIL'
        else:
            # Preguntamos que tipo de factura quiere el Cliente
            if self.type_factura.get() == 'CONTADO':
                self.type_factura = True
            elif self.type_factura.get() == 'CREDITO' :
                self.type_factura = False
            else:
                self.type_factura = ''
            # Guardamos la Pos-In-Lista, el ruc y el tipo de factura
            self.list_final_datos = [pos_cl, self.entry_ruc_cliente.get(), self.type_factura]
            # Destuimos la ventana
            self.destroy()

    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        # Retornamos los datos
        list_data = self.list_final_datos
        return list_data

class MyDialogShowFact(tk.Toplevel):
    def __init__(self, root, cliente, **options):
        # Metodos auxiliares
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('695x375+350+150')
        self.title('Datos Factura')
        self.focus_force()
        # Variables
        self.list_formas_pago = []
        self.check_efectivo = tk.BooleanVar(self)
        self.check_tarjeta = tk.BooleanVar(self)
        self.check_cheque = tk.BooleanVar(self)
        self.check_transferencia = tk.BooleanVar(self)
        self.check_usd = tk.BooleanVar(self)
        self.tabla_servicios = None
        # Etiquetas
        label_info = MyLabel(self, text='Items Consumidos por: ' + cliente.nombre + ' ' + cliente.apellido)
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        # Tabla
        # Le pasamos la lista de items que consumio
        self.create_table_services(cliente.items_consumidos)
        # Etiquetas
        label_deuda_total = MyLabel(self, text='Deuda Total: ' + str(cliente.calcular_deuda()))
        label_deuda_total.config(fg='black', font=('Arial',20))
        label_deuda_total.place(x=20, y=240)
        label_formas_pago = MyLabel(self, text='Formas de Pago:')
        label_formas_pago.config(fg='black', font=('Arial',20))
        label_formas_pago.place(x=20, y=270)
        # Check List
        self.boton_efectivo = ttk.Checkbutton(self, text='Efectivo', variable=self.check_efectivo, cursor='hand2')
        self.boton_efectivo.place(x=190, y=274)
        self.boton_tarjeta = ttk.Checkbutton(self, text='Tarjeta', variable=self.check_tarjeta, cursor='hand2')
        self.boton_tarjeta.place(x=300, y=274)
        self.boton_cheque = ttk.Checkbutton(self, text='Cheque', variable=self.check_cheque, cursor='hand2')
        self.boton_cheque.place(x=400, y=274)
        self.boton_transferencia = ttk.Checkbutton(self, text='Transferencia', variable=self.check_transferencia, cursor='hand2')
        self.boton_transferencia.place(x=500, y=274)
        self.boton_usd = ttk.Checkbutton(self, text='USD', variable=self.check_usd, cursor='hand2')
        self.boton_usd.place(x=630, y=274)
        # Botones
        boton_cobrar_cliente = MyBoton(self, text='Generar Factura', command=self.save_data)
        boton_cobrar_cliente.config(font=('Times', 22))
        boton_cobrar_cliente.place(x=270, y=320)
        # Escuchamos si no hay algun enter
        self.bind('<Return>', on_enter)

    def create_table_services(self, list_items):
        ''' Funcion que crea la tabla de servicios '''
        self.tabla_servicios = MyTable(self)
        self.tabla_servicios.config(height=10)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_servicios['columns'] = ('one', 'two')
        self.tabla_servicios.column('#0', width=150, minwidth=150)
        self.tabla_servicios.column('one', width=280, minwidth=280)
        self.tabla_servicios.column('two', width=240, minwidth=240)
        # Personalizamos los encabezados
        self.tabla_servicios.heading('#0', text='CODIGO', anchor=tk.W)
        self.tabla_servicios.heading('one', text='DESCRIPCION', anchor=tk.W)
        self.tabla_servicios.heading('two', text='PRECIO', anchor=tk.W)
        # Colocamos la tabla
        self.tabla_servicios.place(x=12, y=40)
        # Cargamos la tabla
        for item in list_items:
            self.tabla_servicios.insert('', tk.END, text=item.codigo, values=(item.descripcion, item.precio_unitario))

    def save_data(self):
        ''' Funcion que guarda todos los datos '''
        # Preguntamos si quiere el pago en efectivo
        if self.check_efectivo.get() is True:
            self.list_formas_pago.append('EFECTIVO')
        # Preguntamos si quiere el pago en tarjeta
        if self.check_tarjeta.get() is True:
            self.list_formas_pago.append('TARJETA')
        # Preguntamos si quiere el pago en cheque
        if self.check_cheque.get() is True:
            self.list_formas_pago.append('CHEQUE')
        # Preguntamos si quiere el pago con transferencia
        if self.check_transferencia.get() is True:
            self.list_formas_pago.append('TRANSFERENCIA')
        # Preguntamos si quiere el pago en USD
        if self.check_usd.get() is True:
            self.list_formas_pago.append('USD')
        # Preguntamos si esta vacia la lista de formas de pago
        if len(self.list_formas_pago) == 0:
            # Imprimimos un error
            messagebox.showerror('ERROR', 'SE DEBE DE ELEGIR AL MENOS UNA FORMA DE PAGO')
            # Volvemos al menu
            return
        else:
            # Destruimos la ventana
            self.destroy()

    def show_data(self):
        ''' Funcion que devuelve todos los datos tomados '''
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        # Retornamos los datos
        list_data = self.list_formas_pago
        return list_data

class MyDialogFormPagoVarios(tk.Toplevel):
    def __init__(self, root, forma_pago, **options):
        # Metodos auxiliares
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('480x140+400+200')
        self.title('Datos Factura')
        self.focus_force()
        # Variables
        self.list_datos = ['', '']
        self.forma_pago = forma_pago
        self.monto = 0
        self.dato_pago = None
        self.entry_monto = None
        self.entry_dato_pago = None
        # Etiqueta
        label_info = MyLabel(self, text='Ingrese los Datos:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1) 
        if forma_pago == 'EFECTIVO':
            # Etiquetas
            label_monto = MyLabel(self, text='Ingrese el Monto a Pagar en Efectivo:')
            label_monto.grid(row=2, column=1)
            # Entradas
            self.entry_dato_pago = tk.StringVar()
            self.entry_dato_pago.set('')
            self.entry_monto = MyEntry(self)
            self.entry_monto.grid(row=2, column=2)
        elif forma_pago == 'TARJETA':
            # Etiquetas
            label_dato_pago = MyLabel(self, text='Ingrese el Codigo del Voucher:')
            label_dato_pago.grid(row=2, column=1)
            label_monto = MyLabel(self, text='Ingrese el Monto a Pagar en Tarjeta:')
            label_monto.grid(row=3, column=1)
            # Entradas
            self.entry_dato_pago = MyEntry(self)
            self.entry_dato_pago.grid(row=2, column=2)
            self.entry_monto = MyEntry(self)
            self.entry_monto.grid(row=3, column=2)
        elif forma_pago == 'CHEQUE':
            # Etiquetas
            label_dato_pago = MyLabel(self, text='Ingrese el numero de Cheque:')
            label_dato_pago.grid(row=2, column=1)
            label_monto = MyLabel(self, text='Ingrese el Monto a Pagar con Cheque:')
            label_monto.grid(row=3, column=1)
            # Entradas
            self.entry_dato_pago = MyEntry(self)
            self.entry_dato_pago.grid(row=2, column=2)
            self.entry_monto = MyEntry(self)
            self.entry_monto.grid(row=3, column=2)
        elif forma_pago == 'TRANSFERENCIA':
            # Etiquetas
            label_dato_pago = MyLabel(self, text='Ingrese el Codigo de Transferencia:')
            label_dato_pago.grid(row=2, column=1)
            label_monto = MyLabel(self, text='Ingrese el Monto a pagar con Transferencia:')
            label_monto.grid(row=3, column=1)
            # Entradas
            self.entry_dato_pago = MyEntry(self)
            self.entry_dato_pago.grid(row=2, column=2)
            self.entry_monto = MyEntry(self)
            self.entry_monto.grid(row=3, column=2)
        elif forma_pago == 'USD':
            # Etiquetas
            label_monto = MyLabel(self, text='Ingrese el Monto a Pagar en USD:')
            label_monto.grid(row=2, column=1)
            # Entradas
            self.entry_dato_pago = tk.StringVar()
            self.entry_dato_pago.set('')
            self.entry_monto = MyEntry(self)
            self.entry_monto.grid(row=2, column=2)
        # Boton
        boton_continuar = MyBoton(self, text='Continuar', command=self.save_data)
        boton_continuar.config(font=('Times', 16))
        boton_continuar.grid(row=4, column=2)
        # Escuchamos si no hay algun enter
        self.bind('<Return>', on_enter)

    def save_data(self):
        ''' Guarda las formas de pago en una lista '''
        # Realizamos las validaciones
        if self.forma_pago != 'EFECTIVO':
            # Preguntamos si esta vacio
            if self.forma_pago != 'USD' and self.entry_dato_pago.get() == '':
                # Mostramos el error y volvemos al menu
                messagebox.showerror('ERROR', 'DEBE DE COLOCAR EL DATO DEL PAGO')
                return
        try:
            self.monto = int(self.entry_monto.get())
        except:
            # Mostramos el error y volvemos al menu
            messagebox.showerror('ERROR', 'EL MONTO NO ES NUMERICO')
            return
        else:
            # Guardamos los datos
            self.list_datos = [self.entry_dato_pago.get(), self.monto]
            # Destruimos la ventana
            self.destroy()
    
    def show_data(self):
        ''' Retorna la lista de datos de la forma de pago '''
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        list_data = self.list_datos
        return list_data

class MyDialogFormPagoUnico(tk.Toplevel):
    def __init__(self, root, forma_pago, **options):
        # Metodos auxiliares
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('440x140+400+200')
        self.title('Datos Factura')
        self.focus_force()
        # Variables
        self.dato_pago = None
        self.entry_dato_pago = None
        self.forma_pago = forma_pago
        # Etiqueta
        label_info = MyLabel(self, text='Ingrese los Datos:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1) 
        if forma_pago == 'TARJETA':
            # Etiquetas
            label_dato_pago = MyLabel(self, text='Ingrese el codigo del Voucher:')
            label_dato_pago.grid(row=2, column=1)
            # Entradas
            self.entry_dato_pago = MyEntry(self)
            self.entry_dato_pago.grid(row=2, column=2)
        elif forma_pago == 'CHEQUE':
            # Etiquetas
            label_dato_pago = MyLabel(self, text='Ingrese el numero de Cheque:')
            label_dato_pago.grid(row=2, column=1)
            # Entradas
            self.entry_dato_pago = MyEntry(self)
            self.entry_dato_pago.grid(row=2, column=2)
        elif forma_pago == 'TRANSFERENCIA':
            # Etiquetas
            label_dato_pago = MyLabel(self, text='Ingrese el codigo de Transferencia:')
            label_dato_pago.grid(row=2, column=1)
            # Entradas
            self.entry_dato_pago = MyEntry(self)
            self.entry_dato_pago.grid(row=2, column=2)
        elif forma_pago == 'USD':
            label_dato_pago = MyLabel(self, text='Ingrese el monto en USD:')
            label_dato_pago.grid(row=2, column=1)
            # Entradas
            self.entry_dato_pago = MyEntry(self)
            self.entry_dato_pago.grid(row=2, column=2)
        # Boton
        boton_continuar = MyBoton(self, text='Continuar', command=self.save_data)
        boton_continuar.config(font=('Times', 16))
        boton_continuar.grid(row=3, column=2)
        # Escuchamos si no hay algun enter
        self.bind('<Return>', on_enter)

    def save_data(self):
        ''' Guarda la forma de pago '''
        # Preguntamos si cargo el dato del pago
        if self.entry_dato_pago.get() == '':
            # Si no cargo mostramos un error y volvemos al menu
            messagebox.showerror('ERROR', 'DEBE DE COLOCAR EL DATO DEL PAGO')
            return
        else:
            if self.forma_pago == 'USD':
                try:
                    # Guardamos y salimos
                    self.dato_pago = int(self.entry_dato_pago.get())
                    self.destroy()
                except:
                    # Mostramos el error
                    messagebox.showerror('ERROR', 'EL MONTO NO ES NUMERICO')
                    return
            else:
                # Guardamos y salimos
                self.dato_pago = self.entry_dato_pago.get()
                self.destroy()
    
    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        pago_dato = self.dato_pago
        return pago_dato

class MyDialogGetInfo(tk.Toplevel):
    def __init__(self, root, titulo, mensaje, **options):
        # Funcion auxiliar
        def on_enter(event):
            self.save_data(entry_info.get())
        # Metodo Principal #
        super().__init__(root, **options)
        self.geometry('500x100+400+200')
        self.title(titulo)
        # Variable a utilizar
        self.info_requerida = ''
        # Etiqueta
        label_1 = MyLabel(self, text=mensaje)
        label_1.grid(row=2, column=1)
        label_espacio = MyLabel(self, text='espacio')
        label_espacio.config(fg='white')
        label_espacio.grid(row=3, column=2)
        # Entrada
        entry_info = MyEntry(self)
        entry_info.grid(row=2, column=2)
        entry_info.focus()
        # Boton de Confirmacion
        confirm_buttom = MyBoton(self, text='Continuar', command=lambda: self.save_data(entry_info.get()))
        confirm_buttom.grid(row=4, column=2)
        # Escuchamos si hay un enter
        self.bind('<Return>', on_enter)

    def show_data(self):
        ''' Retorna el Objeto Empleado '''
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        return self.info_requerida

    def save_data(self, codigo_dado):
        # Si esta vacio
        if codigo_dado == '':
            messagebox.showerror('ERROR', 'DEBE DE INTRODUCIR EL DATO SOLICITADO')
            return
        # Guardamos el codigo
        self.info_requerida = codigo_dado
        # Destruuimos la ventana
        self.destroy()

class MyDialogDetalleFact(tk.Toplevel):
    def __init__(self, root, factura, **options):
        def on_enter(event):
            self.save_data()
        super().__init__(root, **options)
        self.geometry('700x320+350+150')
        self.title('Datos Factura')
        self.focus_force()
        # Variables
        self.respuesta = False
        # Etiquetas
        label_info = MyLabel(self, text='Factura de: ' + factura.cliente.nombre + ' ' + factura.cliente.apellido)
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        # Tabla
        # Le pasamos la lista de items que consumio
        self.create_table_services(factura.items)
        # Etiquetas
        label_deuda_total = MyLabel(self, text='Deuda Total: ' + str(factura.calcular_total_pagar()))
        label_deuda_total.config(fg='black', font=('Arial',20))
        label_deuda_total.place(x=20, y=240)
        boton_anular_fact = MyBoton(self, text='Anular Factura', command=self.save_data)
        boton_anular_fact.config(font=('Times', 22))
        boton_anular_fact.place(x=270, y=270)
        # Escuchamos si no hay algun enter
        self.bind('<Return>', on_enter)

    def create_table_services(self, items):
        ''' Funcion que crea la tabla de servicios '''
        self.tabla_servicios = MyTable(self)
        self.tabla_servicios.config(height=10)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_servicios['columns'] = ('one', 'two')
        self.tabla_servicios.column('#0', width=150, minwidth=150)
        self.tabla_servicios.column('one', width=280, minwidth=280)
        self.tabla_servicios.column('two', width=240, minwidth=240)
        # Personalizamos los encabezados
        self.tabla_servicios.heading('#0', text='CODIGO', anchor=tk.W)
        self.tabla_servicios.heading('one', text='DESCRIPCION', anchor=tk.W)
        self.tabla_servicios.heading('two', text='PRECIO', anchor=tk.W)
        # Colocamos la tabla
        self.tabla_servicios.place(x=12, y=40)
        # Cargamos la tabla
        for item in items:
            self.tabla_servicios.insert('', tk.END, text=item.codigo, values=(item.descripcion, item.precio_unitario))

    def save_data(self):
        res = messagebox.askyesno('Anular Factura', '¿Desea Anular la factura?')
        self.respuesta = res
        self.destroy()

    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        return self.respuesta

class MyDialogGetFactNew(tk.Toplevel):
    def __init__(self, root, list_item, **options):
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('695x460+350+100')
        self.title('Factura Nueva')
        self.focus_force()
        # Variables
        self.ruc_cliente = None
        self.tipo_servicio = tk.StringVar()
        self.type_factura = tk.StringVar()
        self.list_codigos = list()
        self.list_final_datos = ['SRUC', [], [], False]
        # Variables de las formas de pago
        self.list_formas_pago = []
        self.check_efectivo = tk.BooleanVar(self)
        self.check_tarjeta = tk.BooleanVar(self)
        self.check_cheque = tk.BooleanVar(self)
        self.check_transferencia = tk.BooleanVar(self)
        self.check_usd = tk.BooleanVar(self)
        # Etiquetas
        label_info = MyLabel(self, text='Ingrese los Datos:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        label_ruc_cliente = MyLabel(self, text='RUC Cliente:')
        label_ruc_cliente.grid(row=2, column=1)
        label_codigo_item = MyLabel(self, text='Codigo del item:')
        label_codigo_item.grid(row=3, column=1)
        label_cantidad = MyLabel(self, text='Cantidad:')
        label_cantidad.grid(row=2, column=3)
        label_tipo_serv = MyLabel(self, text='Tipo:')
        label_tipo_serv.grid(row=4, column=1)
        # Entradas
        self.entry_ruc_cliente = MyEntry(self)
        self.entry_ruc_cliente.grid(row=2, column=2)
        self.entry_cod_item = MyEntry(self)
        self.entry_cod_item.grid(row=3, column=2)
        self.entry_cant_item = tk.Entry(self, justify=tk.CENTER, width=3)
        self.entry_cant_item.grid(row=3, column=3)
        # Multi opciones
        # Lista de opciones        
        option_list_serv = lista_servicios
        # Menu de opciones
        self.option_tipo_serv = tk.OptionMenu(self, self.tipo_servicio, *option_list_serv)
        self.option_tipo_serv.grid(row=4, column=2)
        # Botones
        boton_cargar_item = MyBoton(self, text='Cargar Item', command=lambda: self.cargar_item_cl(self.entry_cod_item.get(), self.entry_cant_item.get()))
        boton_cargar_item.grid(row=3, column=4)
        boton_buscar_serv = MyBoton(self, text='Buscar Servicio', command=lambda: self.buscar_servicio(self.tipo_servicio.get(), list_item))
        boton_buscar_serv.grid(row=4, column=3)
        # Tablas
        self.create_table_services()
        # Check List
        label_formas_pago = MyLabel(self, text='Formas de Pago:')
        label_formas_pago.config(fg='black', font=('Arial',20))
        label_formas_pago.place(x=20, y=330)
        self.boton_efectivo = ttk.Checkbutton(self, text='Efectivo', variable=self.check_efectivo, cursor='hand2')
        self.boton_efectivo.place(x=190, y=334)
        self.boton_tarjeta = ttk.Checkbutton(self, text='Tarjeta', variable=self.check_tarjeta, cursor='hand2')
        self.boton_tarjeta.place(x=300, y=334)
        self.boton_cheque = ttk.Checkbutton(self, text='Cheque', variable=self.check_cheque, cursor='hand2')
        self.boton_cheque.place(x=400, y=334)
        self.boton_transferencia = ttk.Checkbutton(self, text='Transferencia', variable=self.check_transferencia, cursor='hand2')
        self.boton_transferencia.place(x=500, y=334)
        self.boton_usd = ttk.Checkbutton(self, text='USD', variable=self.check_usd, cursor='hand2')
        self.boton_usd.place(x=630, y=334)
        # Lista de opciones
        option_list_type_facturas = ('CONTADO', 'CREDITO')
        # Menu de opciones de tipo de Factura
        label_tipo_factura = MyLabel(self, text='Tipo de Factura:')
        label_tipo_factura.config(fg='black', font=('Arial',20))
        label_tipo_factura.place(x=20, y=375)
        self.option_tipo_factura = tk.OptionMenu(self, self.type_factura, *option_list_type_facturas)
        self.option_tipo_factura.place(x=175, y=379)
        # Boton de Finalizacion
        boton_finalizar = MyBoton(self, text='FINALIZAR', command=self.save_data)
        boton_finalizar.config(font=('Times', 22))
        boton_finalizar.place(x=290, y=420)
        # Escuchamos si hay un enter
        self.bind('<Return>', on_enter)

    def cargar_item_cl(self, codigo_item, cant_item):
        ''' Funcion que guarda los codigos introducidos '''
        if codigo_item == '':
            pass
        else:
            # Vemos la cantidad de veces
            try:
                cant_item = int(cant_item)
            except:
                # Guardamos el codigo
                self.list_codigos.append(codigo_item)
                # Reseteamos el entry
                self.entry_cod_item.delete(0, 'end')
            else:
                # Guardamos el codigo la cantidad de veces solicitada
                for _ in range(cant_item):
                    # Agregamos a la lista
                    self.list_codigos.append(codigo_item)
                # Reseteamos el entry de codigos y de cantidad
                self.entry_cod_item.delete(0, 'end')
                self.entry_cant_item.delete(0, 'end')

    def buscar_servicio(self, tipo_servicio, list_items):
        ''' Funcion que busca servicios y los coloca en una talba '''
        # Reiniciamos la tabla
        self.tabla_servicios.destroy()
        self.create_table_services()
        # Listas por comprension
        servicios_filtrados = (item for item in list_items if tipo_servicio == item.obtener_clase())
        # Cargamos la tabla
        for servicio in servicios_filtrados:
            self.tabla_servicios.insert('', tk.END, text=servicio.codigo, values=(servicio.descripcion, servicio.precio_unitario))

    def save_data(self):
        ''' Funcion que guarda todos los datos y destruye la ventana '''
        # Extraemos la pos del cliente
        if self.entry_ruc_cliente.get() == '':
            # Imprimimos un error
            messagebox.showerror('ERROR', 'SE DEBE DE CARGAR EL RUC')
            # Volvemos al menu
            return
        else:
            # Preguntamos si quiere el pago en efectivo
            if self.check_efectivo.get() is True:
                self.list_formas_pago.append('EFECTIVO')
            # Preguntamos si quiere el pago en tarjeta
            if self.check_tarjeta.get() is True:
                self.list_formas_pago.append('TARJETA')
            # Preguntamos si quiere el pago en cheque
            if self.check_cheque.get() is True:
                self.list_formas_pago.append('CHEQUE')
            # Preguntamos si quiere el pago con transferencia
            if self.check_transferencia.get() is True:
                self.list_formas_pago.append('TRANSFERENCIA')
            # Preguntamos si quiere el pago en USD
            if self.check_usd.get() is True:
                self.list_formas_pago.append('USD')
            # Preguntamos si esta vacia la lista de formas de pago
            if len(self.list_formas_pago) == 0:
                # Imprimimos un error
                messagebox.showerror('ERROR', 'SE DEBE DE ELEGIR AL MENOS UNA FORMA DE PAGO')
                # Retornamos los valores a iniciales
                self.list_formas_pago = []
                # Volvemos al menu
                return
            else:
                # Vemos si tenemos tipo de factura
                if self.type_factura.get() == '':
                    # Mostramos el error
                    messagebox.showerror('ERROR', 'SE DEBE DE COLOCAR EL TIPO DE FACTURA')
                    # Retornamos los valores a iniciales
                    self.list_formas_pago = []
                    # Retornamos al menu
                    return
                # Vemos si tenemos codigos
                if len(self.list_codigos) == 0:
                    # Imprimimos un error
                    messagebox.showerror('ERROR', 'SE DEBE DE ELEGIR AL MENOS UN ITEM')
                    # Retornamos los valores a iniciales
                    self.list_formas_pago = []
                    # Volvemos al menu
                    return
                # Vemos el tipo de factura
                if self.type_factura.get() == 'CONTADO':
                    tipo_fact = True
                else:
                    tipo_fact = False
                # Si todo salio bien guardamos todos los datos
                self.list_final_datos = [self.entry_ruc_cliente.get(), self.list_codigos, self.list_formas_pago, tipo_fact]
                # Destuimos la ventana
                self.destroy()

    def create_table_services(self):
        ''' Funcion que crea la tabla de servicios '''
        self.tabla_servicios = MyTable(self)
        self.tabla_servicios.config(height=10)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_servicios['columns'] = ('one', 'two')
        self.tabla_servicios.column('#0', width=150, minwidth=150)
        self.tabla_servicios.column('one', width=280, minwidth=280)
        self.tabla_servicios.column('two', width=240, minwidth=240)
        # Personalizamos los encabezados
        self.tabla_servicios.heading('#0', text='Codigo', anchor=tk.W)
        self.tabla_servicios.heading('one', text='Descripcion', anchor=tk.W)
        self.tabla_servicios.heading('two', text='Precio', anchor=tk.W)
        # Colocamos la tabla
        self.tabla_servicios.place(x=10, y=120)

    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        list_data = self.list_final_datos
        return list_data

class MyDialogArqCaja(tk.Toplevel):
    def __init__(self, root, caja, nombre_cajero, **options):
        def on_enter(event):
            self.save_data()
        super().__init__(root, **options)
        self.geometry('1228x600+30+80')
        self.title('Datos Factura')
        self.focus_force()
        # Variables
        self.respuesta = False
        # Etiquetas
        label_info = MyLabel(self, text='Arqueo de Caja')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=2)
        label_cajero = MyLabel(self, text='Cajero a cargo del Arqueo: ' + nombre_cajero)
        label_cajero.config(fg='black', font=('Arial',19))
        label_cajero.grid(row=2, column=2)
        # Tabla
        self.create_table_facturas(caja.facturas)
        # Etiquetas
        label_efectivo = MyLabel(self, text='Efectivo: ' + str(caja.total_efectivo))
        label_efectivo.config(fg='black', font=('Arial',17))
        label_efectivo.place(x=12, y=420)
        label_tarjeta = MyLabel(self, text='Tarjeta: ' + str(caja.total_tarjeta))
        label_tarjeta.config(fg='black', font=('Arial',17))
        label_tarjeta.place(x=250, y=420)
        label_cheque = MyLabel(self, text='Cheque: ' + str(caja.total_cheque))
        label_cheque.config(fg='black', font=('Arial',17))
        label_cheque.place(x=500, y=420)
        label_trans = MyLabel(self, text='Transferencia: ' + str(caja.total_transfer))
        label_trans.config(fg='black', font=('Arial',17))
        label_trans.place(x=750, y=420)
        label_dolar = MyLabel(self, text='USD: ' + str(caja.total_usd))
        label_dolar.config(fg='black', font=('Arial',17))
        label_dolar.place(x=1050, y=420)
        label_total_ganancia = MyLabel(self, text='Ganancia Total: ' + str(caja.calcular_monto_total()))
        label_total_ganancia.config(fg='black', font=('Arial',18, 'bold'))
        label_total_ganancia.place(x=12, y=480)
        # Botones
        boton_arquear_caja = MyBoton(self, text='Arquear Caja', command=self.save_data)
        boton_arquear_caja.config(font=('Times', 24))
        boton_arquear_caja.place(x=550, y=550)
        # Escuchamos si no hay algun enter
        self.bind('<Return>', on_enter)

    def create_table_facturas(self, list_facturas):
        self.tabla_servicios = MyTable(self)
        self.tabla_servicios.config(height=18)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_servicios['columns'] = ('one', 'two', 'three', 'four', 'five', 'six', 'seven')
        self.tabla_servicios.column('#0', width=100, minwidth=100)
        self.tabla_servicios.column('one', width=200, minwidth=200)
        self.tabla_servicios.column('two', width=150, minwidth=150)
        self.tabla_servicios.column('three', width=150, minwidth=150)
        self.tabla_servicios.column('four', width=150, minwidth=150)
        self.tabla_servicios.column('five', width=150, minwidth=150)
        self.tabla_servicios.column('six', width=150, minwidth=150)
        self.tabla_servicios.column('seven', width=150, minwidth=150)
        # Personalizamos los encabezados
        self.tabla_servicios.heading('#0', text='NUM FACT', anchor=tk.W)
        self.tabla_servicios.heading('one', text='CLIENTE', anchor=tk.W)
        self.tabla_servicios.heading('two', text='MONTO TOTAL', anchor=tk.W)
        self.tabla_servicios.heading('three', text='EFECTIVO', anchor=tk.W)
        self.tabla_servicios.heading('four', text='TARJETA', anchor=tk.W)
        self.tabla_servicios.heading('five', text='CHEQUE', anchor=tk.W)
        self.tabla_servicios.heading('six', text='TRANSFERENCIA', anchor=tk.W)
        self.tabla_servicios.heading('seven', text='DOLAR', anchor=tk.W)
        # Colocamos la tabla
        self.tabla_servicios.place(x=12, y=65)
        # Cargamos la tabla
        for fact in list_facturas:
            # Guardamos el cliente
            nom_cliente = fact.cliente.nombre + ' ' + fact.cliente.apellido
            # Monto total de la ganancia
            monto_total = str(fact.calcular_total_pagar())
            # Debemos de filtrar las formas de pago para poder mostrar
            monto_efectivo = monto_tarjeta = monto_cheque = monto_transferencia = monto_dolares = '0'
            # Guardamos las formas de pago
            form_pago = fact.formas_pago
            for fp in form_pago:
                if fp.obtener_tipo_pago() == 'CHEQUE':
                    monto_cheque = str(fp.obtener_monto())
                elif fp.obtener_tipo_pago() == 'EFECTIVO':
                    monto_efectivo = str(fp.obtener_monto())
                elif fp.obtener_tipo_pago() == 'TARJETA':
                    monto_tarjeta = str(fp.obtener_monto())
                elif fp.obtener_tipo_pago() == 'TRANSFERENCIA':
                    monto_transferencia = str(fp.obtener_monto())
                elif fp.obtener_tipo_pago() == 'USD':
                    monto_dolares = str(fp.obtener_monto())
            # Mostramos en la tabla
            self.tabla_servicios.insert('', tk.END, text=fact.num_factura, values=(nom_cliente, 
            monto_total, monto_efectivo, monto_tarjeta, monto_cheque, monto_transferencia, monto_dolares))
            # Reiniciamos los valores
            monto_efectivo = monto_tarjeta = monto_cheque = monto_transferencia = monto_dolares = '0'
    
    def save_data(self):
        ''' Guarda la respuesta del usuario '''
        res = messagebox.askyesno('Arqueo de Caja', '¿Esta seguro de Arquear la Caja?')
        self.respuesta = res
        self.destroy()

    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        return self.respuesta

class MyDialogCreateEmp(tk.Toplevel):
    def __init__(self, root, **options):
        # Funcion auxiliar
        def on_enter(event):
            self.save_data()
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('540x290+400+200')
        self.title('Datos del Cliente')
        # Variables
        self.list_data = ['']
        self.tipo_emp = tk.StringVar()
        # Etiquetas
        label_info = MyLabel(self, text='Ingrese los Datos del Empleado:')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.grid(row=1, column=1)
        label_ruc = MyLabel(self, text='RUC/Cedula')
        label_ruc.grid(row=2, column=1)
        label_nombre = MyLabel(self, text='Nombre')
        label_nombre.grid(row=3, column=1)
        label_apellido = MyLabel(self, text='Apellido')
        label_apellido.grid(row=4, column=1)
        label_num_telef = MyLabel(self, text='Telefono')
        label_num_telef.grid(row=5, column=1)
        label_direccion = MyLabel(self, text='Direccion/Ciudad')
        label_direccion.grid(row=6, column=1)
        label_cod_usu = MyLabel(self, text='Codigo de Usuario')
        label_cod_usu.grid(row=7, column=1)
        label_tipo_emp = MyLabel(self, text='Tipo de Empleado:')
        label_tipo_emp.grid(row=8, column=1)
        label_espacio = MyLabel(self, text='Espacio')
        label_espacio.config(fg='white')
        label_espacio.grid(row=9, column=2)
        # Entradas de Texto
        self.entry_ruc = MyEntry(self)
        self.entry_ruc.grid(row=2, column=2)
        self.entry_ruc.focus()
        self.entry_nombre = MyEntry(self)
        self.entry_nombre.grid(row=3, column=2)
        self.entry_apellido = MyEntry(self)
        self.entry_apellido.grid(row=4, column=2)
        self.entry_num_telef = MyEntry(self)
        self.entry_num_telef.grid(row=5, column=2)
        self.entry_direccion = MyEntry(self)
        self.entry_direccion.grid(row=6, column=2)
        self.entry_cod_usu = tk.Entry(self, justify=tk.CENTER)
        self.entry_cod_usu.grid(row=7, column=2)
        # Menu de opciones
        self.option_cuenta_cliente = tk.OptionMenu(self, self.tipo_emp, *lista_tipos_emp)
        self.option_cuenta_cliente.grid(row=8, column=2)
        # Boton de Confirmacion
        confirm_buttom = MyBoton(self, text='Crear Cliente', command=lambda: on_enter(None))
        confirm_buttom.config(font=('Times', 18))
        confirm_buttom.grid(row=10, column=2)
        # Escuchamos si hay un enter
        self.bind('<Return>', on_enter)

    def show_data(self):
        ''' Retorna el la lista de datos del cliente '''
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        list_datos = self.list_data
        return list_datos

    def save_data(self):
        ''' Funcion que guarda la lista de datos '''
        # Guardamos los datos
        self.list_data = [self.entry_ruc.get(), self.entry_nombre.get(), self.entry_apellido.get(), self.entry_num_telef.get(), self.entry_direccion.get(), self.entry_cod_usu.get(), self.tipo_emp.get()]
        # Destruimos la ventana
        self.destroy()

class MyDialogCalcSueldEmp(tk.Toplevel):
    def __init__(self, root, emp, pago_emp, **options):
        # Funciones auxiliares
        def on_enter_pago(event):
            self.save_data()
        def on_enter(event):
            self.destroy()
        super().__init__(root, **options)
        self.geometry('550x650+370+50')
        self.title('Sueldo Empleados')
        self.focus_force()
        # Variables
        self.respuesta = tk.BooleanVar()
        # Etiquetas
        label_info = MyLabel(self, text='Calculo de Sueldo')
        label_info.config(fg='black', font=('Arial',21, 'bold'))
        label_info.place(x=5, y=5)
        label_empleado = MyLabel(self, text='Nombre y Apellido: ' + emp.nombre + ' ' + emp.apellido)
        label_empleado.config(fg='black', font=('Arial',18))
        label_empleado.place(x=20, y=40)
        label_ruc = MyLabel(self, text='RUC: ' + emp.ruc)
        label_ruc.config(fg='black', font=('Arial',18))
        label_ruc.place(x=400, y=40)
        label_trabajos = MyLabel(self, text='Trabajos Realizados:')
        label_trabajos.config(fg='black', font=('Arial',18))
        label_trabajos.place(x=20, y=75)
        # Generamos la tabla
        self.mostrar_tabla_trabajos(emp.items_realizados, emp.productos_vendidos)
        # Botones
        if pago_emp is True:
            botont_finalizar = MyBoton(self, text='Finalizar', command=self.save_data)
            botont_finalizar.config(font=('Times', 24))
            botont_finalizar.place(x=220, y=605)
        else:
            botont_finalizar = MyBoton(self, text='Finalizar', command=self.destroy)
            botont_finalizar.config(font=('Times', 24))
            botont_finalizar.place(x=220, y=605)
        # Etiquetas
        try:
            label_monto_pagar = MyLabel(self, text='Monto a Pagar: ' + str(emp.calcular_sueldo()))
        except:
            # Propagamos la Excepcion
            raise
        label_monto_pagar.config(fg='black', font=('Arial',18))
        label_monto_pagar.place(x=20, y=565)
        label_propina = MyLabel(self, text='Propina: ' + str(emp.propina))
        label_propina.config(fg='black', font=('Arial',18))
        label_propina.place(x=350, y=565)
        #  Escuchamos si no hay algun enter
        if pago_emp is True:
            # Si va a pagar guardamos los datos
            self.bind('<Return>', on_enter_pago)
        else:
            # Si no, salimos
            self.bind('<Return>', on_enter)
        
    def mostrar_tabla_trabajos(self, items_realizados, productos_vendidos):
        ''' Muestra una tabla con todos los items ralizados por el empleado '''
        # Creamos la tabla
        self.tabla_items = MyTable(self)
        self.tabla_items.config(height=24)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_items['columns'] = ('one', 'two', 'three')
        self.tabla_items.column('#0', width=35, minwidth=50)
        self.tabla_items.column('one', width=100, minwidth=100)
        self.tabla_items.column('two', width=235, minwidth=190)
        self.tabla_items.column('three', width=155, minwidth=155)
        # Personalizamos los encabezados
        self.tabla_items.heading('#0', text='Nº', anchor=tk.W)
        self.tabla_items.heading('one', text='CODIGO', anchor=tk.W)
        self.tabla_items.heading('two', text='DESCRIPCION', anchor=tk.W)
        self.tabla_items.heading('three', text='FECHA TRABAJO', anchor=tk.W)
        ## CARGAMOS LA TABLA ##
        # Primeramente los items realizados
        for i in range(len(items_realizados)):
            self.tabla_items.insert('', tk.END, text=(i+1), values=(items_realizados[i].codigo, items_realizados[i].descripcion, items_realizados[i].fecha_consumision_cliente))
        # Luego los productos vendidos
        for i in range(len(productos_vendidos)):
            self.tabla_items.insert('', tk.END, text=(i+1), values=(productos_vendidos[i].codigo, productos_vendidos[i].descripcion, productos_vendidos[i].fecha_consumision_cliente))
        # Colocamos la tabla
        self.tabla_items.place(x=10, y=105)

    def save_data(self):
        ''' Guarda la respuesta del usuario '''
        res = messagebox.askyesno('Pago de Empleado', '¿Desea Pagar al Empleado?')
        self.respuesta = res
        self.destroy()

    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        return self.respuesta

class MyDialogPayEmp(tk.Toplevel):
    def __init__(self, root, emp, **options):
        # Funcion auxiliar
        def on_enter(event):
            self.save_data()
        # Metodo Principal
        super().__init__(root, **options)
        self.geometry('650x690+370+10')
        self.title('Ganancia de Empleados')
        self.focus_force()
        ## Variables ##
        self.tipo_ganacia = []
        self.montos_entry = []
        # Array Options | Array Entrys #
        self.option_menus = []
        self.entrys = []
        ## CONFIGURACION DEL FRAME CON SCROLLBAR ##
        self.myframe=tk.Frame(self,bg='white', relief=tk.GROOVE,width=650,height=690,bd=1)
        self.myframe.place(x=0,y=0)
        self.canvas=tk.Canvas(self.myframe, bg='white')
        self.frame=tk.Frame(self.canvas)
        self.myscrollbar=tk.Scrollbar(self.myframe,orient='vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side='right',fill="y")
        self.canvas.pack(side='left')
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind('<Configure>',self.myfunction)
        # Etiquetas
        label_info = MyLabel(self.frame, text='Administrar Ganancia')
        label_info.config(fg='black', font=('Arial',20, 'bold'))
        label_info.grid(row=0, column=0)
        label_nom_emp = MyLabel(self.frame, text='Nombre y Apellido: ' + emp.obtener_nombres())
        label_nom_emp.grid(row=1, column=0)
        label_espacio = MyLabel(self.frame, text='TIPOOO DE GANANCIAAAAA')
        label_espacio.config(fg='white')
        label_espacio.grid(row=1, column=1)
        label_ruc_emp = MyLabel(self.frame, text='       RUC: ' + emp.ruc)
        label_ruc_emp.grid(row=1, column=2)
        label_tipo_serv = MyLabel(self.frame, text='Tipo de Servicio')
        label_tipo_serv.grid(row=2, column=0)
        label_tipo_serv.config(fg='black', font=('Arial',16, 'bold'))
        label_tipo_gana = MyLabel(self.frame, text='Tipo de Ganancia')
        label_tipo_gana.grid(row=2, column=1)
        label_tipo_gana.config(fg='black', font=('Arial',16, 'bold'))
        label_monto = MyLabel(self.frame, text='Monto/Porcentaje')
        label_monto.grid(row=2, column=2)
        label_monto.config(fg='black', font=('Arial',16, 'bold'))
        # Mostramos las opciones
        self.data_emp(emp)
        # Label de espacio
        label_espacio1 = MyLabel(self.frame, text='espacio')
        label_espacio1.config(fg='white')
        label_espacio1.grid(row=30, column=1)
        # Botones
        botont_finalizar = MyBoton(self.frame, text='Finalizar', command=lambda: on_enter(None))
        botont_finalizar.config(font=('Times', 24))
        botont_finalizar.grid(row=31, column=1)
        # Escuchamos si no hay algun enter
        self.bind('<Return>', on_enter)

    def data_emp(self, emp):
        # Variables
        index = 3
        tipos_ganacia = ('MONTO', 'PORCENTAJE')
        for i in range(len(lista_servicios)):
            # Primeramente colocamos las Etiquetas
            tk.Label(self.frame,text=lista_servicios[i]).grid(row=index,column=0)
            # Luego los Options Menu
            self.tipo_ganacia.append(tk.StringVar())
            self.option_menus.append(tk.OptionMenu(self.frame, self.tipo_ganacia[i], *tipos_ganacia))
            # Luego los Entrys
            self.entrys.append(MyEntry(self.frame))
            # Vemos el tipo de ganancia y colocamos las variables corresponcientes
            if emp.porcent_servicios[i]!=0 and emp.montos_fijos_servicios[i]==0:
                self.tipo_ganacia[i].set('PORCENTAJE')
                self.entrys[i].insert(tk.END, str(emp.porcent_servicios[i]))
            elif emp.porcent_servicios[i]==0 and emp.montos_fijos_servicios[i]!=0:
                self.tipo_ganacia[i].set('MONTO')
                self.entrys[i].insert(tk.END, str(emp.montos_fijos_servicios[i]))
            elif emp.porcent_servicios[i]==0 and emp.montos_fijos_servicios[i]==0:
                self.tipo_ganacia[i].set('')
                self.entrys[i].insert(tk.END, str(0)) # No tiene ganancia
            # Colocamos los entrys y las opciones
            self.option_menus[i].grid(row=index ,column=1)
            self.entrys[i].grid(row=index,column=2)
            index += 1
        
    def myfunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=627,height=682)

    def save_data(self):
        ''' Guarda la respuesta del usuario '''
        # Preguntamos si desea cambiar
        res = messagebox.askyesno('Ganancia Empleados', '¿Desea Cambiar la Ganancia del Empleado?')
        if res is True:
            # Guardamos los tipos de ganancia
            type_g = []
            for tpg in self.tipo_ganacia:
                type_g.append(tpg.get())
            self.tipo_ganacia = type_g
            # Guardamos la lista de montos/porcentajes
            for ent in self.entrys:
                self.montos_entry.append(ent.get())
            self.destroy()
        else:
            self.tipo_ganacia = self.montos_entry = []
            self.destroy()

    def show_data(self):
        # Le pedimos a la venatana que espere
        self.deiconify()
        self.wait_window()
        # Retornamos la lista con los datos
        return [self.tipo_ganacia, self.montos_entry]

class MyDialogColocPropina(tk.Toplevel):
    def __init__(self, root, **options):
        # Metodo principal
        super().__init__(root, **options)
        self.geometry('570x420+400+150')
        self.title('Ingreso de Codigos')
        self.focus_force()
        # Variables
        self.list_final_datos = []
        self.pos_cliente = None
        self.list_cod_items = ['']
        self.cuenta_cliente = tk.StringVar()
        self.tipo_servicio = tk.StringVar()
        # Etiquetas
        label_info = MyLabel(self, text='Colocar Propina:')
        label_info.config(fg='black', font=('Arial', 21, 'bold'))
        label_info.grid(row=1, column=1)
        label_ci_cliente = MyLabel(self, text='CI/RUC Cliente:')
        label_ci_cliente.grid(row=2, column=1)
        label_ci_empleado = MyLabel(self, text='CI/RUC Empleado:')
        label_ci_empleado.grid(row=3, column=1)
        label_monto_propina = MyLabel(self, text='Monto Propina:')
        label_monto_propina.grid(row=4, column=1)
        label_info2 = MyLabel(self, text='Empleados:')
        label_info2.config(fg='black', font=('Arial', 18, 'bold'))
        label_info2.grid(row=5, column=1)
        
        # Entradas
        self.entry_ci_cliente = MyEntry(self, justify=tk.CENTER)
        self.entry_ci_cliente.grid(row=2, column=2)
        self.entry_ci_empleado = MyEntry(self, justify=tk.CENTER)
        self.entry_ci_empleado.grid(row=3, column=2)
        self.entry_monto_propina = MyEntry(self, justify=tk.CENTER)
        self.entry_monto_propina.grid(row=4, column=2)
        # Tablas
        self.tabla_empleados = MyTable(self)
        self.tabla_empleados.config(height=10)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_empleados['columns'] = ('one', 'two')
        self.tabla_empleados.column('#0', width=200, minwidth=200)
        self.tabla_empleados.column('one', width=200, minwidth=200)
        self.tabla_empleados.column('two', width=150, minwidth=150)
        # Personalizamos los encabezados
        self.tabla_empleados.heading('#0', text='Nombre', anchor=tk.W)
        self.tabla_empleados.heading('one', text='Apellido', anchor=tk.W)
        self.tabla_empleados.heading('two', text='CI/RUC', anchor=tk.W)
        # Colocamos la tabla
        self.tabla_empleados.place(x=7, y=150)
        # Boton de Finalizacion
        boton_agg_propina = MyBoton(self, text='Agregar Propina', command=self.destroy)
        boton_agg_propina.config(font=('Times', 20))
        boton_agg_propina.place(x=225, y=370)

## INTERFAZ GRAFICA ##
class ViewApp(MyFrame):
    ''' Abstraccion de una interfaz GUI '''
    def __init__(self, controlador):
        # Controlador
        self.controlador = controlador
        # Root
        self.raiz = MyTk('ProSoft')
        self.raiz.protocol("WM_DELETE_WINDOW", self.cerrando_app)
        # Frames
        self.frame = MyFrame(self.raiz)
        self.frame1 = MyFrame(self.raiz)
        self.frame1.config(bg='Lightgray', width=1160, height= 125)
        self.frame1.place(x=200,y=0)
        self.frame.config(bg='silver', width=200, height=770)
        self.frame.pack(side=tk.LEFT)
        # Etiquetas
        self.etiqueta = MyLabel(self.raiz, text='ProSoft', bg='silver', anchor=tk.W)
        self.etiqueta.config(font=('Times', 40, 'bold'), fg='black')
        self.etiqueta.place(x=30, y=15)
        # Botones
        self.boton_atender = None
        self.boton_cobrar = None
        self.boton_empleados = None
        self.boton_fact = None
        self.boton_clientes = None
        self.boton_stock = None
        self.boton_info = None
        # Tablas
        self.tabla_cuenta_clientes = None
        self.tabla_clientes = None
        self.tabla_empleados = None
        self.tabla_items = None
        self.tabla_facturas = None

    ## MENU PRINCIPAL ##
    def run_app(self):
        ''' Muestra el Menu Principal '''
        # Imagenes
        img_atender = self.get_image('./Vista/icons/grupo.png')
        img_cobrar = self.get_image('./Vista/icons/cobros.png')
        img_emp = self.get_image('./Vista/icons/empleados.png')
        img_facturacion = self.get_image('./Vista/icons/ganancias.png')
        img_clientes = self.get_image('./Vista/icons/clientes.png')
        img_stock = self.get_image('./Vista/icons/stock.png')
        img_info = self.get_image('./Vista/icons/info.png')

        # Botones
        self.boton_atender = MyBoton(self.frame, image=img_atender, text='    Area Principal   ', compound='left', command=self.mostrar_sub_menu_atencion)
        self.boton_atender.place(x=11.5, y=90)
        self.boton_cobrar  = MyBoton(self.frame, image=img_cobrar, text='      Area Caja       ', compound='left', command=self.mostrar_sub_menu_cobrar)
        self.boton_cobrar.place(x=11.5, y=170)
        self.boton_empleados = MyBoton(self.frame, image=img_emp, text='Admin Empleados', compound='left', command=self.mostrar_sub_menu_admin_emp)
        self.boton_empleados.place(x=11.5, y=250)
        self.boton_fact = MyBoton(self.frame, image=img_facturacion, text='  Admin Facturas  ', compound='left', command=self.mostrar_sub_menu_facturacion)
        self.boton_fact.place(x=11.5, y=330)
        self.boton_clientes = MyBoton(self.frame, image=img_clientes, text='   Admin Clientes  ', compound='left', command=self.mostrar_sub_menu_clientes)
        self.boton_clientes.place(x=11.5, y=410)
        self.boton_stock = MyBoton(self.frame, image=img_stock, text='     Admin Stock    ', compound='left', command=self.mostrar_sub_menu_stock)
        self.boton_stock.place(x=11.5, y=490)
        self.boton_info = MyBoton(self.frame, image=img_info, text='     Info ProSoft     ', compound='left', command=self.mostrar_info_prosoft)
        self.boton_info.place(x=11.5, y=570)
    
        self.raiz.mainloop()

    ## SUB MENUS ##
    def mostrar_sub_menu_atencion(self):
        ''' Muestra el sub menu de atencion al cliente '''
        # Funciones auxiliares
        def mostrar_tabla_reporte(emp):
            ''' Funcion que muestra una tabla con el reporte de trabajos el Empleado '''
            # Obtenemos la lista de cuentas abiertas
            pos_emp = self.controlador.pos_emp_in_lista(emp)
            # 0 Corresponde al numero de sucursal
            items_realizados = self.controlador.peluquerias[0].empleados[pos_emp].items_realizados
            productos_vendidos = self.controlador.peluquerias[0].empleados[pos_emp].productos_vendidos
            # Creamos la tabla
            self.tabla_items = MyTable(sub_frame1)
            ## Configuramos y cargamos la tabla ##
            # Configuramos las columnas
            self.tabla_items['columns'] = ('one', 'two', 'three')
            self.tabla_items.column('#0', width=50, minwidth=50)
            self.tabla_items.column('one', width=120, minwidth=120)
            self.tabla_items.column('two', width=320, minwidth=320)
            self.tabla_items.column('three', width=310, minwidth=310)
            # Personalizamos los encabezados
            self.tabla_items.heading('#0', text='Nº', anchor=tk.W)
            self.tabla_items.heading('one', text='CODIGO', anchor=tk.W)
            self.tabla_items.heading('two', text='DESCRIPCION', anchor=tk.W)
            self.tabla_items.heading('three', text='FECHA TRABAJO', anchor=tk.W)
            ## CARGAMOS LA TABLA ##
            # Primero los items realizados
            for i in range(len(items_realizados)):
                self.tabla_items.insert('', tk.END, text=(i+1), values=(items_realizados[i].codigo, items_realizados[i].descripcion, items_realizados[i].fecha_consumision_cliente))
            # Luego los productos vendidos
            for i in range(len(productos_vendidos)):
                self.tabla_items.insert('', tk.END, text=(i+1), values=(productos_vendidos[i].codigo, productos_vendidos[i].descripcion, productos_vendidos[i].fecha_consumision_cliente))
            # Colocamos la tabla
            self.tabla_items.pack(padx=15, pady=9)

        def abrir_cuenta(emp):
            ''' Abre la cuenta de un cliente '''
            # Funciones auxiliares de la sub funcion
            def buscar_cliente():
                ''' Funcion que busca al cliente '''
                try:
                    datos_cliente = self.controlador.abrir_cuenta_cliente(emp, entry_ruc.get())
                except Exception as e:
                    # Reseteamos el entry
                    entry_ruc.delete(0, 'end')
                    # Imprimimos el aviso
                    self.imprimir_error(str(e))
                    entry_ruc.focus_force()
                else:
                    # Imprimimos el aviso
                    self.imprimir_aviso('Se Abrio Correctamente la Cuenta\ndel Cliente: ' + datos_cliente)
                    # Reseteamos el entry
                    entry_ruc.delete(0, 'end')
                    # Actualizamos la tabla
                    self.tabla_cuenta_clientes.destroy()
                    self.mostrar_tabla_cuentas(sub_frame1)
                    entry_ruc.focus_force()
            # Reiniciamos los Sub frames que tenemos
            reiniciar_frames()
            # Colocamos los frames
            sub_frame1.place(x=200,y=125)
            sub_frame2.place(x=1040,y=125)
            # Mostramos la tabla de cuentas abiertas
            self.mostrar_tabla_cuentas(sub_frame1)
            # Etiqueta
            label_1 = MyLabel(sub_frame2, bg='white', text='Ingrese la Cedula\no el RUC del \nCliente a agregar')
            label_1.config(fg='black', font=('Arial',20))
            label_1.pack(padx=20, pady=8)
            # Entrada
            entry_ruc= MyEntry(sub_frame2)
            entry_ruc.focus()
            entry_ruc.pack(padx=20, pady=5)
            # Boton
            boton_buscar = MyBoton(sub_frame2, text='BUSCAR', command=lambda: buscar_cliente())
            boton_buscar.pack(padx=20, pady=12)
                                 
        def cargar_cuenta(emp):
            ''' Funcion que se encarga de cargar la cuenta de un cliente '''
            # Funciones Auxiliares
            def cargar_items():
                ''' Funcion que se encarga de cargar los items '''
                # Inabilitamos los botones secundarios
                self.desac_botones_secundarios()
                try:
                    # Pedimos todos los datos
                    datos_carga_items = MyDialogChargeCl(self.raiz, 
                    self.controlador.model.obtener_lista_cl_cuenta(0), 
                    self.controlador.peluquerias[0].items).show_data()
                    # datos_carga_items[0]: Posicion in lista del cliente | datos_carga_items[1]: Lista de codigos de servicios
                    datos_cl = self.controlador.cargar_cuenta_cliente(emp, 
                    datos_carga_items[0], datos_carga_items[1])
                except Exception as e:
                    # Habilitamos los botones secundarios
                    self.activ_botones_secundarios()
                    # Mostramos el error
                    self.imprimir_error(str(e))
                else:
                    # Habilitamos los botones secundarios
                    self.activ_botones_secundarios()
                    # Mostramos el aviso
                    self.imprimir_aviso('Se Cargo Correctamente la Cuenta del Cliente: ' + datos_cl)
                    
            # Reiniciamos los Sub Frames
            reiniciar_frames()
            # Verificamos que la lista de cuentas no este vacia
            try:
                self.controlador.verificar_lista_cuentas()
            except Exception as e:
                self.imprimir_error(str(e))
            else:
                # Colocamos los frames
                sub_frame1.place(x=200,y=125)
                sub_frame2.place(x=1040,y=125)
                # Mostramos la tabla de cuentas abiertas
                self.mostrar_tabla_cuentas(sub_frame1)
                # Imagen del boton
                img_cargar = self.get_image('./Vista/icons/compra.png')
                # Boton de carga
                boton_cargar_items = MyBoton(sub_frame2, image=img_cargar, 
                text='Buscar y Cargar Items\na la Cuenta del Cliente', 
                compound='top', command=lambda: cargar_items())
                boton_cargar_items.pack(padx=40, pady=12)
                self.frame1.wait_window(sub_frame2)

        def crear_cliente(emp):
            ''' Funcion que crea un Cliente '''
            # Reinicamos los Sub Frames
            reiniciar_frames()
            # Desactivamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                # Pedimos los datos
                list_datos_cl = MyDialogCreateClient(self.raiz).show_data()
                # Le pasamos los datos al controlador
                self.controlador.crear_cliente(emp, list_datos_cl)
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Avisamos que salio todo bien
                self.imprimir_aviso('Se creo correctamente el nuevo Cliente')
                self.frame1.focus_force()

        def crear_item(emp):
            ''' Funcion que crea un Item '''
            # Reinicamos los Sub Frames
            reiniciar_frames()
            # Bloqueamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                # Pedimos los datos
                list_datos_item = MyDialogCreateItem(self.raiz).show_data()
                # Le pasamos los datos al controlador
                self.controlador.crear_item(emp, list_datos_item)
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Avisamos que salio todo bien
                self.imprimir_aviso('Se creo correctamente el nuevo Item')
                self.frame1.focus_force()

        def mi_reporte(emp):
            ''' Muestra todo lo realizado por el Empleado '''
            # Reiniciamos los Frames
            reiniciar_frames()
            # Colocamos los frames
            sub_frame1.place(x=200,y=125)
            sub_frame2.place(x=1040,y=125)
            # Mostramos la tabla de reporte
            mostrar_tabla_reporte(emp)

        # Funcion de salir
        def salir():
            ''' Funcion que se encarga de salir y reiniciar los frames correspondientes '''
            # Reiniciamos el frame
            self.reiniciar_frame_sub_opciones()
            # Destruimos los frames creados
            sub_frame1.destroy()
            sub_frame2.destroy()
            # Activamos los botones
            self.activ_botones_principales()
            
        # Funcion de Reinicio
        def reiniciar_frames():
            # Destruimos todas las opciones anteriores
            for widget in sub_frame1.winfo_children():
                widget.destroy()

            # Destruimos todas las opciones anteriores
            for widget in sub_frame2.winfo_children():
                widget.destroy()

        # Destruimos todas las opciones anteriores
        self.reiniciar_frame_sub_opciones()
        # Invalidamos los botones principales
        self.desac_botones_principales()
        try:
            # Pedimos el codigo de usuario
            emp = MyDialogCodUsu(self.raiz, self.controlador).show_emp()
        except Exception as e:
            # Reactivamos los botones principales
            self.activ_botones_principales()
            # Borramos todos las sub opciones
            self.reiniciar_frame_sub_opciones()
            # Informamos al usuario del error
            self.imprimir_error(str(e))
            self.frame.focus_force()
        else:
            # Frames
            sub_frame1 = MyFrame(self.raiz)
            sub_frame1.config(bg='white smoke', width=840, height=700)
            sub_frame2 = MyFrame(self.raiz)
            sub_frame2.config(bg='white', width=240, height=700)
            
            # Imagenes
            img_abrir_cuenta = self.get_image('./Vista/icons/carro.png')
            img_cargar_cuenta = self.get_image('./Vista/icons/bolsa.png')
            img_crear_cliente = self.get_image('./Vista/icons/usuario.png')
            img_crear_item = self.get_image('./Vista/icons/mas.png')
            img_mi_reporte = self.get_image('./Vista/icons/verificacion.png')
            img_salir = self.get_image('./Vista/icons/logout.png')

            # Etiquetas
            self.mostrar_usuario(emp)

            # Botones
            boton_abrir_cuenta = MyBoton(self.frame1, image=img_abrir_cuenta, text=' Abrir Cuenta\nCliente ', compound='top', command=lambda: abrir_cuenta(emp))
            boton_abrir_cuenta.place(x=140, y=18)
            boton_cargar_cuenta = MyBoton(self.frame1, image=img_cargar_cuenta,text='Cargar Cuenta\nCliente', compound='top', command=lambda: cargar_cuenta(emp))
            boton_cargar_cuenta.place(x=260, y=18)
            boton_crear_cliente = MyBoton(self.frame1, image=img_crear_cliente,text='\n  Crear Cliente  ', compound='top', command=lambda: self.crear_cliente(emp, reiniciar_frames))
            boton_crear_cliente.place(x=393, y=18)
            boton_crear_item = MyBoton(self.frame1, image=img_crear_item, text='\n   Crear Item   ', compound='top', command=lambda: crear_item(emp))
            boton_crear_item.place(x=530, y=18)
            boton_mi_reporte = MyBoton(self.frame1, image=img_mi_reporte, text='  Mi  \n   Reporte   ', compound='top', command=lambda: mi_reporte(emp))
            boton_mi_reporte.place(x=660, y=18)
            boton_salir = MyBoton(self.frame1, image=img_salir, text='\n      Salir     ', compound='top', command=salir)
            boton_salir.place(x=980, y=18)

            self.raiz.wait_window(self.frame1)

    def mostrar_sub_menu_cobrar(self):
        '''' Muestra el sub menu de cobros '''
        # Funciones auxiliares
        def cobrar_cliente(emp):
            ''' Funcion que pide al controlador cobrar al cliente '''
            # Bloqueamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                # Pedimos los datos
                list_cuentas = self.controlador.peluquerias[0].lista_clientes_cuenta = self.controlador.model.obtener_lista_cl_cuenta(0)
                if len(list_cuentas) == 0:
                    raise Exception('LA LISTA DE CUENTAS ESTA VACIA')
                list_datos_fact_principal = MyDialogDatFactura(self.raiz, list_cuentas).show_data()
                # list_datos_fact_principal[0]: cuenta | list_datos_fact_principal[1]: ruc | list_datos_fact_principal[2]: tipo de factura #
                # Validamos los datos de "list_datos_fact_principal"
                self.controlador.validar_datos_fact(list_datos_fact_principal)
                # Pedimos la formas de pago -> list_formas_pago[]
                list_formas_pago = MyDialogShowFact(self.raiz, list_cuentas[list_datos_fact_principal[0]]).show_data()
                if len(list_formas_pago) == 1:
                    # Preguntamos si es Efectivo el medio de pago
                    if list_formas_pago[0] != 'EFECTIVO':
                        dato_pago = MyDialogFormPagoUnico(self.raiz, list_formas_pago[0]).show_data()
                    else:
                        dato_pago = ''
                    # Vemos si es en dolares
                    if list_formas_pago[0] == 'USD':
                        # Le pasamos los datos al controlador para crear las formas de pago
                        formas_pago = self.controlador.crear_formas_pago(list_formas_pago, [dato_pago], None)
                        # Pasamos todos los datos recogidos para generar la factura   (emp, cuenta, ruc, tipo_factura, formas_pago)
                        self.controlador.cobrar_cliente(emp, list_datos_fact_principal[0], list_datos_fact_principal[1], list_datos_fact_principal[2], formas_pago)
                    else:
                        # Le pasamos los datos al controlador para crear las formas de pago
                        formas_pago = self.controlador.crear_formas_pago(list_formas_pago, [list_cuentas[list_datos_fact_principal[0]].calcular_deuda()], [dato_pago])
                        # Pasamos todos los datos recogidos para generar la factura   (emp, cuenta, ruc, tipo_factura, formas_pago)
                        self.controlador.cobrar_cliente(emp, list_datos_fact_principal[0], list_datos_fact_principal[1], list_datos_fact_principal[2], formas_pago)
                else:
                    # Lista de datos de los pagos -> Contiene arrays con el monto y el dato de pago
                    list_datos_pago = []
                    # Preguntamos por los medios de pago
                    for forma_pag in list_formas_pago:
                        # OBS: MyDialogFormPagoVarios -> returns -> []
                        if forma_pag == 'EFECTIVO':
                            list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                        elif forma_pag == 'TARJETA':
                            list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                        elif forma_pag == 'CHEQUE':
                            list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                        elif forma_pag == 'TRANSFERENCIA':
                            list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                        elif forma_pag == 'USD':
                            list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                    # Primeramente filtramos los pagos y los datos
                    opciones_datos = []
                    montos = []
                    for pos in range(len(list_datos_pago)):
                        for pos_in in range(2): # 2 ya que vienen de a dos
                            if pos_in == 0:
                                # Aqui van las opciones
                                opciones_datos.append(list_datos_pago[pos][pos_in])
                            if pos_in == 1:
                                # Aqui van los montos
                                montos.append(list_datos_pago[pos][pos_in])
                    # Creamos las formas de pago 
                    # OBS: crear_formas_pago -> returns -> []
                    formas_pago = self.controlador.crear_formas_pago(list_formas_pago, montos, opciones_datos)
                    # Pasamos todos los datos recogidos para generar la factura   (emp, cuenta, ruc, tipo_factura, formas_pago)
                    self.controlador.cobrar_cliente(emp, list_datos_fact_principal[0], list_datos_fact_principal[1], list_datos_fact_principal[2], formas_pago)
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Avisamos que salio todo bien
                self.imprimir_aviso('Se Cobro y Cerro Correctamente\nla Cuenta del Cliente: ' 
                + list_cuentas[list_datos_fact_principal[0]].nombre + ' ' 
                + list_cuentas[list_datos_fact_principal[0]].apellido)
                ### PREGUNTAR PARA IMPRIMIR LA FACTURA ###
                # Reiniciamos la tabla de cuentas
                self.tabla_cuenta_clientes.destroy()
                # Actualizamos la tabla de cuentas abiertas
                self.mostrar_tabla_cuentas(sub_frame1)
                # Damos la atencion al la pagina principal
                self.frame1.focus_force()
            
        def anular_factura(emp):
            ''' Funcion que pide al controlador anular una Factura '''
            # Bloqueamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                num_comprobante = MyDialogGetInfo(self.raiz, 'Facturas', 'Ingrese el numero de Factura:').show_data()
                try:
                    factura = self.controlador.obtener_factura(int(num_comprobante)-1)
                except:
                    # Mostramos el aviso
                    self.imprimir_error('EL DATO ES INVALIDO')
                    # Activamos los botones secundarios
                    self.activ_botones_secundarios()
                    # Damos la atencion al la pagina principal
                    self.frame1.focus_force()
                    return
                respuesta = MyDialogDetalleFact(self.raiz, factura).show_data()
                # Vemos si quiere anular la factura
                if respuesta is True:
                    # Debemos de generar la factura que reemplazara a la anulada
                    datos_nueva_factura = MyDialogGetFactNew(self.raiz, self.controlador.peluquerias[0].items).show_data()
                    # datos_nueva_factura[0]: RUC -> Str | datos_nueva_factura[1]: cod_items -> []
                    # datos_nueva_factura[2]: Formas de pago -> [] | datos_nueva_factura[3] -> Bool
                    # Obtenemos los items
                    items = self.controlador.obtener_items(datos_nueva_factura[1])
                    monto_pagar = self.controlador.calcular_total_pagar(items)
                    # Mostramos el monto a pagar
                    self.imprimir_aviso('El Total a pagar es: ' + str(monto_pagar))
                    # Generamos las formas de pago
                    list_formas_pago = datos_nueva_factura[2]
                    if len(list_formas_pago) == 1:
                        # Preguntamos si es Efectivo el medio de pago
                        if list_formas_pago[0] != 'EFECTIVO':
                            dato_pago = MyDialogFormPagoUnico(self.raiz, list_formas_pago[0]).show_data()
                        else: 
                            dato_pago = ''
                        # Vemos si es en dolares
                        if list_formas_pago[0] == 'USD':
                            # Le pasamos los datos al controlador para crear las formas de pago
                            formas_pago = self.controlador.crear_formas_pago(list_formas_pago, [dato_pago], None)
                        else:
                            # Le pasamos los datos al controlador para crear las formas de pago
                            formas_pago = self.controlador.crear_formas_pago(list_formas_pago, [monto_pagar], [dato_pago])
                    else:
                        # Lista de datos de los pagos -> Contiene arrays con el monto y el dato de pago
                        list_datos_pago = []
                        # Preguntamos por los medios de pago
                        for forma_pag in list_formas_pago:
                            # OBS: MyDialogFormPagoVarios -> returns -> []
                            if forma_pag == 'EFECTIVO':
                                list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                            elif forma_pag == 'TARJETA':
                                list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                            elif forma_pag == 'CHEQUE':
                                list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                            elif forma_pag == 'TRANSFERENCIA':
                                list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                            elif forma_pag == 'USD':
                                list_datos_pago.append(MyDialogFormPagoVarios(self.raiz, forma_pag).show_data())
                        # Primeramente filtramos los pagos y los datos
                        opciones_datos = []
                        montos = []
                        for pos in range(len(list_datos_pago)):
                            for pos_in in range(2): # 2 ya que vienen de a dos
                                if pos_in == 0:
                                    # Aqui van las opciones
                                    opciones_datos.append(list_datos_pago[pos][pos_in])
                                if pos_in == 1:
                                    # Aqui van los montos
                                    montos.append(list_datos_pago[pos][pos_in])
                        # Creamos las formas de pago 
                        # OBS: crear_formas_pago -> returns -> []
                        formas_pago = self.controlador.crear_formas_pago(list_formas_pago, montos, opciones_datos)
                    # Le pasamos al controlador para generar la factura nueva: (condicion_factura, items, cliente, formas_pago)
                    factura_nueva = self.controlador.generar_factura(datos_nueva_factura[3], items, datos_nueva_factura[0], formas_pago, emp)
                    # Anulamos la nueva factura
                    self.controlador.anular_factura(int(num_comprobante)-1, factura_nueva)
                else:
                    # Si no, salimos
                    # Activamos los botones secundarios
                    self.activ_botones_secundarios()
                    return
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Avisamos que salio todo bien
                self.imprimir_aviso('Se Anulo y Creo Correctamente\nla Factura Vieja y la Factura Nueva')
                ### PREGUNTAR PARA IMPRIMIR LA FACTURA ###
                # Damos la atencion al la pagina principal
                self.frame1.focus_force()

        def reiniciar_tabla_cuentas():
            # Reiniciamos los frames
            reiniciar_frames()
            # Volvemos a cargar la tabla
            self.mostrar_tabla_cuentas(sub_frame1)

        def reporte_caja(emp):
            # Funciones auxiliares
            def realizar_arqueo(emp):
                num_caja = MyDialogGetInfo(self.raiz, 'Caja', 
                'Ingrese el Numero de Caja:').show_data()
                try:
                    num_caja = int(num_caja) - 1
                    if len(self.controlador.peluquerias[0].cajas) < num_caja:
                        raise Exception('EL NUMERO DE CAJA NO EXISTE')
                    caja = self.controlador.obtener_caja(num_caja)
                    respuesta = MyDialogArqCaja(self.raiz, caja, (emp.nombre + ' ' + emp.apellido)).show_data()
                    if respuesta is True:
                        # Guardamos la caja para el reporte
                        #caja_reporte = caja
                        # Arqueamos la caja
                        self.controlador.arquear_caja(num_caja)
                    else:
                        # Activamos los botones secundarios
                        self.activ_botones_secundarios()
                        # Damos la atencion al la pagina principal
                        self.frame1.focus_force()
                        return
                except Exception as e:
                    # Activamos los botones secundarios
                    self.activ_botones_secundarios()
                    # Mostramos el error
                    self.imprimir_error(str(e))
                    self.frame1.focus_force()
                else:
                    # Activamos los botones secundarios
                    self.activ_botones_secundarios()
                    # Avisamos que salio todo bien
                    self.imprimir_aviso('Se Arqueo Correctamente la Caja')
                    ### PREGUNTAR PARA IMPRIMIR EL REPORTE ###
                    #print(caja_reporte)
                    # Reiniciamos la tabla de cuentas
                    self.tabla_facturas.destroy()
                    # Actualizamos la tabla de cuentas abiertas
                    self.mostrar_tabla_facturas(sub_frame1)
                    # Damos la atencion al la pagina principal
                    self.frame1.focus_force()
                
            def imprimir_factura():
                pass

            ## FUNCION PRINCIPAL ##
            # Reiniciamos los frames
            reiniciar_frames()
            # Mostramos la tabal de facturas
            self.mostrar_tabla_facturas(sub_frame1)
            sub_frame2.place(x=1040,y=125)
            # Imagen del boton
            img_arquear = self.get_image('./Vista/icons/banco.png')
            img_imp_fact = self.get_image('./Vista/icons/impresion.png')
            # Botones
            boton_cargar_items = MyBoton(sub_frame2, image=img_arquear, 
            text='Mostrar Reporte y\n  Arquear la Caja ', 
            compound='top', command=lambda: realizar_arqueo(emp))
            boton_cargar_items.pack(padx=60, pady=12)
            boton_imprimir_factura = MyBoton(sub_frame2, image=img_imp_fact, 
            text='       Imprimir       \n        Factura       ', 
            compound='top', command=imprimir_factura)
            boton_imprimir_factura.pack(padx=60, pady=20)
            # Esperamos a que se destruya el frame
            self.frame1.wait_window(sub_frame2)

        def colocar_propina(emp):
            pass

        # Funcion de salir
        def salir():
            ''' Funcion que sale del sub menu cobrar cliente '''
            # Reiniciamos el frame
            self.reiniciar_frame_sub_opciones()
            # Destruimos los frames creados
            sub_frame1.destroy()
            sub_frame2.destroy()
            # Activamos los botones
            self.activ_botones_principales()
        
        # Funcion de Reinicio
        def reiniciar_frames():
            # Destruimos todas las opciones anteriores
            for widget in sub_frame1.winfo_children():
                widget.destroy()

            # Destruimos todas las opciones anteriores
            for widget in sub_frame2.winfo_children():
                widget.destroy()

        ## FUNCION PRINCIPAL ##
        # Destruimos todas las opciones anteriores
        self.reiniciar_frame_sub_opciones()
        # Invalidamos los botones principales
        self.desac_botones_principales()
        try:
            # Pedimos el codigo de usuario
            emp = MyDialogCodUsu(self.raiz, self.controlador).show_emp()
            # Verificamos el tipo de empleado
            self.controlador.verificar_tipo_empleado_cobros(emp)
        except Exception as e:
            # Reactivamos los botones principales
            self.activ_botones_principales()
            # Borramos todos las sub opciones
            self.reiniciar_frame_sub_opciones()
            # Informamos al usuario del error
            self.imprimir_error(str(e))
            self.frame.focus_force()
        else:
            # Frames
            sub_frame1 = MyFrame(self.raiz)
            sub_frame1.config(bg='white smoke', width=840, height=700)
            sub_frame1.place(x=200,y=125)
            sub_frame2 = MyFrame(self.raiz)
            sub_frame2.config(bg='white', width=240, height=700)

            # Imagenes
            img_cobrar_cliente = self.get_image('./Vista/icons/cobrar.png')
            img_anular_factura = self.get_image('./Vista/icons/anular.png')
            img_recargar_cuentas = self.get_image('./Vista/icons/recargar.png')
            img_arquear_caja = self.get_image('./Vista/icons/cajero.png')
            img_agg_cliente = self.get_image('./Vista/icons/emp_agg.png')
            img_coloc_propina = self.get_image('./Vista/icons/bitcoin.png')
            img_salir = self.get_image('./Vista/icons/logout.png')

            # Etiquetas
            self.mostrar_usuario(emp)

            # Botones
            boton_cobrar_cliente = MyBoton(self.frame1, image=img_cobrar_cliente, text='    Cobrar    \n    Cliente   ', compound='top', command=lambda: cobrar_cliente(emp))
            boton_cobrar_cliente.place(x=140, y=18)
            boton_anular_factura = MyBoton(self.frame1, image=img_anular_factura,text='     Anular   \n    Factura   ', compound='top', command=lambda: anular_factura(emp))
            boton_anular_factura.place(x=260, y=18)
            boton_recargar_tab_cuentas = MyBoton(self.frame1, image=img_recargar_cuentas,text='Recargar Tabla\n  de Cuentas ', compound='top', command=reiniciar_tabla_cuentas)
            boton_recargar_tab_cuentas.place(x=378, y=18)
            boton_reporte_caja = MyBoton(self.frame1, image=img_arquear_caja, text='     Reporte    \n     Caja    ', compound='top', command=lambda: reporte_caja(emp))
            boton_reporte_caja.place(x=525, y=18)
            boton_agregar_cliente = MyBoton(self.frame1, image=img_agg_cliente, text='    Agregar   \n    Cliente   ', compound='top', command=lambda: self.crear_cliente(emp, reiniciar_frames))
            boton_agregar_cliente.place(x=660, y=18)
            boton_colocar_propina = MyBoton(self.frame1, image=img_coloc_propina, text='    Colocar    \n    Propina    ', compound='top', command=lambda: colocar_propina(emp))
            boton_colocar_propina.place(x=780, y=18)
            boton_salir = MyBoton(self.frame1, image=img_salir, text='\n      Salir     ', compound='top', command=lambda: salir())
            boton_salir.place(x=980, y=18)

            # Mostramos la tabla de cuentas abiertas
            self.mostrar_tabla_cuentas(sub_frame1)

            self.raiz.wait_window(self.frame1)

    def mostrar_sub_menu_admin_emp(self):
        '''' Muestra el sub menu de administracion de Empleados '''
        # Funciones Auxiliares #
        def crear_nuevo_emp(emp):
            ''' Funcion que obtiene los datos nuevos y los manda al controlador '''
            # Desactivamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                # Conseguimos los datos
                datos_new_emp = MyDialogCreateEmp(self.raiz).show_data()
                # Le pasamos al controlador
                self.controlador.crear_emp(emp, datos_new_emp)
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Avisamos que salio todo bien
                self.imprimir_aviso('Se Creo Correctamente el Nuevo Empleado')
                # Damos la atencion al la pagina principal
                self.frame1.focus_force()
        
        def mostrar_lista_emp():
            ''' Muestra la lista de empleados '''
            ## FUNCION PRINCIPAL ##
            # Reiniciamos los frames
            reiniciar_frames()
            sub_frame1.place(x=200,y=125)
            # Mostramos la tabal de facturas
            self.mostrar_tabla_empleados(sub_frame1)
            self.frame1.wait_window(sub_frame1)

        def colocar_porcetn_emp():
            # Desactivamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                # Pedimos el numero de cedula del empleado
                ruc_emp = MyDialogGetInfo(self.raiz, 'Admin Empleados',
                'Ingrese el RUC/Cedula del Empleado').show_data()
                # Le pasamos el dato al controlador y obtenemos al empleado
                emp_a_config = self.controlador.obtener_empleado(ruc_emp)
                list_datos_ganacia = MyDialogPayEmp(self.raiz, emp_a_config).show_data()
                # Vemos si quiso cambiar los datos
                if len(list_datos_ganacia[0]) == 0:
                    # Activamos los botones secundarios
                    self.activ_botones_secundarios()
                    # Damos la atencion al la pagina principal
                    self.frame1.focus_force()
                    # Salimos
                    return
                # Le pasamos al controlador para que realize los cambios #
                # (ruc_emp, list_tipo_ganancia, list_montos)
                self.controlador.admin_ganancia_emp(emp_a_config, list_datos_ganacia[0], list_datos_ganacia[1])
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Imprimimos el aviso
                self.imprimir_aviso('Se Cambio Correctamente la Ganancia del Empleado')
                # Damos la atencion al la pagina principal
                self.frame1.focus_force()

        def calcular_sueldo_emp():
            # Desactivamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                # Conseguimos los datos
                ruc_emp = MyDialogGetInfo(self.raiz, 'Admin Empleados',
                'Ingrese el RUC/Cedula del Empleado').show_data()
                # Le pasamos el dato al controlador y obtenemos al empleado
                emp_a_calcular = self.controlador.obtener_empleado(ruc_emp)
                # Pasamos el objeto empleado para mostrar los detalles | False: No va a pagar al empleado
                MyDialogCalcSueldEmp(self.raiz, emp_a_calcular, False)
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Damos la atencion al la pagina principal
                self.frame1.focus_force()

        def pagar_emp():
            # Desactivamos los botones secundarios
            self.desac_botones_secundarios()
            try:
                # Conseguimos los datos
                ruc_emp = MyDialogGetInfo(self.raiz, 'Admin Empleados',
                'Ingrese el RUC/Cedula del Empleado').show_data()
                # Le pasamos el dato al controlador y obtenemos al empleado
                # emp_a_calcular[0]: Pos_in_lista | emp_a_calcular[1]: Objeto Empleado
                emp_a_calcular = self.controlador.emp_in_lista_ruc(ruc_emp)
                # Pasamos el objeto empleado para mostrar los detalles | True: Va a pagar al empleado
                respuesta = MyDialogCalcSueldEmp(self.raiz, emp_a_calcular[1], True).show_data()
                if respuesta is True:
                    # Le decimos al controlador que pague al empleado
                    self.controlador.pagar_sueldo_emp(emp_a_calcular[0])
                else:
                    # Activamos los botones secundarios
                    self.activ_botones_secundarios()
                    # Damos la atencion al la pagina principal
                    self.frame1.focus_force()
                    # Salimos de la funcion
                    return
            except Exception as e:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Mostramos el error
                self.imprimir_error(str(e))
                self.frame1.focus_force()
            else:
                # Activamos los botones secundarios
                self.activ_botones_secundarios()
                # Imprimimos el aviso
                self.imprimir_aviso('Se Pago Correctamente al Empleado')
                ## Preguntamos si queremos imprimir el comprobante de apgo ##
                # Damos la atencion al la pagina principal
                self.frame1.focus_force()

        # Funcion de salir
        def salir():
            # Activamos los botones
            self.activ_botones_principales()
            # Destruimos los frames creados
            sub_frame1.destroy()
            # Reiniciamos el frame
            self.reiniciar_frame_sub_opciones()

        # Funcion de Reinicio
        def reiniciar_frames():
            # Destruimos todas las opciones anteriores
            for widget in sub_frame1.winfo_children():
                widget.destroy()

        ## FUNCION PRINCIPAL ##
        # Destruimos todas las opciones anteriores
        self.reiniciar_frame_sub_opciones()
        # Invalidamos los botones principales
        self.desac_botones_principales()
        try:
            # Pedimos el codigo de usuario
            emp = MyDialogCodUsu(self.raiz, self.controlador).show_emp()
            # Verificamos el tipo de empleado
            self.controlador.verificar_tipo_empleado_administracion(emp)
        except Exception as e:
            # Reactivamos los botones principales
            self.activ_botones_principales()
            # Borramos todos las sub opciones
            self.reiniciar_frame_sub_opciones()
            # Informamos al usuario del error
            self.imprimir_error(str(e))
            self.frame.focus_force()
        else:
            # Frames
            sub_frame1 = MyFrame(self.raiz)
            sub_frame1.config(bg='white smoke', width=1160, height=700)

            # Imagenes
            img_nuevo_emp = self.get_image('./Vista/icons/emp_agg.png')
            img_lista_emp = self.get_image('./Vista/icons/archivo.png')
            img_porcent_emp = self.get_image('./Vista/icons/lista.png')
            img_calc_sueldo = self.get_image('./Vista/icons/calculadora.png')
            img_pagar_emp = self.get_image('./Vista/icons/pago.png')
            img_salir = self.get_image('./Vista/icons/logout.png')

            # Etiquetas
            self.mostrar_usuario(emp)

            # Botones
            boton_crear_emp = MyBoton(self.frame1, image=img_nuevo_emp, text='Crear Nuevo\n  Empleado ', compound='top', command=lambda: crear_nuevo_emp(emp))
            boton_crear_emp.place(x=120, y=18)
            boton_mostrar_emp = MyBoton(self.frame1, image=img_lista_emp, text='Mostrar Lista\n  Empleados  ', compound='top', command=lambda: mostrar_lista_emp())
            boton_mostrar_emp.place(x=230, y=18)
            boton_porcent_emp = MyBoton(self.frame1, image=img_porcent_emp, text='Editar Porcentaje\n    Empleados   ', compound='top', command=lambda: colocar_porcetn_emp())
            boton_porcent_emp.place(x=350, y=18)
            boton_calc_sueldo_emp = MyBoton(self.frame1, image=img_calc_sueldo, text='Calcular Sueldo\n    Empleado   ', compound='top', command=lambda: calcular_sueldo_emp())
            boton_calc_sueldo_emp.place(x=497, y=18)
            boton_pagar_emp = MyBoton(self.frame1, image=img_pagar_emp, text=' Pagar \n  Empleado  ', compound='top', command=lambda: pagar_emp())
            boton_pagar_emp.place(x=640, y=18)
            boton_salir = MyBoton(self.frame1, image=img_salir, text='\n      Salir     ', compound='top', command=lambda: salir())
            boton_salir.place(x=980, y=18)

            self.raiz.wait_window(self.frame1)

    def mostrar_sub_menu_facturacion(self):
        '''' Muestra el sub menu de facturacion '''
        # Funcion de salir
        def salir():
            # Activamos los botones
            self.activ_botones_principales()
            # Reiniciamos el frame
            self.reiniciar_frame_sub_opciones()

        ## Metodo Principal ##
        # Destruimos todas las opciones anteriores
        self.reiniciar_frame_sub_opciones()
        # Invalidamos los botones principales
        self.desac_botones_principales()
        try:
            # Pedimos el codigo de usuario
            emp = MyDialogCodUsu(self.raiz, self.controlador).show_emp()
        except Exception as e:
            # Reactivamos los botones principales
            self.activ_botones_principales()
            # Borramos todos las sub opciones
            self.reiniciar_frame_sub_opciones()
            # Informamos al usuario del error
            self.imprimir_error(str(e))
            self.frame.focus_force()
        else:
            pass

    def mostrar_sub_menu_clientes(self):
        '''' Muestra el sub menu de administracion de Clientes '''
        # Funcion de salir
        def salir():
            # Activamos los botones
            self.activ_botones_principales()
            # Reiniciamos el frame
            self.reiniciar_frame_sub_opciones()

        # Destruimos todas las opciones anteriores
        self.reiniciar_frame_sub_opciones()
        # Invalidamos los botones principales
        self.desac_botones_principales()
        try:
            # Pedimos el codigo de usuario
            emp = MyDialogCodUsu(self.raiz, self.controlador).show_emp()
        except Exception as e:
            # Reactivamos los botones principales
            self.activ_botones_principales()
            # Borramos todos las sub opciones
            self.reiniciar_frame_sub_opciones()
            # Informamos al usuario del error
            self.imprimir_error(str(e))
            self.frame.focus_force()
        else:
            pass

    def mostrar_sub_menu_stock(self):
        '''' Muestra el sub menu de cobros '''
        # Funcion de salir
        def salir():
            # Activamos los botones
            self.activ_botones_principales()
            # Reiniciamos el frame
            self.reiniciar_frame_sub_opciones()

        # Destruimos todas las opciones anteriores
        self.reiniciar_frame_sub_opciones()
        # Invalidamos los botones principales
        self.desac_botones_principales()
        try:
            # Pedimos el codigo de usuario
            emp = MyDialogCodUsu(self.raiz, self.controlador).show_emp()
        except Exception as e:
            # Reactivamos los botones principales
            self.activ_botones_principales()
            # Borramos todos las sub opciones
            self.reiniciar_frame_sub_opciones()
            # Informamos al usuario del error
            self.imprimir_error(str(e))
            self.frame.focus_force()
        else:
            pass

    def mostrar_info_prosoft(self):
        '''' Muestra informacion de ProSoft '''
        # Destruimos todas las opciones anteriores
        self.reiniciar_frame_sub_opciones()

    ### FUNCIONES DE PARA MUCHOS SUBMENUS ###
    def crear_cliente(self, emp, reiniciar_frames):
        ''' Funcion que crea un Cliente '''
        # Reinicamos los Sub Frames
        reiniciar_frames()
        # Desactivamos los botones secundarios
        self.desac_botones_secundarios()
        try:
            # Pedimos los datos
            list_datos_cl = MyDialogCreateClient(self.raiz).show_data()
            # Le pasamos los datos al controlador
            self.controlador.crear_cliente(emp, list_datos_cl)
        except Exception as e:
            # Activamos los botones secundarios
            self.activ_botones_secundarios()
            # Mostramos el error
            self.imprimir_error(str(e))
            self.frame1.focus_force()
        else:
            # Activamos los botones secundarios
            self.activ_botones_secundarios()
            # Avisamos que salio todo bien
            self.imprimir_aviso('Se creo correctamente el nuevo Cliente')
            self.frame1.focus_force()

    ## FUNCIONES PARA ACTIVAR/DESACTIVAR BOTONES PRINCIPALES Y SECUNDARIOS ##
    def activ_botones_principales(self):
        ''' Funcion que activa los botones principales '''
        self.boton_atender.config(state='normal')
        self.boton_clientes.config(state='normal')
        self.boton_cobrar.config(state='normal')
        self.boton_empleados.config(state='normal')
        self.boton_fact.config(state='normal')
        self.boton_info.config(state='normal')
        self.boton_stock.config(state='normal')

    def desac_botones_principales(self):
        ''' Funcion que desactivo los botones principales '''
        self.boton_atender.config(state='disable')
        self.boton_clientes.config(state='disable')
        self.boton_cobrar.config(state='disable')
        self.boton_empleados.config(state='disable')
        self.boton_fact.config(state='disable')
        self.boton_info.config(state='disable')
        self.boton_stock.config(state='disable')

    def activ_botones_secundarios(self):
        ''' Activa los botones secundarios '''
        for widget in self.frame1.winfo_children():
            widget.config(state='normal')

    def desac_botones_secundarios(self):
        ''' Desactiva los botones secundarios '''
        for widget in self.frame1.winfo_children():
            widget.config(state='disable')

    ## FUNCIONES PARA MENSAJES ##
    def imprimir_error(self, cadena):
        messagebox.showerror('ERROR', cadena)

    def imprimir_aviso(self, cadena):
        messagebox.showinfo('AVISO', cadena)

    ## FUNCIONES PARA LAS IMAGENES Y FRAMES ##
    def get_image(self, ruta_img):
        ''' Obtiene y redimensiona una imagen '''
        # Abrimos la imagen
        imagen = Image.open(ruta_img)
        # Redimensionamos la imagen
        imagen = imagen.resize((50,50), Image.ANTIALIAS)
        # La guardamos en un formato de Tkinter
        imagen = ImageTk.PhotoImage(imagen)
        # Retornamos la imagen
        return imagen

    def reiniciar_frame_sub_opciones(self):
        ''' Reinicia las opciones del frame de sub opciones '''
        # Destruimos todas las opciones anteriores
        for widget in self.frame1.winfo_children():
            widget.destroy()

    def mostrar_usuario(self, emp):
        ''' Muestra el Usuario logeado '''
        # Etiquetas
        nom_usu = emp.nombre + '\n' + emp.apellido
        usu_label = MyLabel(self.frame1, text='Usuario:', bg='lightgray', anchor=tk.W)
        usu_label.config(font=('Times', 20, 'bold'), fg='black')
        usu_label.place(x=15, y=18)
        usu_ingresado = MyLabel(self.frame1, text=nom_usu, bg='lightgray', anchor=tk.W)
        usu_ingresado.config(font=('Times', 18), fg='black')
        usu_ingresado.place(x=15, y=45)

    ## FUNCIONES PARA LAS TABLAS ##
    def mostrar_tabla_cuentas(self, frame):
        ''' Muestra la lista de Cuentas Abiertas '''
        # Obtenemos la lista de cuentas abiertas
        # 0 Corresponde al numero de sucursal
        list_cl_cuentas = self.controlador.model.obtener_lista_cl_cuenta(0)
        # Creamos la tabla
        self.tabla_cuenta_clientes = MyTable(frame)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_cuenta_clientes['columns'] = ('one', 'two', 'three')
        self.tabla_cuenta_clientes.column('#0', width=50, minwidth=50)
        self.tabla_cuenta_clientes.column('one', width=120, minwidth=120)
        self.tabla_cuenta_clientes.column('two', width=320, minwidth=320)
        self.tabla_cuenta_clientes.column('three', width=310, minwidth=310)
        # Personalizamos los encabezados
        self.tabla_cuenta_clientes.heading('#0', text='Nº', anchor=tk.W)
        self.tabla_cuenta_clientes.heading('one', text='CEDULA', anchor=tk.W)
        self.tabla_cuenta_clientes.heading('two', text='NOMBRE', anchor=tk.W)
        self.tabla_cuenta_clientes.heading('three', text='APELLIDO', anchor=tk.W)
        # Cargamos la tabla
        for i in range(len(list_cl_cuentas)):
            self.tabla_cuenta_clientes.insert('', tk.END, text=(i+1), values=(list_cl_cuentas[i].ruc, list_cl_cuentas[i].nombre, list_cl_cuentas[i].apellido))
        # Colocamos la tabla
        self.tabla_cuenta_clientes.pack(padx=15, pady=9) 

    def mostrar_tabla_facturas(self, frame):
        # Obtenemos la lista de cuentas abiertas
        # 0 Corresponde al numero de sucursal
        list_facturas_caja = self.controlador.model.obtener_facturas_caja(0, 0) # 0: NUM_CAJA, 0:NUM_SUCUR
        # Creamos la tabla
        self.tabla_facturas = MyTable(frame)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_facturas['columns'] = ('one', 'two', 'three')
        self.tabla_facturas.column('#0', width=50, minwidth=50)
        self.tabla_facturas.column('one', width=120, minwidth=120)
        self.tabla_facturas.column('two', width=320, minwidth=320)
        self.tabla_facturas.column('three', width=310, minwidth=310)
        # Personalizamos los encabezados
        self.tabla_facturas.heading('#0', text='Nº', anchor=tk.W)
        self.tabla_facturas.heading('one', text='NUM FACTURA', anchor=tk.W)
        self.tabla_facturas.heading('two', text='CLIENTE', anchor=tk.W)
        self.tabla_facturas.heading('three', text='MONTO TOTAL', anchor=tk.W)
        # Cargamos la tabla
        for i in range(len(list_facturas_caja)):
            # Guardamos los datos de la factura
            num_factura = str(list_facturas_caja[i].num_factura)
            nom_cliente = list_facturas_caja[i].cliente.nombre + ' ' + list_facturas_caja[i].cliente.apellido
            monto_total = str(list_facturas_caja[i].calcular_total_pagar())
            # Lo insertamos dentro de la tabla
            self.tabla_facturas.insert('', tk.END, text=(i+1), values=(num_factura, nom_cliente, monto_total))
        # Colocamos la tabla
        self.tabla_facturas.pack(padx=15, pady=9)

    def mostrar_tabla_empleados(self, frame):
        ''' Muestra la lista de empleados '''
        # Obtenemos la lista de cuentas abiertas
        # 0 Corresponde al numero de sucursal
        list_empleados = self.controlador.model.obtener_empleados(0)
        # Creamos la tabla
        self.tabla_empleados = MyTable(frame)
        ## Configuramos y cargamos la tabla ##
        # Configuramos las columnas
        self.tabla_empleados['columns'] = ('one', 'two', 'three')
        self.tabla_empleados.column('#0', width=185, minwidth=185)
        self.tabla_empleados.column('one', width=300, minwidth=300)
        self.tabla_empleados.column('two', width=300, minwidth=300)
        self.tabla_empleados.column('three', width=260, minwidth=260)
        # Personalizamos los encabezados
        self.tabla_empleados.heading('#0', text='RUC', anchor=tk.W)
        self.tabla_empleados.heading('one', text='NOMBRE', anchor=tk.W)
        self.tabla_empleados.heading('two', text='APELLIDO', anchor=tk.W)
        self.tabla_empleados.heading('three', text='CODIGO USUARIO', anchor=tk.W)
        # Cargamos la tabla
        for i in range(len(list_empleados)):
            self.tabla_empleados.insert('', tk.END, text=(list_empleados[i].ruc), 
            values=(list_empleados[i].nombre, list_empleados[i].apellido, 
            list_empleados[i].usuario.obtener_codigo()))
        # Colocamos la tabla
        self.tabla_empleados.pack(padx=15, pady=9) 

    ## FUNCION PARA CONFIRMAR SALIDA DE PROSOFT ##
    def cerrando_app(self):
        ''' Funcion que confirma la salida de la App '''
        respuesta = messagebox.askyesno('ProSoft','¿Desea Salir de ProSoft?')
        if respuesta is True:
            self.raiz.destroy()
        else:
            self.raiz.focus_force()