import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout
from PyQt6.QtCore import QTimer
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from main import MainWindow

class lecturaPuerto(QMainWindow):
    def __init__(self):
        super().__init__()

        self.serial_port = None
        self.data_points = []
        self.time_points = []

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout(self.central_widget)

        self.button_start = QPushButton('Iniciar Lectura', self)
        self.button_start.clicked.connect(self.start_reading)
        self.layout.addWidget(self.button_start, 0, 0)

        self.button_stop = QPushButton('Detener Lectura', self)
        self.button_stop.clicked.connect(self.stop_reading)
        self.layout.addWidget(self.button_stop, 0, 1)
        self.button_stop.setEnabled(False)

        self.plot_widget = QWidget(self)
        self.plot_layout = QVBoxLayout(self.plot_widget)
        self.figure, self.ax = plt.subplots()
        self.plot_canvas = FigureCanvas(self.figure)
        self.plot_layout.addWidget(self.plot_canvas)
        self.layout.addWidget(self.plot_widget, 1, 0, 1, 2)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_and_plot_data)
        self.reading_started = False

        self.button_back = QPushButton('Volver a la Ventana Principal')
        self.button_back.clicked.connect(self.back_to_main_window)
        self.layout.addWidget(self.button_back, 2, 0, 1, 2) 

    def back_to_main_window(self):
        self.close()  # Cerrar la ventana secundaria
        from main import MainWindow  # Importar la clase MainWindow aquí para evitar la importación circular
        self.ventana_principal = MainWindow()
        self.ventana_principal.show()

    def start_reading(self):
        if not self.reading_started:
            try:
                self.serial_port = serial.Serial('COM3', 9600)  # Modifica el puerto serial según tu configuración
                self.reading_started = True
                self.button_start.setEnabled(False)
                self.button_stop.setEnabled(True)
                self.timer.start(100)  # Intervalo de lectura en milisegundos
            except serial.SerialException as e:
                print("Error al abrir el puerto serial:", e)
        else:
            print("La lectura ya está en curso.")

    def stop_reading(self):
        if self.reading_started:
            self.reading_started = False
            self.button_start.setEnabled(True)
            self.button_stop.setEnabled(False)
            self.timer.stop()
            if self.serial_port is not None:
                self.serial_port.close()

    def read_and_plot_data(self):
        if self.reading_started:
            if self.serial_port is not None and self.serial_port.is_open:
                data = self.serial_port.readline().decode().strip()
                try:
                    value = float(data.split(':')[-1].strip('cm'))
                    self.data_points.append(value)
                    self.time_points.append(len(self.data_points))
                    self.ax.clear()  # Limpiar el eje antes de trazar nuevamente
                    self.ax.plot(self.time_points, self.data_points, color='b')
                    self.plot_canvas.draw()
                except ValueError:
                    pass  # Ignorar errores de conversión de datos
            else:
                pass  # Ignorar si el puerto serial no está abierto o no se puede leer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = lecturaPuerto()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
