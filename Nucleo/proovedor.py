# Importamos la clase empresa
from empresa import Empresa

class Proveedor(Empresa):
    ''' Abstraccion de un Proveedor '''
    # Atributo Estatico
    cant_proveedores = 0

    def __init__(self, nombre, ruc):
        self.nombre = nombre
        self.ruc = ruc
        self.contactos = []
        self.__class__.cant_proveedores += 1

    # Metodo Propio
    def agregar_contacto(self, contacto):
        ''' Agrega un contacto numerico al proveedor '''
        self.contactos.append(contacto)
