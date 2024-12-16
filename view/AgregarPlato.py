import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from controller.Funciones import registrar_plato


class AgregarPlato():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="500")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Agregar Plato")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Agregar Plato", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        #ID texto
        self.lblId = Label(self.ventanaCliente, text="ID*", font=("Arial", 15))
        self.lblId.place(x=90, y=100)
        
        # Validación para números, espacios y caja de texto
        validate_id = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtId = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_id, '%P'))
        self.txtId.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtId, "Solo se permiten números")
        
        #Nombre texto
        self.lblNombre = Label(self.ventanaCliente, text="Nombre*", font=("Arial", 15))
        self.lblNombre.place(x=90, y=150)
        
        # Validación para letras, tildes y espacios y caja de texto
        validate_nombre = self.ventanaCliente.register(lambda texto: all(c.isalpha() or c in " áéíóúÁÉÍÓÚñÑ" for c in texto))
        self.txtNombre = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_nombre, '%P'))
        self.txtNombre.place(x=230, y=150, width=200, height=25)
        self.create_tooltip(self.txtNombre, "Solo se permiten letras")
        
        #Precio texto
        self.lblPrecio= Label(self.ventanaCliente, text="Precio*", font=("Arial", 15))
        self.lblPrecio.place(x=90, y=200)
        
        # Validación para números, puntos ".", espacios y caja de texto
        validate_precio = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c in ". " for c in texto))
        self.txtPrecio = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_precio, '%P'))
        self.txtPrecio.place(x=230, y=200, width=200, height=25)
        self.create_tooltip(self.txtPrecio, "Formato: 0.00")
        
        #Cantidad Disponible texto
        self.lblCantidad_disponible = Label(self.ventanaCliente, text="Cantidad Disponible*", font=("Arial", 15))
        self.lblCantidad_disponible.place(x=40, y=250)
        
        # Validación para números, espacios y caja de texto
        validate_cantidad_disponible = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtCantidad_disponible = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_cantidad_disponible, '%P'))
        self.txtCantidad_disponible.place(x=230, y=250, width=200, height=25)
        self.create_tooltip(self.txtCantidad_disponible, "Solo se permiten números")
        
        #Descripcion texto
        self.lblDescripcion = Label(self.ventanaCliente, text="Descripcion*", font=("Arial", 15))
        self.lblDescripcion.place(x=90, y=300)
        
        #Descripcion caja de texto
        self.txtDescripcion = Entry(self.ventanaCliente)
        self.txtDescripcion.place(x=230, y=300, width=200, height=100)

        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16)  
        img_guardar = PhotoImage(file=r"icons\guardar-datos.png").subsample(16) 
        
        #Boton Guardar
        self.btnGuardar = Button(self.ventanaCliente, image = img_guardar, command=self.guardar_platos)
        self.btnGuardar.place(x=140, y=415, height=40, width=110)
        self.btnGuardar.image = img_guardar
        self.create_tooltip(self.btnGuardar, "Guardar Platos")
        
        #Boton Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir, command=self.salir)
        self.btnSalir.place(x=300, y=415, height=40, width=110)
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


    def guardar_platos(self):
        # Obtiene los datos de los campos de entrada
        id = self.txtId.get()
        nombre = self.txtNombre.get()
        precio = self.txtPrecio.get()
        cantidad_disponible = self.txtCantidad_disponible.get()
        descripcion = self.txtDescripcion.get()

        # Validación de datos
        if not id or not nombre or not precio or not cantidad_disponible or not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos obligatorios")
            return
        
        try:
            # Llama a la función para registrar al chef
            registrar_plato(id, nombre, precio, cantidad_disponible, descripcion)
            messagebox.showinfo("Éxito", "Plato registrado con éxito")
            
            # Limpia los campos después de guardar
            self.txtId.delete(0, 'end')
            self.txtNombre.delete(0, 'end')
            self.txtPrecio.delete(0, 'end')
            self.txtCantidad_disponible.delete(0, 'end')
            self.txtDescripcion.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {e}")
            
    def salir(self):
        self.ventanaCliente.destroy()