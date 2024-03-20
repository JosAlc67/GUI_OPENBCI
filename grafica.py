import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class ejemploGrafica(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ventana con dos QHBox')
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        top_layout = QHBoxLayout(central_widget)

        left_layout = QVBoxLayout()
        for i in range(5):
            button = QPushButton(f'Botón {i+1}')
            left_layout.addWidget(button)

        left_layout.setStretchFactor(left_layout, 1)

        right_layout = QVBoxLayout()

        blank_label = QLabel('Recuadro en blanco')
        right_layout.addWidget(blank_label)

        senoidal_plot = SenoidalPlot()
        right_layout.addWidget(senoidal_plot)
        right_layout.setStretchFactor(senoidal_plot, 1) 

        top_layout.addLayout(left_layout)
        top_layout.addLayout(right_layout)

        bottom_layout = QHBoxLayout()

        for i in range(3):
            button = QPushButton(f'Botón {i+1}')
            bottom_layout.addWidget(button)

        boton_regreso = QPushButton('Regresar')
        boton_regreso.clicked.connect(self.back_to_main_window)
        bottom_layout.addWidget(boton_regreso)

        right_layout.addLayout(bottom_layout)

    def back_to_main_window(self):
        self.close()
        from main import MainWindow 
        self.ventana_principal = MainWindow()
        self.ventana_principal.show()

class SenoidalPlot(QWidget):
    def __init__(self):
        super().__init__()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.canvas)

        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)

        self.ax.plot(x, y)
        self.ax.set_title('Gráfica')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ejemploGrafica()
    window.show()
    sys.exit(app.exec())
