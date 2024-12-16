from tkinter import messagebox
from model.ConexionDB import Conexion
from view.MenuCajero import MenuCajero
from view.MenuChef import MenuChef
from view.MenuMesero import MenuMesero

class User:
    def __init__(self): #inicializamos un método constructor
        self.cedula = None #inicializamos una variable cedula como NONE 
        self.nombre = None #inicializamos una variable nombre como NONE
        self.rol = None #inicializamos una variable rol como NONE

    def iniciar_sesion(self, nombre_usuario, password, loggin): # Inicializamos la función iniciar_sesion

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Ejecuta la consulta con los parámetros ingresados
            consulta = "SELECT cedula, nombre, rol FROM admi WHERE nombre = %s AND cedula = %s"
            cursor.execute(consulta, (nombre_usuario, password))
            resultado = cursor.fetchone()
            
            if resultado:
                # Si encontró el usuario, asigna los valores y muestra el mensaje
                self.cedula, self.nombre, self.rol = resultado

                # Redirige a la interfaz correspondiente según el rol
                if self.rol == "cajero":
                    messagebox.showinfo("Acceso correcto", "Bienvenido, Cajero")
                    app = MenuCajero(loggin, self)
                elif self.rol == "chef":
                    messagebox.showinfo("Acceso correcto", "Bienvenido, Chef")
                    app = MenuChef(loggin, self)
                elif self.rol == "mesero":
                    messagebox.showinfo("Acceso correcto", "Bienvenido, mesero")
                    app = MenuMesero(loggin, self)
                else:
                    messagebox.showinfo("Acceso correcto", f"Bienvenido, {self.rol.capitalize()}")
                    # Añade aquí la lógica para otros roles, si es necesario
                return True
            else:
                # Si no encontró el usuario, muestra advertencia
                messagebox.showwarning("Advertencia", "El nombre de usuario y/o contraseña no existen, verifique e intente nuevamente")
                return False
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
            return False
        finally:
            # Cierra la conexión
            mi_conexion.cerrarConexion()

