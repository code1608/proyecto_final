import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Entry, Button, PhotoImage
from model.ConexionDB import Conexion
from collections import Counter


class CalcularPrecioTotal():
    def __init__(self):
        self.ventanaCliente = tk.Toplevel()
        self.ventanaCliente.config(width="500", height="500")
        self.ventanaCliente.resizable(0,0)
        self.ventanaCliente.title("Precio Total")
        
        #Titulo principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Precio Total", font=("Arial", 15))
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
        
        #Cedula caja de texto
        self.txtCedula_cliente = Entry(self.ventanaCliente, state="disabled")
        self.txtCedula_cliente.place(x=230, y=150, width=200, height=25)
        
        #Mesa texto
        self.lblMesa= Label(self.ventanaCliente, text="N° Mesa*", font=("Arial", 15))
        self.lblMesa.place(x=90, y=200)
        
        #Mesa caja de texto
        self.txtMesa = Entry(self.ventanaCliente, state="disabled")
        self.txtMesa.place(x=230, y=200, width=200, height=25)
        
        
        #Platos texto
        self.lblPlatos= Label(self.ventanaCliente, text="Platos*", font=("Arial", 15))
        self.lblPlatos.place(x=90, y=250)
        
        #Platos texto
        self.txtPlatos = Entry(self.ventanaCliente, state="disabled")
        self.txtPlatos.place(x=230, y=250, width=200, height=25)
        
        #Precio Total texto
        self.lblPrecio_total= Label(self.ventanaCliente, text="Precio Total*", font=("Arial", 15))
        self.lblPrecio_total.place(x=90, y=300)
        
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
        img_calcular = PhotoImage(file=r"icons\calcular.png").subsample(16) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(16) 
        
        #Boton Calcular
        self.btnCalcularPrecioTotal = Button(self.ventanaCliente, image = img_calcular, command=self.calcular_precio_total)
        self.btnCalcularPrecioTotal.place(x=140, y=430, height=40, width=110)
        self.btnCalcularPrecioTotal.image = img_calcular
        self.create_tooltip(self.btnCalcularPrecioTotal, "Calcular Precio Total")
        
        #Boton Salir
        self.btnSalir = Button(self.ventanaCliente, image = img_salir, command=self.salir)
        self.btnSalir.place(x=300, y=430, height=40, width=110)
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

    def calcular_precio_total(self):
        id = self.txtId.get()

        if not id:
            messagebox.showerror("Error", "El ID es obligatorio.")
            return

        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Obtener los datos de la comanda
            consulta_comanda = "SELECT cedula_cliente, mesa, platos, precio_total, estado FROM comanda WHERE id = %s"
            cursor.execute(consulta_comanda, (id,))
            comanda = cursor.fetchone()

            if comanda:
                # Llenar campos de la interfaz con los datos obtenidos
                self.txtCedula_cliente.config(state="normal")
                self.txtMesa.config(state="normal")
                self.txtPlatos.config(state="normal")
                self.txtPrecio_total.config(state="normal")
                self.txtEstado.config(state="normal")

                self.txtCedula_cliente.delete(0, 'end')
                self.txtMesa.delete(0, 'end')
                self.txtPlatos.delete(0, 'end')
                self.txtPrecio_total.delete(0, 'end')
                self.txtEstado.delete(0, 'end')

                self.txtCedula_cliente.insert(0, comanda[0])
                self.txtMesa.insert(0, comanda[1])
                self.txtPlatos.insert(0, comanda[2])
                self.txtEstado.insert(0, comanda[4])

                self.txtCedula_cliente.config(state="disabled")
                self.txtMesa.config(state="disabled")
                self.txtPlatos.config(state="disabled")
                self.txtEstado.config(state="disabled")

                platos_ids = comanda[2]  # IDs de los platos, separados por comas, por ejemplo: "1,2,3"

                platos_ids_list = platos_ids.split(",")

                # Contar la frecuencia de cada ID
                frecuencia_platos = Counter(platos_ids_list)

                # Consulta para obtener los datos de los platos desde la base de datos
                consulta_precios_cantidad = f"""
                    SELECT id, precio, cantidad_disponible 
                    FROM plato 
                    WHERE id IN ({','.join(['%s'] * len(frecuencia_platos))})
                """
                cursor.execute(consulta_precios_cantidad, list(frecuencia_platos.keys()))
                platos_data = cursor.fetchall()

                total_precio = 0

                for plato in platos_data:
                    plato_id, precio, cantidad_disponible = plato

                    # Obtener la cantidad solicitada de este plato usando el contador
                    cantidad_solicitada = frecuencia_platos[str(plato_id)]

                    # Verificar si hay suficiente cantidad disponible
                    if cantidad_disponible < cantidad_solicitada:
                        messagebox.showwarning(
                            "Advertencia",
                            f"El plato con ID {plato_id} tiene solo {cantidad_disponible} disponibles, pero se solicitaron {cantidad_solicitada}."
                        )
                        continue

                    # Calcular el costo total para este plato
                    subtotal = precio * cantidad_solicitada
                    total_precio += subtotal

                    # Actualizar la cantidad disponible del plato en la base de datos
                    consulta_actualizar_cantidad = """
                        UPDATE plato 
                        SET cantidad_disponible = cantidad_disponible - %s 
                        WHERE id = %s
                    """
                    cursor.execute(consulta_actualizar_cantidad, (cantidad_solicitada, plato_id))

                # Actualizar el precio total en la tabla comanda
                consulta_actualizar = """
                    UPDATE comanda 
                    SET precio_total = %s 
                    WHERE id = %s
                """
                cursor.execute(consulta_actualizar, (total_precio, id))
                con.commit()

                # Mostrar el precio total en la interfaz
                self.txtPrecio_total.insert(0, f"{total_precio:.2f}")
                self.txtPrecio_total.config(state="disabled")

                messagebox.showinfo("Éxito", f"Precio total calculado: {total_precio}\nCantidades disponibles actualizadas.")
            else:
                messagebox.showerror("Error", f"No se encontró una comanda con ID: {id}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al calcular el precio total: {e}")
        finally:
            mi_conexion.cerrarConexion()

    # Función para salir
    def salir(self):
        self.ventanaCliente.destroy()

