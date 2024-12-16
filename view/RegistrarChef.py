import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import Label, Entry, Button, PhotoImage

class RegistrarChef:
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="450")
        self.ventanaCliente.resizable(0, 0)
        self.ventanaCliente.title("Registrar Chef")
        
        # Título principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Registrar Chef", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        # Campos y etiquetas
        self.lblCedula = Label(self.ventanaCliente, text="Cedula*", font=("Arial", 15))
        self.lblCedula.place(x=90, y=100)

        # Validación para números, puntos "." y espacios y caja de texto
        validate_cedula = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c in ". " for c in texto))
        self.txtCedula = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_cedula, '%P'))
        self.txtCedula.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtCedula, "Solo se permiten números y puntos")
        
        self.lblNombre = Label(self.ventanaCliente, text="Nombre*", font=("Arial", 15))
        self.lblNombre.place(x=90, y=150)

        # Validación para letras, tildes y espacios caja de texto
        validate_nombre = self.ventanaCliente.register(lambda texto: all(c.isalpha() or c in " áéíóúÁÉÍÓÚñÑ" for c in texto))
        self.txtNombre = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_nombre, '%P'))
        self.txtNombre.place(x=230, y=150, width=200, height=25)
        self.create_tooltip(self.txtNombre, "Solo se permiten letras y tildes para las letras")
        
        self.lblApellido = Label(self.ventanaCliente, text="Apellido*", font=("Arial", 15))
        self.lblApellido.place(x=90, y=200)

        # Validación para letras, tildes y espacios y caja de texto
        validate_apellido = self.ventanaCliente.register(lambda texto: all(c.isalpha() or c in " áéíóúÁÉÍÓÚñÑ" for c in texto))
        self.txtApellido = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_apellido, '%P'))
        self.txtApellido.place(x=230, y=200, width=200, height=25)
        self.create_tooltip(self.txtApellido, "Solo se permiten letras y tildes para las letras")
        
        self.lblTelefono = Label(self.ventanaCliente, text="Telefono*", font=("Arial", 15))
        self.lblTelefono.place(x=90, y=250)

        # Validación para números y espacios
        validate_telefono = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtTelefono = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_telefono, '%P'))
        self.txtTelefono.place(x=230, y=250, width=200, height=25)
        self.create_tooltip(self.txtTelefono, "Solo se permiten números")
        
        self.lblEmail = Label(self.ventanaCliente, text="Email*", font=("Arial", 15))
        self.lblEmail.place(x=90, y=300)
        self.txtEmail = Entry(self.ventanaCliente)
        self.txtEmail.place(x=230, y=300, width=200, height=25)

        #iconos
        img_guardar = PhotoImage(file=r"icons\guardar-datos.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 
        
        # Botón Guardar
        self.btnGuardar = Button(self.ventanaCliente, image = img_guardar, command=self.guardar_datos_chef)
        self.btnGuardar.place(x=140, y=370, height=40, width=110)
        self.btnGuardar.image = img_guardar
        self.create_tooltip(self.btnGuardar, "Guardar datos chef")
        
        # Botón Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir, command=self.ventanaCliente.destroy)
        self.btnSalir.place(x=300, y=370, height=40, width=110)
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
    
    def guardar_datos_chef(self):
        # Importación diferida para evitar ciclo
        from controller.Funciones import registrar_chef

        # Obtiene los datos de los campos de entrada
        cedula = self.txtCedula.get()
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        telefono = self.txtTelefono.get()
        email = self.txtEmail.get()

        # Validación de datos
        if not cedula or not nombre or not apellido or not telefono or not email:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos obligatorios")
            return
        
        try:
            # Llama a la función para registrar al chef
            registrar_chef(cedula, nombre, apellido, telefono, email)
            messagebox.showinfo("Éxito", "Chef registrado con éxito")
            
            # Limpia los campos después de guardar
            self.txtCedula.delete(0, 'end')
            self.txtNombre.delete(0, 'end')
            self.txtApellido.delete(0, 'end')
            self.txtTelefono.delete(0, 'end')
            self.txtEmail.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {e}")
            
    def salir(self):
        self.ventanaMesero.destroy()


