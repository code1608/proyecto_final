import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view.RegistrarChef import RegistrarChef
from view.EliminarChef import EliminarChef
from view.RegistrarMesero import RegistrarMesero
from view.EliminarMesero import EliminarMesero
from view.AgregarMesa import AgregarMesa
from view.EliminarMesa import EliminarMesa
from view.CalcularPrecioTotal import CalcularPrecioTotal
from view.GenerarInforme import GenerarInforme


class MenuCajero():
    def __init__(self, loggin, admi):
        self.ventana_menu = tk.Toplevel(loggin)
        self.ventana_menu.config(width=400, height=400)
        self.ventana_menu.title("Menú Cajero")
        self.ventana_menu.resizable(0, 0)

        self.admi = admi
        self.app = None

        # Crear un Frame para el menú vertical
        menu_frame = tk.Frame(self.ventana_menu, bg="black", padx=10, pady=10)
        menu_frame.pack(fill=tk.Y, side=tk.LEFT)

        # Diccionario con las opciones del submenú
        self.opciones_menu = {
            "Gestionar Chef": ["Añadir Chef", "Eliminar Chef"],
            "Gestionar Meseros": ["Añadir Mesero", "Eliminar Mesero"],
            "Gestionar Mesas": ["Añadir Mesa", "Eliminar Mesa"],
            "Gestionar Comandas": ["Calcular Precio Total", "Generar Informe Diario"],
            "Salir": []
        }

        # Crear botones principales con submenús
        for texto in self.opciones_menu:
            btn = tk.Button(
                menu_frame,
                text=texto,
                pady=10,
                width=20,
                command=lambda t=texto: self.mostrar_submenu(t),
                font=("Cascadia Code Bold", 15),
                fg="#7ED4AD",
                bg="#003161"
            )
            btn.pack(pady=5)

    def mostrar_submenu(self, opcion):
        # Verificar si la ventana aún existe antes de mostrar el submenú
        if not self.ventana_menu.winfo_exists():
            return  # No hacer nada si la ventana ha sido destruida

        # Crear un submenú flotante (Menu contextual)
        submenu = tk.Menu(self.ventana_menu, tearoff=0)

        if self.opciones_menu[opcion]:
            for sub_opcion in self.opciones_menu[opcion]:
                submenu.add_command(
                    label=sub_opcion,
                    command=lambda o=sub_opcion: self.ejecutar_accion(o)
                )
        else:
            if opcion == "Salir":
                self.salir()

        # Mostrar el submenú en la posición del cursor
        try:
            submenu.post(self.ventana_menu.winfo_pointerx(), self.ventana_menu.winfo_pointery())
        except tk.TclError:
            pass  # Ignorar errores si la ventana fue destruida antes de mostrar el menú

    def ejecutar_accion(self, opcion):
        if opcion == "Añadir Chef":
            self.app = RegistrarChef()
            
        elif opcion == "Eliminar Chef":
            self.app = EliminarChef()
            
        elif opcion == "Añadir Mesero":
            self.app = RegistrarMesero()
            
        elif opcion == "Eliminar Mesero":
            self.app = EliminarMesero()
            
        elif opcion == "Añadir Mesa":
            self.app = AgregarMesa()
            
        elif opcion == "Eliminar Mesa":
            self.app = EliminarMesa()
            
        elif opcion == "Calcular Precio Total":
            self.app == CalcularPrecioTotal()

        elif opcion == "Generar Informe Diario":
            self.app = GenerarInforme()
    
        else:
            messagebox.showinfo("Opción seleccionada", f"Has seleccionado: {opcion}")

    """def mostrar_formulario_chef(self):
        # Crear una nueva ventana para el formulario
        ventana_formulario = tk.Toplevel(self.ventana_menu)
        ventana_formulario.title("Añadir Chef")
        ventana_formulario.geometry("300x200")
        ventana_formulario.resizable(0, 0)

        # Etiquetas y entradas para el formulario
        tk.Label(ventana_formulario, text="Nombre del Chef:", font=("Arial", 12)).pack(pady=10)
        entry_nombre = tk.Entry(ventana_formulario, width=30)
        entry_nombre.pack(pady=5)

        tk.Label(ventana_formulario, text="Especialidad:", font=("Arial", 12)).pack(pady=10)
        entry_especialidad = tk.Entry(ventana_formulario, width=30)
        entry_especialidad.pack(pady=5)

        # Botón para guardar
        tk.Button(ventana_formulario, text="Guardar", command=lambda: self.guardar_chef(entry_nombre.get(), entry_especialidad.get())).pack(pady=10)

    def guardar_chef(self, nombre, especialidad):
        if nombre and especialidad:
            messagebox.showinfo("Guardado", f"Chef {nombre} con especialidad en {especialidad} ha sido añadido.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")"""

    def salir(self):
        self.ventana_menu.destroy()
        
    