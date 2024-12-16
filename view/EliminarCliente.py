import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from model.ConexionDB import Conexion
from controller.Funciones import eliminar_cliente

class EliminarCliente():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="450")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Eliminar Cliente")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Eliminar Cliente", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        #Cedula texto
        self.lblCedula = Label(self.ventanaCliente, text="Cedula*", font=("Arial", 15))
        self.lblCedula.place(x=90, y=100)
        
        # Validación para números, puntos "." y espacios y caja de texto
        validate_cedula = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c in ". " for c in texto))
        self.txtCedula = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_cedula, '%P'))
        self.txtCedula.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtCedula, "Solo se permiten números y puntos")
        
        #Nombre texto
        self.lblNombre = Label(self.ventanaCliente, text="Nombre*", font=("Arial", 15))
        self.lblNombre.place(x=90, y=150)
        
        #Nombre caja de texto
        self.txtNombre = Entry(self.ventanaCliente, state="disabled")
        self.txtNombre.place(x=230, y=150, width=200, height=25)
        
        #Apellido texto
        self.lblApellido= Label(self.ventanaCliente, text="Apellido*", font=("Arial", 15))
        self.lblApellido.place(x=90, y=200)
        
        #Apellido caja de texto
        self.txtApellido = Entry(self.ventanaCliente, state="disabled")
        self.txtApellido.place(x=230, y=200, width=200, height=25)
        
        #Telefono texto
        self.lblTelefono= Label(self.ventanaCliente, text="Telefono*", font=("Arial", 15))
        self.lblTelefono.place(x=90, y=250)
        
        #Telefono caja de texto
        self.txtTelefono = Entry(self.ventanaCliente, state="disabled")
        self.txtTelefono.place(x=230, y=250, width=200, height=25)
        
        #Email texto
        self.lblEmail= Label(self.ventanaCliente, text="Email*", font=("Arial", 15))
        self.lblEmail.place(x=90, y=300)
        
        #Email caja de texto
        self.txtEmail = Entry(self.ventanaCliente, state="disabled")
        self.txtEmail.place(x=230, y=300, width=200, height=25)

        #Iconos
        img_buscar = PhotoImage(file=r"icons\buscar.png").subsample(16) 
        img_eliminar = PhotoImage(file=r"icons\guardar-datos.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 
        
        #Boton Buscar
        self.btnBuscar = Button(self.ventanaCliente, image = img_buscar, command=self.buscar_cliente)
        self.btnBuscar.place(x=60, y=370, height=40, width=110)
        self.btnBuscar.image = img_buscar
        self.create_tooltip(self.btnBuscar, "Buscar Cliente")
        
        #Boton Elimiar
        self.btnEliminar = Button(self.ventanaCliente, image = img_eliminar, command=self.eliminar_cliente)
        self.btnEliminar.place(x=190, y=370, height=40, width=110)
        self.btnEliminar.image = img_eliminar
        self.create_tooltip(self.btnEliminar, "Eliminar Cliente")
        
        #Boton Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir, command=self.salir)
        self.btnSalir.place(x=315, y=370, height=40, width=110)
        self.btnSalir.image = img_salir
        self.create_tooltip(self.btnSalir, "Salir")

        self.tooltip = None  # Para almacenar el tooltip
        
    def create_tooltip(self, widget, text):
        """Crear un tooltip simple para un widget."""
        tooltip = Label(self.ventanaCliente, text=text, background="#aed6f1", borderwidth=1, relief="solid", font=("Arial", 12))
        tooltip.place_forget()  # Oculta el tooltip inicialmente
        
        def show_tooltip(event):
            x = widget.winfo_x() + (widget.winfo_width() // 2) - (tooltip.winfo_width() // 2)
            y = widget.winfo_y() - tooltip.winfo_height() - 5
            tooltip.place(x=x, y=y)

        def hide_tooltip(event):
            tooltip.place_forget()

        # Eventos para mostrar y ocultar el tooltip
        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)
        
    # Función para buscar y eliminar un mesero
    def eliminar_cliente(self):
        cedula = self.txtCedula.get()
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        telefono = self.txtTelefono.get()
        email = self.txtEmail.get()

        if not cedula and not nombre and not apellido and not telefono and not email:
            messagebox.showwarning("Advertencia", "Por favor, ingrese al menos un dato para buscar")
            return

        try:
            # Llama a la función eliminar_cliente con los datos
            eliminar_cliente(cedula, nombre, apellido, telefono, email)
            messagebox.showinfo("Éxito", "cliente eliminado con éxito")

            # Limpiar campos
            self.txtCedula.delete(0, 'end')
            self.txtNombre.delete(0, 'end')
            self.txtApellido.delete(0, 'end')
            self.txtTelefono.delete(0, 'end')
            self.txtEmail.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar/eliminar el cliente: {e}")

    # Función para buscar cliente
    def buscar_cliente(self):
        """Busca un cliente por su cédula ."""
        cedula = self.txtCedula.get()

        if not cedula:
            messagebox.showwarning("Advertencia", "Por favor, ingrese la cédula para buscar")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Consulta para buscar un cliente por cédula
            consulta = "SELECT nombre, apellido, telefono, email FROM cliente WHERE cedula = %s"
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
                messagebox.showwarning("Advertencia", "No se encontró un cliente con la cédula proporcionada")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el cliente: {e}")
        finally:
            mi_conexion.cerrarConexion()

    # Función para salir
    def salir(self):
        self.ventanaCliente.destroy()