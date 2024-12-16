import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from controller.Funciones import registrar_mesa


class AgregarMesa():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="350")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Agregar Mesa")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Agregar Mesa", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        #ID texto
        self.lblId = Label(self.ventanaCliente, text="ID*", font=("Arial", 15))
        self.lblId.place(x=90, y=100)
        
        # Validación para números, espacios y caja de texto
        validate_id = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtId = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_id, '%P'))
        self.txtId.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtId, "Ingrese el ID de la mesa")
        
        #Cantidad Comensales texto
        self.lblCantidad_comensales = Label(self.ventanaCliente, text="Cantidad Comensales*", font=("Arial", 15))
        self.lblCantidad_comensales.place(x=20, y=150)
        
        # Validación para números, espacios y caja de texto
        validate_cantidad_comensales = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtCantidad_comensales = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_cantidad_comensales, '%P'))
        self.txtCantidad_comensales.place(x=230, y=150, width=200, height=25)
        self.create_tooltip(self.txtCantidad_comensales, "Ingrese la cantidad de comensales")
        
        #Estado texto
        self.lblEstado= Label(self.ventanaCliente, text="Estado*", font=("Arial", 15))
        self.lblEstado.place(x=69, y=200)

        # Validación para letras, tildes y espacios y caja de texto
        validate_estado = self.ventanaCliente.register(lambda texto: all(c.isalpha() or c in " áéíóúÁÉÍÓÚñÑ" for c in texto))
        self.txtEstado = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_estado, '%P'))
        self.txtEstado.place(x=230, y=200, width=200, height=25)
        self.create_tooltip(self.txtEstado, "Ingrese el estado de la mesa")
    
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16)  
        img_guardar = PhotoImage(file=r"icons\guardar-datos.png").subsample(16) 
    
        #Boton Guardar
        self.btnGuardar = Button(self.ventanaCliente, image=img_guardar, command=self.guardar_mesa)
        self.btnGuardar.place(x=140, y=270, height=40, width=110)
        self.btnGuardar.image = img_guardar
        self.create_tooltip(self.btnGuardar, "Guardar Mesas")
        
        #Boton Salir
        self.btnSalir = Button(self.ventanaCliente, image=img_salir, command=self.salir)
        self.btnSalir.place(x=300, y=270, height=40, width=110)
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


    def guardar_mesa(self):
        # Obtener datos de los campos
        id = self.txtId.get()
        cantidad_comensales = self.txtCantidad_comensales.get()
        estado = self.txtEstado.get()

        # Validar datos obligatorios
        if not id or not cantidad_comensales or not estado:
            messagebox.showwarning("Advertencia", "Los campos ID, Cantidad de Comensales y Estado son obligatorios")
            return

        try:
            # Llama a la función de registrar_mesa
            registrar_mesa(id, cantidad_comensales, estado)
            messagebox.showinfo("Éxito", "Mesa registrada con éxito")

            # Limpiar los campos después de guardar
            self.txtId.delete(0, 'end')
            self.txtCantidad_comensales.delete(0, 'end')
            self.txtEstado.delete(0, 'end')

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar la mesa: {e}")

            messagebox.showerror("Error", f"Ocurrió un error al registrar la mesa: {e}")

    def salir(self):
        self.ventanaCliente.destroy()