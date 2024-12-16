import mysql.connector

class Conexion():
    
    def conectar(self):
        self.conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "admin"
        )   
    
    def cerrarConexion(self):
        if self.conexion:
            self.conexion.close()
            self.conexion = None

            
    def getConectar(self):
        return self.conexion    
      
      
app = Conexion()
app.conectar()
app.cerrarConexion  