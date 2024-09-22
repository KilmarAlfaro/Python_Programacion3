from PyQt5.QtWidgets import(QApplication,QMainWindow,QWidget,QLabel,
                            QLineEdit,QFormLayout, QTextEdit,QPushButton,QLayout,QMessageBox)

import smtplib


class mainv(QWidget):
    def __init__(self):
        self.setWindowTitle
        layout = QFormLayout()
        self.lbldest = QLabel("Destinatario")
        self.lblasunt = QLabel("Asunto")
        self.lblmesage = QLabel("Mensaje")
        self.editdest = QLineEdit()
        self.editdest.setPlaceholderText("Correo destino")
        self.editasunt = QLineEdit()
        self.editmesage = QTextEdit()
        self.btnenv = QPushButton("Enviar mensaje")
        layout.addRow(self.lbldest,self.editdest)
        layout.addRow(self.lblasunt,self.editasunt)
        layout.addRow(self.lblmesage,self.editmesage)
        self.setLayout(layout)
        self.btnenv.clicked.connect(self.enviar)


app = QApplication(sys.argv)
ventana = mainv


        

    

