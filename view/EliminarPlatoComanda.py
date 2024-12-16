import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from model.ConexionDB import Conexion

class EliminarPlatoComanda():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="500")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Eliminar Plato Comanda")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Eliminar Plato Comanda", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        #ID texto
        self.lblId = Label(self.ventanaCliente, text="ID*", font=("Arial", 15))
        self.lblId.place(x=90, y=100)
        
        # Validación para números, espacios y caja de texto
        validate_id = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtId = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_id, '%P'))
        self.txtId.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtId, "Solo se permiten números")
        
        #Cedula Cliente texto
        self.lblCedula_cliente = Label(self.ventanaCliente, text="Cédula Cliente*", font=("Arial", 15))
        self.lblCedula_cliente.place(x=90, y=150)
        
        #Cedula Cliente caja de texto
        self.txtCedula_cliente = Entry(self.ventanaCliente, state="disabled")
        self.txtCedula_cliente.place(x=230, y=150, width=200, height=25)
        
        #N°Mesa texto
        self.lblMesa= Label(self.ventanaCliente, text="N° Mesa*", font=("Arial", 15))
        self.lblMesa.place(x=90, y=200)
        
        #N°Mesa caja de texto
        self.txtMesa = Entry(self.ventanaCliente, state="disabled")
        self.txtMesa.place(x=230, y=200, width=200, height=25)
        
        #Platos texto
        self.lblPlatos = Label(self.ventanaCliente, text="Platos*", font=("Arial", 15))
        self.lblPlatos.place(x=90, y=250)
        
        # Validación para números, guiones y comas "-", espacios y caja de texto
        validate_platos = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c in "-, " for c in texto))
        self.txtPlatos = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_platos, '%P'))
        self.txtPlatos.place(x=230, y=250, width=200, height=25)
        self.create_tooltip(self.txtPlatos, "Solo se permiten números guiones y comas")
        
        #Precio Total texto
        self.lblPrecio_total = Label(self.ventanaCliente, text="Precio Total*", font=("Arial", 15))
        self.lblPrecio_total.place(x=90, y=300)
        
        #Precio Total caja de texto
        self.txtPrecio_total = Entry(self.ventanaCliente, state="disabled")
        self.txtPrecio_total.place(x=230, y=300, width=200, height=25)
        
        #Estado texto
        self.lblEstado= Label(self.ventanaCliente, text="Pendiente*", font=("Arial", 15))
        self.lblEstado.place(x=90, y=350)
        
        #Estado caja de texto
        self.txtEstado = Entry(self.ventanaCliente, state="disabled")
        self.txtEstado.place(x=230, y=350, width=200, height=25)

        #Iconos
        img_buscar = PhotoImage(file=r"icons\buscar.png").subsample(16) 
        img_eliminar_plato = PhotoImage(file=r"icons\cuchilleria.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 
        
        #Boton Buscar
        self.btnBuscar = Button(self.ventanaCliente, image = img_buscar, command=self.buscar_comanda)
        self.btnBuscar.place(x=50, y=430, height=40, width=110)
        self.btnBuscar.image = img_buscar
        self.create_tooltip(self.btnBuscar, "Buscar Comanda")
        
        #Boton Eliminar platos
        self.btnEliminar_plato = Button(self.ventanaCliente, image = img_eliminar_plato, command=self.eliminar_platos)
        self.btnEliminar_plato.place(x=180, y=430, height=40, width=150)
        self.btnEliminar_plato.image = img_eliminar_plato
        self.create_tooltip(self.btnEliminar_plato, "Eliminar Plato")
        
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
        
    def eliminar_platos(self):
        id = self.txtId.get()  # Obtener ID de la comanda

        if not id:
            messagebox.showerror("Error", "El ID es obligatorio.")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Verificar si la comanda existe
            consulta_verificacion = "SELECT * FROM comanda WHERE id = %s"
            cursor.execute(consulta_verificacion, (id,))
            comanda_existente = cursor.fetchone()

            if comanda_existente:
                # Eliminar platos asociados al ID específico
                consulta_eliminar = "UPDATE comanda SET platos = NULL WHERE id = %s AND platos IS NOT NULL"
                cursor.execute(consulta_eliminar, (id,))

                con.commit()
                messagebox.showinfo("Éxito", "Platos eliminados con éxito.")
            else:
                messagebox.showerror("Error", f"No se encontró la comanda con ID: {id}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar los platos: {e}")
        finally:
            mi_conexion.cerrarConexion()

    def buscar_comanda(self):
        id = self.txtId.get()

        if not id:
            messagebox.showerror("Error", "Todos los campos marcados con * son obligatorios.")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Buscar la comanda por id
            consulta_busqueda = "SELECT cedula_cliente, mesa, estado FROM comanda WHERE id = %s"
            cursor.execute(consulta_busqueda, (id,))
            comanda = cursor.fetchone()

            if comanda:
                # Llenar campos correspondientes
                self.txtCedula_cliente.config(state="normal")
                self.txtMesa.config(state="normal")
                self.txtEstado.config(state="normal")

                self.txtCedula_cliente.delete(0, 'end')
                self.txtMesa.delete(0, 'end')
                self.txtEstado.delete(0, 'end')

                # Accediendo correctamente a los campos de la tupla
                self.txtCedula_cliente.insert(0, comanda[0])  # Usando índices
                self.txtMesa.insert(0, comanda[1])
                self.txtEstado.insert(0, comanda[2])

                self.txtCedula_cliente.config(state="disabled")
                self.txtMesa.config(state="disabled")
                self.txtEstado.config(state="disabled")

                messagebox.showinfo("Éxito", f"Comanda encontrada: ID {id}")
            else:
                messagebox.showerror("Error", f"No se encontró la comanda con ID: {id}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar la comanda: {e}")
        finally:
            mi_conexion.cerrarConexion()

    # Función para salir
    def salir(self):
        self.ventanaCliente.destroy()