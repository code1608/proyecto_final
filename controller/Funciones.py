from model.ConexionDB import Conexion
from tkinter import messagebox    

## FUNCIONES PARA TODOS LAS ACCIONES QUE ESTAN EN EL ROL MESERO
#funciones para cliente
def registar_cliente(cedula, nombre, apellido, telefono, email):
    """Registra un nuevo cliente en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Inserta un nuevo cliente en la tabla correspondiente
        consulta = "INSERT INTO cliente (cedula, nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (cedula, nombre, apellido, telefono, email))
        con.commit()

        messagebox.showinfo("Éxito", "Cliente registrado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar el Cliente: {e}")
    finally:
        mi_conexion.cerrarConexion()

def listar_cliente():
    """Lista todos los clientes registrados en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Recupera todos los clientes de la tabla
        consulta = "SELECT * FROM cliente"
        cursor.execute(consulta)
        cliente = cursor.fetchall()

        return cliente
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al listar los clientes: {e}")
        return []
    finally:
        mi_conexion.cerrarConexion()

def eliminar_cliente(cedula, nombre, apellido, telefono, email):
    """Elimina un cliente de la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Elimina un cliente por múltiples campos
        consulta = """
        DELETE FROM cliente
        WHERE cedula = %s OR nombre = %s OR apellido = %s OR telefono = %s OR email = %s
        """
        cursor.execute(consulta, (cedula, nombre, apellido, telefono, email))
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "cliente eliminado con éxito")
        else:
            messagebox.showwarning("Advertencia", "No se encontró un cliente con los datos proporcionados")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al eliminar el cliente: {e}")
    finally:
        mi_conexion.cerrarConexion()



## FUNCIONES PARA TODAS LAS ACCIONES QUE ESTAN EN EL ROL CHEF
#funciones para platos
def registrar_plato(id, nombre, precio, cantidad_diponible, descripcion):
    """Registra un nuevo plato en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Inserta un nuevo chef en la tabla correspondiente
        consulta = "INSERT INTO plato (id, nombre, precio, cantidad_disponible, descripcion) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (id, nombre, precio, cantidad_diponible, descripcion))
        con.commit()

        messagebox.showinfo("Éxito", "Plato registrado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar el plato: {e}")
    finally:
        mi_conexion.cerrarConexion()

def listar_plato():
    """Lista todos los platos registrados en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Recupera todos los platos de la tabla
        consulta = "SELECT * FROM plato"
        cursor.execute(consulta)
        plato = cursor.fetchall()

        return plato
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al listar los platos: {e}")
        return []
    finally:
        mi_conexion.cerrarConexion()

def eliminar_plato(id, nombre, precio, cantidad_disponible, descripcion):
    """Elimina un plato de la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Elimina un plato por múltiples campos
        consulta = """
        DELETE FROM plato
        WHERE id = %s OR nombre = %s OR precio = %s OR cantidad_disponible = %s OR descripcion = %s
        """
        cursor.execute(consulta, (id, nombre, precio, cantidad_disponible, descripcion))
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "plato eliminado con éxito")
        else:
            messagebox.showwarning("Advertencia", "No se encontró un plato con los datos proporcionados")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al eliminar el plato: {e}")
    finally:
        mi_conexion.cerrarConexion()


## FUNCIONES PARA TODAS LAS ACCIONES QUE ESTAN EN EL ROL CAJERO
#funciones para el chef
def registrar_chef(cedula, nombre, apellido, telefono, email):
    """Registra un nuevo chef en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Inserta un nuevo chef en la tabla correspondiente
        consulta = "INSERT INTO chef (cedula, nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (cedula, nombre, apellido, telefono, email))
        con.commit()

        messagebox.showinfo("Éxito", "Chef registrado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar el chef: {e}")
    finally:
        mi_conexion.cerrarConexion()

def listar_chef():
    """Lista todos los chefs registrados en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Recupera todos los chefs de la tabla
        consulta = "SELECT * FROM chef"
        cursor.execute(consulta)
        chefs = cursor.fetchall()

        return chefs
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al listar los chef: {e}")
        return []
    finally:
        mi_conexion.cerrarConexion()

def eliminar_chef(cedula, nombre, apellido, telefono, email):
    """Elimina un chef de la base de datos por cédula, nombre, apellido, teléfono y email."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Elimina un chef por múltiples campos
        consulta = """
        DELETE FROM chef
        WHERE cedula = %s AND nombre = %s AND apellido = %s AND telefono = %s AND email = %s
        """
        cursor.execute(consulta, (cedula, nombre, apellido, telefono, email))
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Chef eliminado con éxito")
        else:
            messagebox.showwarning("Advertencia", "No se encontró un chef con los datos proporcionados")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al eliminar el chef: {e}")
    finally:
        mi_conexion.cerrarConexion()

#funciones para el mesero
def registrar_mesero(cedula, nombre, apellido, telefono, email): 
    """Registra un nuevo mesero en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Inserta un nuevo mesero en la tabla correspondiente
        consulta = "INSERT INTO mesero (cedula, nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (cedula, nombre, apellido, telefono, email))
        con.commit()

        messagebox.showinfo("Éxito", "Mesero registrado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar el mesero: {e}")
    finally:
        mi_conexion.cerrarConexion()

def listar_mesero():
    """Lista todos los meseros registrados en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Recupera todos los meseros de la tabla
        consulta = "SELECT * FROM mesero"
        cursor.execute(consulta)
        meseros = cursor.fetchall()

        return meseros
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al listar los meseros: {e}")
        return []
    finally:
        mi_conexion.cerrarConexion()

def eliminar_mesero(cedula, nombre, apellido, telefono, email):
    """Elimina un mesero de la base de datos por cédula, nombre, apellido, teléfono y email."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Elimina un mesero por múltiples campos
        consulta = """
        DELETE FROM mesero
        WHERE cedula = %s AND nombre = %s AND apellido = %s AND telefono = %s AND email = %s
        """
        cursor.execute(consulta, (cedula, nombre, apellido, telefono, email))
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Mesero eliminado con éxito")
        else:
            messagebox.showwarning("Advertencia", "No se encontró un mesero con los datos proporcionados")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al eliminar el mesero: {e}")
    finally:
        mi_conexion.cerrarConexion()

#funciones para la mesas
def registrar_mesa(id, cantidad_comensales, estado):
    """Registra una nueva mesa en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Inserta una nueva mesa en la tabla
        consulta = "INSERT INTO mesa (id, cantidad_comensales, estado) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (id, cantidad_comensales, estado))
        con.commit()

        messagebox.showinfo("Éxito", "Mesa registrada con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar la mesa: {e}")
    finally:
        mi_conexion.cerrarConexion()

def listar_mesa():
    """Lista todas las mesas registradas en la base de datos."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Recupera todas las mesas de la tabla
        consulta = "SELECT * FROM mesa"
        cursor.execute(consulta)
        mesas = cursor.fetchall()

        return mesas
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al listar las mesas: {e}")
        return []
    finally:
        mi_conexion.cerrarConexion()

def eliminar_mesa(id, cantidad_comensales, estado):
    """Elimina una mesa de la base de datos por ID, cantidad de comensales y estado."""
    mi_conexion = Conexion()
    try:
        mi_conexion.conectar()
        con = mi_conexion.getConectar()
        cursor = con.cursor()

        # Elimina una mesa por ID, cantidad de comensales y estado
        consulta = """
        DELETE FROM mesa
        WHERE id = %s AND cantidad_comensales = %s AND estado = %s
        """
        cursor.execute(consulta, (id, cantidad_comensales, estado))
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Mesa eliminada con éxito")
        else:
            messagebox.showwarning("Advertencia", "No se encontró una mesa con los datos proporcionados")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al eliminar la mesa: {e}")
    finally:
        mi_conexion.cerrarConexion()



