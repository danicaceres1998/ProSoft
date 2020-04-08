# Importamos la libreria abc
from abc import ABCMeta, abstractmethod

class Empresa(metaclass = ABCMeta):
    ''' Abstraccion de una empresa '''
    def __init__(self, nombre, ruc, contacto):
        self.nombre = nombre
        self.ruc = ruc
        self.contactos = []
        # Agregamos el contacto recibido
        self.contactos.append(contacto)
