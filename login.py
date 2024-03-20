import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from main import MainWindow  # Importa la clase MainWindow desde main.py

class userInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle("Layout Nested")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        mensaje_principal = QLabel('Por favor ingresar sus datos:')
        nombres_label = QLabel('Nombres:')
        nombres_label.setFixedWidth(60)
        self.nombres_input = QLineEdit()
        apellidos_label = QLabel('Apellidos:')
        apellidos_label.setFixedWidth(60)
        self.apellidos_input = QLineEdit()
        edad_label = QLabel('Edad:')
        edad_label.setFixedWidth(60)
        self.edad_input = QLineEdit()
        correo_label = QLabel('Correo:')
        correo_label.setFixedWidth(60)
        self.correo_input = QLineEdit()
        direccion_label = QLabel('Direccion:')
        direccion_label.setFixedWidth(60)
        self.direccion_input = QLineEdit()
        telefono_label = QLabel('Telefono:')
        telefono_label.setFixedWidth(60)
        self.telefono_input = QLineEdit()
        enviar_boton = QPushButton("Enviar")
        regresar_boton = QPushButton("Regresar a la Ventana Principal")  # Botón de regresar

        vertical_layout_main = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()

        h_layout_1.addWidget(nombres_label)
        h_layout_1.addWidget(self.nombres_input)
        h_layout_1.addWidget(correo_label)
        h_layout_1.addWidget(self.correo_input)

        h_layout_2.addWidget(apellidos_label)
        h_layout_2.addWidget(self.apellidos_input)
        h_layout_2.addWidget(direccion_label)
        h_layout_2.addWidget(self.direccion_input)

        h_layout_3.addWidget(edad_label)
        h_layout_3.addWidget(self.edad_input)
        h_layout_3.addWidget(telefono_label)
        h_layout_3.addWidget(self.telefono_input)

        vertical_layout_main.addWidget(mensaje_principal)
        vertical_layout_main.addLayout(h_layout_1)
        vertical_layout_main.addLayout(h_layout_2)
        vertical_layout_main.addLayout(h_layout_3)
        vertical_layout_main.addWidget(enviar_boton)
        vertical_layout_main.addWidget(regresar_boton)  # Agregar el botón de regresar al diseño

        self.setLayout(vertical_layout_main)

        # Conectar el botón de regresar a la función correspondiente
        regresar_boton.clicked.connect(self.regresar_a_ventana_principal)

    def regresar_a_ventana_principal(self):
        self.close()  # Cerrar la ventana actual
        self.ventana_principal = MainWindow()  # Crear una instancia de la ventana principal
        self.ventana_principal.show()  # Mostrar la ventana principal


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = userInfo()
    sys.exit(app.exec())
