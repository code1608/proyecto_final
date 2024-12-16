import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from model.ConexionDB import Conexion


class TomarComanda():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="500")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Tomar Comanda")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Tomar Comanda", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        #ID texto
        self.lblId = Label(self.ventanaCliente, text="ID*", font=("Arial", 15))
        self.lblId.place(x=90, y=100)
        
        # Validación para números, espacios y caja de texto
        validate_Id = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtId = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_Id, '%P'))
        self.txtId.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtId, "Solo se permiten números")
        
        #Cedula Cliente texto
        self.lblCedula_cliente = Label(self.ventanaCliente, text="Cédula Cliente*", font=("Arial", 15))
        self.lblCedula_cliente.place(x=90, y=150)
        
        # Validación para números, puntos "." y espacios y caja de texto
        validate_cedula = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c in ". " for c in texto))
        self.txtCedula_cliente = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_cedula, '%P'))
        self.txtCedula_cliente.place(x=230, y=150, width=200, height=25)
        self.create_tooltip(self.txtCedula_cliente, "Solo se permiten números y puntos")
        
        #Mesa texto
        self.lblMesa = Label(self.ventanaCliente, text="N° Mesa*", font=("Arial", 15))
        self.lblMesa .place(x=90, y=200)
        
        # Validación para números, espacios y caja de texto
        validate_mesa = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtMesa = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_mesa, '%P'))
        self.txtMesa.place(x=230, y=200, width=200, height=25)
        self.create_tooltip(self.txtMesa, "Solo se permiten números")
        
        #Platos Total texto
        self.lblPlatos = Label(self.ventanaCliente, text="Platos*", font=("Arial", 15))
        self.lblPlatos .place(x=90, y=250)
        
        #Platos caja de texto
        self.txtPlatos = Entry(self.ventanaCliente, state="disabled")
        self.txtPlatos.place(x=230, y=250, width=200, height=25)
        
        #Precio Total texto
        self.lblPrecio_total = Label(self.ventanaCliente, text="Precio Total*", font=("Arial", 15))
        self.lblPrecio_total .place(x=90, y=300)
        
        #Precio Total caja de texto
        self.txtPrecio_total = Entry(self.ventanaCliente, state="disabled")
        self.txtPrecio_total.place(x=230, y=300, width=200, height=25)
        
        #Estado texto
        self.lblEstado= Label(self.ventanaCliente, text="Estado*", font=("Arial", 15))
        self.lblEstado.place(x=90, y=350)
        
        #Estado caja de texto
        self.txtEstado = Entry(self.ventanaCliente, state="disabled")
        self.txtEstado.place(x=230, y=350, width=200, height=25)

        #Iconos
        img_comanda = PhotoImage(file=r"icons\guardar-datos.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 
        
        #Boton Tomar Comanda
        self.btnComanda = Button(self.ventanaCliente, image = img_comanda, command=self.registrar_comanda)
        self.btnComanda.place(x=180, y=430, height=40, width=150)
        self.btnComanda.image = img_comanda
        self.create_tooltip(self.btnComanda, "Tomar comanda")
        
        #Boton Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir, command=self.salir)
        self.btnSalir.place(x=350, y=430, height=40, width=110)
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

    #funcion para registrar comanda
    def registrar_comanda(self):
        id = self.txtId.get()
        cedula_cliente = self.txtCedula_cliente.get()
        mesa = self.txtMesa.get()
        estado = "Pendiente"  

        if not id or not cedula_cliente or not mesa:
            messagebox.showerror("Error", "Todos los campos marcados con * son obligatorios.")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Inserta una nueva comanda en la tabla correspondiente
            consulta = "INSERT INTO comanda (id, cedula_cliente, mesa) VALUES (%s, %s, %s)"
            cursor.execute(consulta, (id, cedula_cliente, mesa))
            con.commit()

            self.txtEstado.config(state="normal")
            self.txtEstado.delete(0, tk.END)
            self.txtEstado.insert(0, estado)
            self.txtEstado.config(state="disabled")

            messagebox.showinfo("Éxito", "Comanda registrada con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al tomar la comanda: {e}")
        finally:
            mi_conexion.cerrarConexion()

        
    # Función para salir
    def salir(self):
        self.ventanaCliente.destroy()