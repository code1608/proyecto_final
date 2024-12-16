from tkinter import *
from tkinter import messagebox
from model.ConexionDB import Conexion
from datetime import datetime
from tkinter import Label, Button, PhotoImage

class GenerarInforme:
    def __init__(self):
        self.ventanaCliente = Toplevel()
        self.ventanaCliente.title("Generar Informe")
        self.ventanaCliente.geometry("500x450")
        self.ventanaCliente.resizable(0, 0)

        # Título principal
        self.lblTituloPrincipal = Label(self.ventanaCliente, text="Registrar Datos del Día", font=("Arial", 15, "bold"))
        self.lblTituloPrincipal.pack(pady=20)

        # Contenedor para los datos
        frame_datos = Frame(self.ventanaCliente)
        frame_datos.pack(pady=20)

        # ID
        self.lblID = Label(frame_datos, text="ID:", font=("Arial", 15), anchor="w", width=20)
        self.lblID.grid(row=0, column=0, padx=10, pady=5)
        self.lblIDValor = Label(frame_datos, text="Pendiente", font=("Arial", 15), fg="blue", anchor="w")
        self.lblIDValor.grid(row=0, column=1, padx=10, pady=5)

        # Fecha
        self.lblFecha = Label(frame_datos, text="Fecha:", font=("Arial", 15), anchor="w", width=20)
        self.lblFecha.grid(row=1, column=0, padx=10, pady=5)
        self.lblFechaValor = Label(frame_datos, text="Pendiente", font=("Arial", 15), fg="blue", anchor="w")
        self.lblFechaValor.grid(row=1, column=1, padx=10, pady=5)

        # Cantidad de Comandas
        self.lblCantidadComandas = Label(frame_datos, text="Cantidad Comandas:", font=("Arial", 15), anchor="w", width=20)
        self.lblCantidadComandas.grid(row=2, column=0, padx=10, pady=5)
        self.lblCantidadComandasValor = Label(frame_datos, text="Pendiente", font=("Arial", 15), fg="blue", anchor="w")
        self.lblCantidadComandasValor.grid(row=2, column=1, padx=10, pady=5)

        # Total Ganancias Día
        self.lblTotalGananciasDia = Label(frame_datos, text="Total Ganancias Día:", font=("Arial", 15), anchor="w", width=20)
        self.lblTotalGananciasDia.grid(row=3, column=0, padx=10, pady=5)
        self.lblTotalGananciasDiaValor = Label(frame_datos, text="Pendiente", font=("Arial", 15), fg="blue", anchor="w")
        self.lblTotalGananciasDiaValor.grid(row=3, column=1, padx=10, pady=5)

        # Promedio Ganancias Día
        self.lblPromedioGananciasDia = Label(frame_datos, text="Promedio Ganancias Día:", font=("Arial", 15), anchor="w", width=20)
        self.lblPromedioGananciasDia.grid(row=4, column=0, padx=10, pady=5)
        self.lblPromedioGananciasDiaValor = Label(frame_datos, text="Pendiente", font=("Arial", 15), fg="blue", anchor="w")
        self.lblPromedioGananciasDiaValor.grid(row=4, column=1, padx=10, pady=5)

        # Contenedor para los botones
        frame_botones = Frame(self.ventanaCliente)
        frame_botones.pack(pady=20)

        #Iconos
        img_informe = PhotoImage(file=r"icons\infome.png").subsample(10) 
        img_salir = PhotoImage(file=r"icons\salida.png").subsample(10)

        # Botón Generar Informe
        self.btnGenerarInforme = Button(frame_botones, image = img_informe, command=self.generar_informe)
        self.btnGenerarInforme.grid(row=0, column=0, padx=30, pady=30)
        self.btnGenerarInforme.image = img_informe
        self.create_tooltip(self.btnGenerarInforme, "Generar Informe")

        # Botón Salir
        self.btnSalir = Button(frame_botones, image = img_salir, command=self.salir)
        self.btnSalir.grid(row=0, column=1, padx=30, pady=30)
        self.btnSalir.image = img_salir
        self.create_tooltip(self.btnSalir, "Salir")

        self.tooltip = None  # Para almacenar el tooltip
        
    def create_tooltip(self, widget, text):
        """Crea un tooltip que aparece encima del widget al pasar el cursor."""
        tooltip = Label(self.ventanaCliente, text=text, background="#aed6f1", borderwidth=1, 
                        relief="solid", font=("Arial", 10))
        tooltip.place_forget()  # Oculta inicialmente el tooltip

        def show_tooltip(event):
            # Calcula las coordenadas para posicionar el tooltip arriba del widget
            x = widget.winfo_rootx() + (widget.winfo_width() // 2) - (tooltip.winfo_reqwidth() // 2)
            y = widget.winfo_rooty() - tooltip.winfo_reqheight() - 5
            tooltip.place(x=x, y=y)  # Muestra el tooltip

        def hide_tooltip(event):
            tooltip.place_forget()  # Oculta el tooltip

        # Enlaza eventos para mostrar y ocultar el tooltip
        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)

    #funcion para generar el informe con la base de datos
    def generar_informe(self):
        mi_conexion = Conexion()
        try:
            mi_conexion.conectar()
            con = mi_conexion.getConectar()
            cursor = con.cursor()

            # Calcular la fecha actual
            fecha_actual = datetime.now().date()

            # Contar la cantidad de comandas
            consulta_cantidad_comandas = "SELECT COUNT(id) FROM comanda"
            cursor.execute(consulta_cantidad_comandas)
            cantidad_comandas = cursor.fetchone()[0]

            # Calcular el total de ganancias
            consulta_total_ganancias = "SELECT SUM(precio_total) FROM comanda"
            cursor.execute(consulta_total_ganancias)
            total_ganancias = cursor.fetchone()[0] or 0

            # Calcular el promedio de ganancias
            promedio_ganancias = total_ganancias / cantidad_comandas if cantidad_comandas > 0 else 0

            # Insertar los datos en la tabla informeDiario
            consulta_insertar_informe = """
                INSERT INTO informeDiario (fecha, cantidad_comandas, total_ganancias_dia, promedio_ganancias_dia)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(consulta_insertar_informe, (fecha_actual, cantidad_comandas, total_ganancias, promedio_ganancias))

            # Obtener el ID generado automáticamente
            informe_id = cursor.lastrowid

            con.commit()

            # Mostrar datos en la interfaz
            self.lblIDValor.config(text=str(informe_id))  # Mostrar el ID en la interfaz
            self.lblFechaValor.config(text=str(fecha_actual))
            self.lblCantidadComandasValor.config(text=str(cantidad_comandas))
            self.lblTotalGananciasDiaValor.config(text=f"${total_ganancias:.2f}")
            self.lblPromedioGananciasDiaValor.config(text=f"${promedio_ganancias:.2f}")

            messagebox.showinfo("Éxito", "Informe generado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el informe: {e}")
        finally:
            mi_conexion.cerrarConexion()


    def salir(self):
        self.ventanaCliente.destroy()

