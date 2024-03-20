import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from window import HOLA

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumHeight(300)
        self.setFixedWidth(300)
        self.setWindowTitle("Layout Vertical")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        boton1 = QPushButton("Ingresar Datos de usuario")
        boton2 = QPushButton("Gráfica Ejemplo")
        boton3 = QPushButton("Lectura de Datos")
        boton4 = QPushButton("Cerrar")

        boton1.clicked.connect(self.open_user_info)
        boton2.clicked.connect(self.open_grafica)
        boton3.clicked.connect(self.open_lectura)
        boton4.clicked.connect(self.close)  

        layout = QVBoxLayout()
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        layout.addWidget(boton4)

        self.setLayout(layout)

    def imprimir_nombre_boton(self):
        boton = self.sender()
        QMessageBox.information(
            self,
            'Boton press',
            f'Se oprimió el boton {boton.text()}',
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Ok
        )

    def open_second_window(self):
        self.close()  
        self.main_window = HOLA()
        self.main_window.show()

    def open_user_info(self):
        from login import userInfo
        self.close()
        self.user_info = userInfo()
        self.user_info.show()

    def open_grafica(self):
        from grafica import ejemploGrafica
        self.close()  
        self.user_plot = ejemploGrafica()
        self.user_plot.show()

    def open_lectura(self):
        from lectura_serial import lecturaPuerto 
        self.close()  
        self.user_plot = lecturaPuerto()
        self.user_plot.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
