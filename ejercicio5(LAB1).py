# Construir un programa que muestre una ventana a traves de la cual se puedan leer 10 datos caracteristicos de una persona


from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QFormLayout, QLabel)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 600, 400)
        self.setWindowTitle("Datos de una Persona")

        # 
        self.nombre = QLineEdit()
        self.apellido = QLineEdit()
        self.edad = QLineEdit()
        self.genero = QLineEdit()
        self.gustos = QLineEdit()
        self.pasatiempos = QLineEdit()
        self.altura = QLineEdit()
        self.peso = QLineEdit()
        self.pais = QLineEdit()
        self.color_pelo = QLineEdit()

        # label para mostrar el resultado
        self.resultado = QLabel()

        # Botón para capturar los datos
        boton = QPushButton("Guardar datos")
        boton.clicked.connect(self.boton_click)

        # Creacion del layout del formulario
        layout = QFormLayout()
        central = QWidget()

        # los campos del formulario
        layout.addRow("Nombre:", self.nombre)
        layout.addRow("Apellido:", self.apellido)
        layout.addRow("Edad:", self.edad)
        layout.addRow("Género:", self.genero)
        layout.addRow("Gustos:", self.gustos)
        layout.addRow("Pasatiempos:", self.pasatiempos)
        layout.addRow("Altura:", self.altura)
        layout.addRow("Peso:", self.peso)
        layout.addRow("País:", self.pais)
        layout.addRow("Color de pelo:", self.color_pelo)

        # Añadir el botón y el label para los resultados
        layout.addRow(boton)
        layout.addRow(self.resultado)

        # Configurar el layout en la ventana principal
        central.setLayout(layout)
        self.setCentralWidget(central)

    def boton_click(self):
        # Leer los datos de los campos de texto
        datos = {
            "Nombre": self.nombre.text(),
            "Apellido": self.apellido.text(),
            "Edad": self.edad.text(),
            "Género": self.genero.text(),
            "Gustos": self.gustos.text(),
            "Pasatiempos": self.pasatiempos.text(),
            "Altura": self.altura.text(),
            "Peso": self.peso.text(),
            "País": self.pais.text(),
            "Color de pelo": self.color_pelo.text(),
        }

        # Mostrar los datos en el QLabel 
        texto_resultado = "\n".join([f"{clave}: {valor}" for clave, valor in datos.items()])
        self.resultado.setText(texto_resultado)


app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec_()
