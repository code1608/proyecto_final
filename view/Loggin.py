import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Entry, Button, Frame, PhotoImage
from controller.User import User

class Loggin():
    def iniciar_sesion(self):
        nombre_user = self.entUser.get()  
        password = self.entContraseña.get()  
        
        if not nombre_user or not password:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        admin = User()
        admin.iniciar_sesion(self.entUser.get(), self.entContraseña.get(), self.ventana)
    
    def mostrar_ayuda(self, event):
        ayuda = "Para iniciar sesión:\n- Ingrese su nombre de usuario.\n- Ingrese su contraseña.\n- Presione 'Enter' o haga clic en 'Login'.\n\nPara salir:\n- Puede cerrar la ventana o usar 'Esc' Para salir del todo.\n- Para volver a ver la ayuda precio 'Alt-a' o click Izquierdo\n- para cerrar ayuda use 'Esc'"
        messagebox.showinfo("Ayuda", ayuda)

    def cerrar_ventana(self, event=None):
        self.ventana.destroy()

    def create_tooltip(self, widget, text):
        """Crear un tooltip simple para un widget."""
        tooltip = Label(self.ventana, text=text, background="#aed6f1", borderwidth=1, relief="solid", font=("Arial", 10))
        tooltip.place_forget()  # Oculta el tooltip inicialmente

        def show_tooltip(event):
            tooltip.update_idletasks()  
            x = widget.winfo_x() + (widget.winfo_width() // 2) - (tooltip.winfo_width() // 2)
            y = widget.winfo_y() - tooltip.winfo_height() - 5
            
            x = max(0, min(x, self.ventana.winfo_width() - tooltip.winfo_width()))
            y = max(0, y)
            tooltip.place(x=x, y=y)

        def hide_tooltip(event):
            tooltip.place_forget()

        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x420") 
        self.ventana.resizable(False, False) 
        self.ventana.title("Loggin")
        self.ventana.configure(background="#003161")
        
        self.lblTitulo = Label(self.ventana, text="Login Form", font=("Cascadia Code Bold", 23), fg="#7ED4AD", bg="#003161")
        self.lblTitulo.place(x=110, y=30)

        # Cargar imágenes para "User" y "Password"
        img_user = PhotoImage(file=r"icons\usuario.png").subsample(15) 
        img_password = PhotoImage(file=r"icons\encerrar.png").subsample(1) 

        # Sustituir etiquetas de texto por imágenes
        self.lblUser = Label(self.ventana, image=img_user, bg="#003161")
        self.lblUser.image = img_user 
        self.lblUser.place(x=183, y=105)

        validate_user = self.ventana.register(lambda texto: all(c.isalpha() or c in " áéíóúÁÉÍÓÚñÑ" for c in texto))
        self.entUser = Entry(self.ventana, font="Arial", justify="center", highlightbackground="red", highlightthickness=3, validate="key", validatecommand=(validate_user, '%P'))
        self.entUser.place(x=110, y=150, width=180, height=25)

        self.lblContraseña = Label(self.ventana, image=img_password, bg="#003161")
        self.lblContraseña.image = img_password  
        self.lblContraseña.place(x=183, y=195)

        validate_contraseña = self.ventana.register(lambda texto: all(c.isdigit() or c == " " for c in texto))
        self.entContraseña = Entry(self.ventana, font="Arial", justify="center", show="*", highlightbackground="red", highlightthickness=3,validate="key", validatecommand=(validate_contraseña, '%P'))  
        self.entContraseña.place(x=110, y=240, width=180, height=25)

        # Cargar imágenes para los botones
        img_login = PhotoImage(file=r"icons\entrar.png").subsample(8)  
        img_ayuda = PhotoImage(file=r"icons\ayudar.png").subsample(16)  

        #Botones
        self.btnLogin = Button(self.ventana, image=img_login, border=0, command=self.iniciar_sesion, bg="#003161")
        self.btnLogin.image = img_login  # Guardar referencia a la imagen
        self.btnLogin.place(x=160, y=315)

        self.btnAyuda = Button(self.ventana, image=img_ayuda, border=0, command=self.mostrar_ayuda, bg="#003161")
        self.btnAyuda.image = img_ayuda  # Guardar referencia a la imagen
        self.btnAyuda.place(x=360, y=10)

        # Crear tooltips para los iconos
        self.create_tooltip(self.lblUser, "Usuario")
        self.create_tooltip(self.lblContraseña, "Contraseña")
        self.create_tooltip(self.btnAyuda, "Ayuda\n'Alt-a' para abrir")

        # Evento de enter
        self.entContraseña.bind('<Return>', lambda event: self.iniciar_sesion())
        self.btnLogin.bind('<Return>', lambda event: self.iniciar_sesion())
        self.entUser.bind('<Return>', lambda event: self.iniciar_sesion())
        self.ventana.bind('<Escape>', self.cerrar_ventana)
        self.ventana.bind('<Alt-a>', self.mostrar_ayuda)
        self.btnAyuda.bind('<Button-1>', self.mostrar_ayuda)

        self.ventana.mainloop()