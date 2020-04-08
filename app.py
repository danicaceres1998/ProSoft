# Importamos las clases necesarias
from Nucleo.software import Software # Va a hacer el papel de controlador
from Vista.myview import ViewApp # Va a hacer el papel de Interaccion con el usuario
from tkinter import messagebox

##### MAIN APP #####
if __name__ == "__main__":
    try:
        # Instanciamos el controlador
        controler = Software()
    except:
        messagebox.showerror('ERROR', 'NO TIENE CONEXION A LA BASE DE DATOS')
    else:
        # Instanciamos la vista
        view = ViewApp(controler)
        # Corremos el programa
        view.run_app()
