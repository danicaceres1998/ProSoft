
class Usuario:
    ''' Abstraccion de un Usuario '''
    # Atributo estatico
    cant_usuarios = 0

    # Metodos
    def __init__(self, codigo):
        self.codigo = codigo

    def obtener_codigo(self):
        ''' Retorna el codigo del Usuario '''
        return self.codigo