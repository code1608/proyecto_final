import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from model.ConexionDB import Conexion
from controller.Funciones import eliminar_chef 

class EliminarChef():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="450")
        self.ventanaCliente.resizable(0, 0)
        self.ventanaCliente.title("Eliminar Chef")
        
        # Título principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Eliminar Chef", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        # Campos de entrada
        self.lblCedula = Label(self.ventanaCliente, text="Cedula*", font=("Arial", 15))
        self.lblCedula.place(x=90, y=100)

        # Validación para números, puntos "." y espacios y caja de texto
        validate_cedula = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c in ". " for c in texto))
        self.txtCedula = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_cedula, '%P'))
        self.txtCedula.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtCedula, "Solo se permiten números y puntos")

        self.lblNombre = Label(self.ventanaCliente, text="Nombre*", font=("Arial", 15))
        self.lblNombre.place(x=90, y=150)
        self.txtNombre = Entry(self.ventanaCliente, state="disabled")
        self.txtNombre.place(x=230, y=150, width=200, height=25)

        self.lblApellido = Label(self.ventanaCliente, text="Apellido*", font=("Arial", 15))
        self.lblApellido.place(x=90, y=200)
        self.txtApellido = Entry(self.ventanaCliente, state="disabled")
        self.txtApellido.place(x=230, y=200, width=200, height=25)

        self.lblTelefono = Label(self.ventanaCliente, text="Telefono*", font=("Arial", 15))
        self.lblTelefono.place(x=90, y=250)
        self.txtTelefono = Entry(self.ventanaCliente, state="disabled")
        self.txtTelefono.place(x=230, y=250, width=200, height=25)

        self.lblEmail = Label(self.ventanaCliente, text="Email*", font=("Arial", 15))
        self.lblEmail.place(x=90, y=300)
        self.txtEmail = Entry(self.ventanaCliente, state="disabled")
        self.txtEmail.place(x=230, y=300, width=200, height=25)

        #Iconos
        img_buscar = PhotoImage(file=r"icons\buscar.png").subsample(16) 
        img_eliminar = PhotoImage(file=r"icons\guardar-datos.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 

        # Botón Buscar 
        self.btnBuscar = Button(self.ventanaCliente, image = img_buscar, command=self.buscar_chef)
        self.btnBuscar.place(x=60, y=370, height=40, width=110)
        self.btnBuscar.image = img_buscar
        self.create_tooltip(self.btnBuscar, "Buscar Chef")
        
        
        # Botón Guardar 
        self.btnEliminar = Button(self.ventanaCliente, image = img_eliminar, command=self.eliminar_chef) 
        self.btnEliminar.place(x=190, y=370, height=40, width=110)
        self.btnEliminar.image = img_eliminar
        self.create_tooltip(self.btnEliminar, "Eliminar Chef")
        
        # Botón Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir, command=self.salir)
        self.btnSalir.place(x=315, y=370, height=40, width=110)
        self.btnSalir.image = img_salir
        self.create_tooltip(self.btnSalir, "Salir")

        self.tooltip = None 
        
    def create_tooltip(self, widget, text):
        """Crear un tooltip simple para un widget."""
        tooltip = Label(self.ventanaCliente, text=text, background="#aed6f1", borderwidth=1, relief="solid", font=("Arial", 12))
        tooltip.place_forget()
        
        def show_tooltip(event):
            x = widget.winfo_x() + (widget.winfo_width() // 2) - (tooltip.winfo_width() // 2)
            y = widget.winfo_y() - tooltip.winfo_height() - 5
            tooltip.place(x=x, y=y)

        def hide_tooltip(event):
            tooltip.place_forget()

        # Eventos para mostrar y ocultar el tooltip
        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)

    # Función para eliminar un chef
    def eliminar_chef(self):
        cedula = self.txtCedula.get()
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        telefono = self.txtTelefono.get()
        email = self.txtEmail.get()

        if not cedula and not nombre and not apellido and not telefono and not email:
            messagebox.showwarning("Advertencia", "Por favor, ingrese al menos un dato para buscar")
            return

        try:
            # Llama a la función eliminar_chef con los datos
            eliminar_chef(cedula, nombre, apellido, telefono, email)
            messagebox.showinfo("Éxito", "Chef eliminado con éxito")

            # Limpiar campos
            self.txtCedula.delete(0, 'end')
            self.txtNombre.delete(0, 'end')
            self.txtApellido.delete(0, 'end')
            self.txtTelefono.delete(0, 'end')
            self.txtEmail.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar/eliminar el chef: {e}")

    # Función para buscar el chef
    def buscar_chef(self):
        """Busca un chef por cédula y llena los campos deshabilitados si existe."""
        cedula = self.txtCedula.get()

        if not cedula:
            messagebox.showwarning("Advertencia", "Por favor, ingrese la cédula para buscar")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Consulta para buscar un chef por cédula
            consulta = "SELECT nombre, apellido, telefono, email FROM chef WHERE cedula = %s"
            cursor.execute(consulta, (cedula,))
            resultado = cursor.fetchone()

            if resultado:
                # Llenar los campos con los datos encontrados
                self.txtNombre.config(state="normal")
                self.txtApellido.config(state="normal")
                self.txtTelefono.config(state="normal")
                self.txtEmail.config(state="normal")

                self.txtNombre.delete(0, 'end')
                self.txtNombre.insert(0, resultado[0])

                self.txtApellido.delete(0, 'end')
                self.txtApellido.insert(0, resultado[1])

                self.txtTelefono.delete(0, 'end')
                self.txtTelefono.insert(0, resultado[2])

                self.txtEmail.delete(0, 'end')
                self.txtEmail.insert(0, resultado[3])

                self.txtNombre.config(state="readonly")
                self.txtApellido.config(state="readonly")
                self.txtTelefono.config(state="readonly")
                self.txtEmail.config(state="readonly")
            else:
                messagebox.showwarning("Advertencia", "No se encontró un chef con la cédula proporcionada")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el chef: {e}")
        finally:
            mi_conexion.cerrarConexion()

    # Función para salir
    def salir(self):
        self.ventanaCliente.destroy()
