# Importamos la libreria ZODB y transaction
from ZODB import FileStorage, DB
from ZEO import ClientStorage
import transaction

class MiZODB(object):
    ''' Base de Datos '''
    def __init__(self, addr):
        ''' Levanta una base de Datos '''
        # Opcion con FileStorage
        #self.storage = FileStorage.FileStorage(addr)
        ## Opcion con ClientStorage - Funcion Cliente-Servidor ##
        self.storage = ClientStorage.ClientStorage(addr, cache_size=1000)
        self.db = DB(self.storage, cache_size=1000)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()

    def close(self):
        ''' Sirve para cerrar la base de Datos '''
        self.conexion.close()
        self.db.close()
        self.storage.close()