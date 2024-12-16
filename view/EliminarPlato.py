import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from model.ConexionDB import Conexion
from controller.Funciones import eliminar_plato


class EliminarPlato():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="500")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Eliminar Plato")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Eliminar Plato", font=("Arial", 15))
        self.lblTituloPrincipal.place(x=180, y=30)
        
        #ID texto
        self.lblId = Label(self.ventanaCliente, text="ID*", font=("Arial", 15))
        self.lblId.place(x=90, y=100)
        
        # Validación para números, espacios y caja de texto
        validate_Id = self.ventanaCliente.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.txtId = Entry(self.ventanaCliente, validate="key", validatecommand=(validate_Id, '%P'))
        self.txtId.place(x=230, y=100, width=200, height=25)
        self.create_tooltip(self.txtId, "Solo se permiten números")
        
        #Nombre texto
        self.lblNombre = Label(self.ventanaCliente, text="Nombre*", font=("Arial", 15))
        self.lblNombre.place(x=90, y=150)
        
        #Nombre caja de texto
        self.txtNombre = Entry(self.ventanaCliente, state="disabled")
        self.txtNombre.place(x=230, y=150, width=200, height=25)
        
        #Precio texto
        self.lblPrecio = Label(self.ventanaCliente, text="Precio*", font=("Arial", 15))
        self.lblPrecio.place(x=90, y=200)
        
        #Precio caja de texto
        self.txtPrecio = Entry(self.ventanaCliente, state="disabled")
        self.txtPrecio.place(x=230, y=200, width=200, height=25)
        
        #Cantidad Disponible texto
        self.lblCantidad_disponible = Label(self.ventanaCliente, text="Cantidad Disponible*", font=("Arial", 15))
        self.lblCantidad_disponible.place(x=40, y=250)
        
        #Cantidad Disponible caja de texto
        self.txtCantidad_disponible = Entry(self.ventanaCliente, state="disabled")
        self.txtCantidad_disponible.place(x=230, y=250, width=200, height=25)
        
        #Descripcion texto
        self.lblDescripcion = Label(self.ventanaCliente, text="Descripcion*", font=("Arial", 15))
        self.lblDescripcion.place(x=90, y=300)
        
        #Descripcion caja de texto
        self.txtDescripcion = Entry(self.ventanaCliente, state="disabled")
        self.txtDescripcion.place(x=230, y=300, width=200, height=100)

        #Iconos
        img_buscar = PhotoImage(file=r"icons\buscar.png").subsample(16) 
        img_guardar = PhotoImage(file=r"icons\guardar-datos.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 
        
        #Boton Buscar
        self.btnBuscar = Button(self.ventanaCliente, image = img_buscar, command=self.buscar_plato)
        self.btnBuscar.place(x=50, y=415, height=40, width=110)
        self.btnBuscar.image = img_buscar
        self.create_tooltip(self.btnBuscar, "Buscar Plato")
        
        #Boton Guardar
        self.btnGuardar = Button(self.ventanaCliente, image = img_guardar, command=self.eliminar_plato)
        self.btnGuardar.place(x=180, y=415, height=40, width=110)
        self.btnGuardar.image = img_guardar
        self.create_tooltip(self.btnGuardar, "Eliminar Plato")
        
        #Boton Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir,command=self.salir)
        self.btnSalir.place(x=310, y=415, height=40, width=110)
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
        
    # Función para buscar y eliminar un plato
    def eliminar_plato(self):
        id = self.txtId.get()
        nombre = self.txtNombre.get()
        precio = self.txtPrecio.get()
        cantidad_disponible = self.txtCantidad_disponible.get()
        descripcion = self.txtDescripcion.get()

        if not id and not nombre and not precio and not cantidad_disponible and not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, ingrese al menos un dato para buscar")
            return

        try:
            # Llama a la función eliminar_palto con los datos
            eliminar_plato(id, nombre, precio, cantidad_disponible, descripcion)
            messagebox.showinfo("Éxito", "Plato eliminado con éxito")

            # Limpiar campos
            self.txtId.delete(0, 'end')
            self.txtNombre.delete(0, 'end')
            self.txtPrecio.delete(0, 'end')
            self.txtCantidad_disponible.delete(0, 'end')
            self.txtDescripcion.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar/eliminar el plato: {e}")

    #funcion para buscar el plato
    def buscar_plato(self):
        """Busca un plato por Id."""
        id = self.txtId.get()

        if not id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el ID para buscar")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Consulta para buscar un plato por Id
            consulta = "SELECT nombre, precio, cantidad_disponible, descripcion FROM plato WHERE id = %s"
            cursor.execute(consulta, (id,))
            resultado = cursor.fetchone()

            if resultado:
                # Llenar los campos con los datos encontrados y habilitarlos
                self.txtNombre.config(state="normal")
                self.txtPrecio.config(state="normal")
                self.txtCantidad_disponible.config(state="normal")
                self.txtDescripcion.config(state="normal")

                self.txtNombre.delete(0, 'end')
                self.txtNombre.insert(0, resultado[0])

                self.txtPrecio.delete(0, 'end')
                self.txtPrecio.insert(0, resultado[1])

                self.txtCantidad_disponible.delete(0, 'end')
                self.txtCantidad_disponible.insert(0, resultado[2])

                self.txtDescripcion.delete(0, 'end')
                self.txtDescripcion.insert(0, resultado[3])

                self.txtNombre.config(state="readonly")
                self.txtPrecio.config(state="readonly")
                self.txtCantidad_disponible.config(state="readonly")
                self.txtDescripcion.config(state="readonly")
            else:
                messagebox.showwarning("Advertencia", "No se encontró un plato con el id proporcionado")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el plato: {e}")
        finally:
            mi_conexion.cerrarConexion()

    # Función para salir
    def salir(self):
        self.ventanaCliente.destroy()