import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botón Redondo en PyQt6")

        # Crear el botón
        self.round_button = QPushButton("Click", self)
        self.round_button.setFixedSize(100, 100)  # Ancho y alto iguales
        self.round_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db; /* Color de fondo */
                color: white; /* Color del texto */
                font-size: 16px;
                border: none; /* Sin bordes */
                border-radius: 50%; /* Forma circular */
            }
            QPushButton:hover {
                background-color: #2980b9; /* Color al pasar el mouse */
            }
        """)
        self.round_button.clicked.connect(self.button_clicked)

        # Configuración de la ventana
        self.setCentralWidget(self.round_button)

    def button_clicked(self):
        print("¡Botón redondo presionado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(200, 200)  # Tamaño de la ventana
    window.show()
    sys.exit(app.exec())
