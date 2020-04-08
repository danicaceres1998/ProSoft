from model import Model
# Importamos el path
from sys import path
path.append('./Nucleo')
from superAdministrador import SuperAdministrador

modelo = Model()

'''facturas = modelo.obtener_facturas(0)
for fc in facturas:
    print(fc.mostrar_datos_factura(), ' - ', fc.num_factura)
    fp = fc.formas_pago
    for f in fp:
        print(f.obtener_tipo_pago())

cajas = modelo.obtener_cajas(0)

print(cajas[0].total_efectivo)
print(cajas[0].total_tarjeta)
empleados = []
superadmin = SuperAdministrador('4251724', 'Juan', 'Ojeda', '+595971160145', 'Luque')
superadmin.crear_usuario('superadmin123')
empleados.append(superadmin)
usuarios = []
usuarios.append(superadmin.usuario)
modelo.actualizar_empleados(empleados, 0)
modelo.actualizar_usuarios(usuarios, 0)'''
emplead = modelo.obtener_empleados(0)
for emp in emplead:
    print(emp.obtener_datos(True))

print(emplead[0].porcent_servicios)
'''cajas[0].arquear_caja()
modelo.actualizar_cajas(cajas, 0)
modelo.actualizar_clientes([], 0)
modelo.actualizar_facturas([], 0)
modelo.actualizar_lista_cl_cuenta([], 0)
modelo.actualizar_empleados([], 0)'''