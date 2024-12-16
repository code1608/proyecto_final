import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view.AgregarPlato import AgregarPlato
from view.EliminarPlato import EliminarPlato
from view.CambiarEstadoComanda import CambiarEstadoComanda


class MenuChef():
    def __init__(self, loggin, admi):
        self.ventana_menu = tk.Toplevel(loggin)
        self.ventana_menu.config(width=400, height=400)
        self.ventana_menu.title("Menú Chef")
        self.ventana_menu.resizable(0, 0)

        self.admi = admi

        # Crear un Frame para el menú vertical
        menu_frame = tk.Frame(self.ventana_menu, bg="black", padx=10, pady=10)
        menu_frame.pack(fill=tk.Y, side=tk.LEFT)

        # Diccionario con las opciones del submenú
        self.opciones_menu = {
            "Gestionar platos": ["Añadir Plato", "Eliminar Plato"],
            "Gestionar Comandas": ["Cambiar Estado Comanda"],
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
        if opcion == "Añadir Plato":
            self.app = AgregarPlato()
        elif opcion == "Eliminar Plato":
            self.app = EliminarPlato()
        elif opcion == "Cambiar Estado Comanda":
            self.app = CambiarEstadoComanda()
        elif opcion == "Salir":
            self.salir()
        else:
            messagebox.showinfo("Opción seleccionada", f"Has seleccionado: {opcion}")


    def salir(self):
        self.ventana_menu.destroy()