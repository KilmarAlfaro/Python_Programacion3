

"""
Este programa hace uso del combo box y el spin box, hace que el usuario ingrese que tan fanatico del anime se considera y dependiendo su eleccion de datos les mostrara un mensaje 
diciendo si va por buen camino, o si esta seleccionando un nivel de fanatismo mayor al que deberia, esto obviamente es a especie de broma respecto a los animes pero usando este 
mismo formato podria adaptarse a un entorno mas serio como lo puede ser ingresar el nivel de un ingeniero y cuantos años de experiencia posee.
"""




from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QFormLayout, QLabel, QComboBox, QSpinBox)
import sys





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 400, 300)
        self.setWindowTitle("Catador de Animes")

        # Crea el combo box para seleccionar nivel de fanatico del anime
        self.nivel_experiencia = QComboBox()
        self.nivel_experiencia.addItems(["Principiante", "Intermedio", "Avanzado"])

        # Crea el spin box para ingresar cuántos animes ha visto
        self.animes_vistos = QSpinBox()
        self.animes_vistos.setRange(0, 50) 

        # Crea un labwl para mostrar el resultado
        self.resultado = QLabel()

        # Botón para capturar los datos
        boton = QPushButton("Guardar datos")
        boton.clicked.connect(self.boton_click)

        # Crea el layout del formulario
        layout = QFormLayout()
        central = QWidget()

        # Añadir los widgets al formulario
        layout.addRow("¿Qué tan fanático del anime te consideras?", self.nivel_experiencia)
        layout.addRow("¿Cuántos animes has visto?", self.animes_vistos)

        # Añade el botón y el label para los resultados
        layout.addRow(boton)
        layout.addRow(self.resultado)

    
        central.setLayout(layout)
        self.setCentralWidget(central)

    def boton_click(self):
        # Lee los datos del combo box y del spin box
        nivel = self.nivel_experiencia.currentText()
        animes_vistos = self.animes_vistos.value()

        # Definir las condiciones según el nivel y el número de animes vistos
        if nivel == "Avanzado" and animes_vistos < 20:
            mensaje = f"falso! Para ser considerado un fan avanzado necesitas haber visto un minimo de 20 animes. Tú solo has visto  {animes_vistos}."
        if nivel == "Avanzado" and animes_vistos >= 20:
            mensaje = f"Un grande, llevas {animes_vistos} animes vistos, tienes mi respetos."
        

        elif nivel == "Intermedio" and animes_vistos < 10:
            mensaje = f"falso! Para ser considerado un fan intermedio necesitas haber visto un minimo de 10 animes. Tú solo has visto {animes_vistos}."

        if nivel == "Intermedio" and animes_vistos >= 10:
            mensaje = f"Genial, llevas {animes_vistos} animes vistos, vas por buen camino hacia la grandeza."


        
        elif nivel == "Principiante" and animes_vistos >= 20:
            mensaje = f"llevas {animes_vistos} animes vistos, ya puedes considerarte un fanatico avanazado!"


        elif nivel == "Principiante" and animes_vistos > 9:
            mensaje = f"llevas {animes_vistos} animes vistos, ya puedes considerarte un fanatico intermedio!"
        

        elif nivel == "Principiante" and animes_vistos > 0:
            mensaje = f"felicidades por escoger este camino, con un par de animes vistos mas y tu nivel sera mas alto, sigue asi! (llevas {animes_vistos} animes vistos)."


        elif nivel == "Principiante" and animes_vistos <= 0:
            mensaje = f"Muy mal, como es posible que no hayas visto ningun anime :("

        
       
     

        # Mostrar el resultado en el QLabel
        self.resultado.setText(mensaje)

# Configuración básica de la aplicación
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec_()

