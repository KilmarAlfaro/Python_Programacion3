import sys
from PyQt5 import uic

import mysql.connector



from PyQt5.QtWidgets import(QApplication,QMainWindow,QWidget,QLabel,
                            QLineEdit,QFormLayout, QTextEdit,QPushButton,QLayout,QMessageBox)




class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Adm_cuentas.ui", self)
        
        # esto conecta los datos del pyqt5 usando el findChild que primero necesitamos cual es el tipo de QWidget que queremos buscar y el nombre que le hemos puesto en pyqt designer
        self.editUser = self.findChild(QLineEdit, "editUser") 
        self.editContra = self.findChild(QLineEdit, "editContra")  
        self.btnGuardar = self.findChild(QPushButton, "btnGuardar")  
        self.txtUser = self.findChild(QLabel, "txtUser")  
        self.txtContra = self.findChild(QLabel, "txtContra") 
        self.lblServicio = self.findChild(QLabel, "lblServicio")
        self.editServicio = self.findChild(QLineEdit, "editServicio")
        self.txtServicio = self.findChild(QLabel, "txtServicio")
       

        self.editUser.setPlaceholderText("Ingrese un nombre de usuario o gmail")
        self.editContra.setPlaceholderText("Ingrese la contraseña")
        self.editServicio.setPlaceholderText("Ingrese donde utiliza estas credenciales")
        
        self.btnGuardar.clicked.connect(self.guardar_datos)

    def guardar_datos(self):
        
        nombre_usuario = self.editUser.text()
        contraseña = self.editContra.text()
        Servicio = self.editServicio.text()

        if not nombre_usuario or not contraseña or not Servicio:
            
            QMessageBox.warning(self, "Ha ocurrido un error: ","Debe ingresar un nombre de usuario y una contraseña y el servicio.")
            return

        try:
            # la conexion a la base de datos MySQL
            db = mysql.connector.connect(
                user="root",
                password="1234",
                host="localhost",
                database="users"
            )
            cursor = db.cursor()

            
            sql = "INSERT INTO usuarios (Usuario, Contraseña, Servicio) VALUES (%s, %s, %s)"
            values = (nombre_usuario, contraseña, Servicio)

            
            cursor.execute(sql, values)
            db.commit()

            
            self.txtUser.setText(f"Usuario guardado: {nombre_usuario}")
            self.txtContra.setText(f"Contraseña guardada: {contraseña}")
            self.txtServicio.setText(f"Servicio guardado: {Servicio}")

            
            QMessageBox.information(self, "Genial!","Las credenciales han sido almacenadas correctamente en la base de datos.")
        
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ha Ocurrido un error: ", f"Error al conectar con la base de datos: {err}")
        
        finally:
            
            cursor.close()
            db.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ventana = ventana()
    Ventana.show()
    sys.exit(app.exec_())