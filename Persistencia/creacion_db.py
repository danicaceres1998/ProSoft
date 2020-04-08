###### ESTE PROGRAMA SE USO UNICAMENTE PARA LA CREACION DE LA PRIMERA PELUQUERIA (SUCURSAL) ######
###### NO VOLVER A USAR. USAR EN CASO DE QUE NO EXISTA LA BASE DE DATOS ######
from sys import path
path.append('./Nucleo')
# Importamos la Base de Datos y la clase peluqueria
from mizodb import MiZODB, transaction
from peluqueria import Peluqueria
from superAdministrador import SuperAdministrador
from caja import Caja

# Levantamos la base de datos
db = MiZODB('Data.fs')
dbroot = db.raiz

# Creamos y agregamos
peluqueria = Peluqueria()
# Tenemos el Superadministrador
superadmin = SuperAdministrador('4251724', 'Juan', 'Ojeda', '+595971160145', 'Luque')
superadmin.crear_usuario('superadmin777')
# Tenemos la caja 
caja = Caja()
# Guardamos dentro de peluqueria
peluqueria.empleados.append(superadmin)
peluqueria.usuarios.append(superadmin.usuario)
peluqueria.cajas.append(caja)

# Guardamos en la base de datos
dbroot[peluqueria.NUM_SUCUR] = peluqueria

# Realizamos la transaccion y cerramos la conexion
transaction.commit()
db.close()