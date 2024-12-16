import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from model.ConexionDB import Conexion

class ConsultarMesa():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="350")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Consultar Mesa")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Consultar Mesa", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        #ID texto
        self.lblId = Label(self.ventanaCliente, text="ID*", font=("Arial", 15))
        self.lblId.place(x=90, y=100)
        
        # Validación para números, espacios y caja de texto
        validate_id = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtId = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_id, '%P'))
        self.txtId.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtId, "Solo se permiten números")
        
        #Cantidad Comensales texto
        self.lblCantidad_comensales = Label(self.ventanaCliente, text="Cantidad Comensales*", font=("Arial", 15))
        self.lblCantidad_comensales.place(x=20, y=150)
        
        #Cantidad Comensales caja de texto
        self.txtCantidad_comensales = Entry(self.ventanaCliente, state="disabled")
        self.txtCantidad_comensales.place(x=230, y=150, width=200, height=25)
        
        #Estado texto
        self.lblEstado = Label(self.ventanaCliente, text="Estado*", font=("Arial", 15))
        self.lblEstado.place(x=69, y=200)
        
        #Estado caja de texto
        self.txtEstado = Entry(self.ventanaCliente, state="disabled")
        self.txtEstado.place(x=230, y=200, width=200, height=25)

        #Iconos
        img_buscar = PhotoImage(file=r"icons\buscar.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 
    
        #Boton Buscar
        self.btnBuscar = Button(self.ventanaCliente, image = img_buscar, command=self.buscar_mesa)
        self.btnBuscar.place(x=140, y=270, height=40, width=110)
        self.btnBuscar.image = img_buscar
        self.create_tooltip(self.btnBuscar, "Buscar Mesa")
        
        #Boton Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir, command=self.salir)
        self.btnSalir.place(x=300, y=270, height=40, width=110)
        self.btnSalir.image = img_salir
        self.create_tooltip(self.btnSalir, "Salir")

        self.tooltip = None  # Para almacenar el tooltip
        
    def create_tooltip(self, widget, text):
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

    def buscar_mesa(self):
        """Busca una mesa por su id."""
        try:
            id = int(self.txtId.get())  
        except ValueError:
            messagebox.showwarning("Advertencia", "El ID debe ser un número")
            return

        if not id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el id para buscar")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Consulta para buscar una mesa por id
            consulta = "SELECT cantidad_comensales, estado FROM mesa WHERE id = %s"
            cursor.execute(consulta, (id,))
            resultado = cursor.fetchone()

            if resultado:
                # Llenar los campos con los datos encontrados
                self.txtCantidad_comensales.config(state="normal")
                self.txtEstado.config(state="normal")

                self.txtCantidad_comensales.delete(0, 'end')
                self.txtCantidad_comensales.insert(0, resultado[0])  

                self.txtEstado.delete(0, 'end')
                self.txtEstado.insert(0, resultado[1])  

                self.txtCantidad_comensales.config(state="readonly")
                self.txtEstado.config(state="readonly")

            else:
                messagebox.showwarning("Advertencia", "No se encontró uns mesa con el id proporcionado")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar la mesa: {e}")
        finally:
            mi_conexion.cerrarConexion()

    # Función para salir
    def salir(self):
        self.ventanaCliente.destroy()