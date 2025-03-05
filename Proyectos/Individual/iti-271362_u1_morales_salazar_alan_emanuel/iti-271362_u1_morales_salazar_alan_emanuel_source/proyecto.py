from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QPixelFormat, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDoubleSpinBox, QFrame
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(800, 400))
        self.setWindowTitle("Volumen Converter")
        self.setStyleSheet("background-color: #3164cb; color: white;")

        #layout main
        layout_main = QHBoxLayout()

        #layouts
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()

        #header
        header_layout = QHBoxLayout()
        self.button_cm = QPushButton("CM")
        self.button_inch = QPushButton("Inch")
        self.button_cm.setStyleSheet("background-color: #19347F; color: white; padding: 10px; border: none;")
        self.button_inch.setStyleSheet("background-color: #19347F; color: white; padding: 10px; border: none;")
        self.button_cm.clicked.connect(lambda: self.unit("cm"))
        self.button_inch.clicked.connect(lambda: self.unit("inch"))
        header_layout.addWidget(self.button_cm)
        header_layout.addWidget(self.button_inch)
        layout_left.addLayout(header_layout)

        # unit initial
        self.current_unit = "cm"
        self.imperial_unit = "m3"

        # inputs
        self.lenght = QLabel("Lenght: ")
        self.widht = QLabel("Widht: ")
        self.height = QLabel("Height: ")

        self.lenght_input = self.c_spinbox()
        self.widht_input = self.c_spinbox()
        self.height_input = self.c_spinbox()

        #esto hace que el label del volumen se modifique automaticamente
        self.lenght_input.valueChanged.connect(self.update_volume)
        self.widht_input.valueChanged.connect(self.update_volume)
        self.height_input.valueChanged.connect(self.update_volume)

        #agrega los layouts al layout_left
        layout_left.addLayout(self.rows_units(self.lenght, self.lenght_input))
        layout_left.addLayout(self.rows_units(self.widht, self.widht_input))
        layout_left.addLayout(self.rows_units(self.height, self.height_input))

        #label del resultado
        layout_left.addSpacing(40)
        self.volume_label = QLabel("1.00 m3")
        self.volume_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.volume_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_left.addWidget(self.volume_label)

        #unit text
        self.unit_text = QLabel("Meters Cubed")
        self.unit_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_left.addWidget(self.unit_text)

        #Unit buttons
        self.button_meters3 = QPushButton()
        self.button_meters3.setFixedSize(20, 20)
        self.button_meters3.setStyleSheet(" QPushButton {"
                                          "background-color: #19347F;"
                                          "border-radius: 10px;"
                                          "border: none; "
                                          "}"
                                          "QPushButton:hover {"
                                          "background-color: white;"
                                          "}")
        self.button_feet3 = QPushButton()
        self.button_feet3.setFixedSize(20, 20)
        self.button_feet3.setStyleSheet(" QPushButton {"
                                          "background-color: #19347F;"
                                          "border: none; "
                                          "border-radius: 10px;"
                                          "}"
                                          "QPushButton:hover {"
                                          "background-color: white;"
                                          "}")

        self.button_cm3 = QPushButton()
        self.button_cm3.setFixedSize(20, 20)
        self.button_cm3.setStyleSheet(" QPushButton {"
                                          "background-color: #19347F;"                
                                          "border-radius: 10px;"
                                          "border: none; "
                                          "}"
                                          "QPushButton:hover {"
                                          "background-color: white;"
                                          "}")
        layout_left.addLayout(self.row_buttons(self.button_meters3, self.button_feet3, self.button_cm3))
        self.button_meters3.clicked.connect(lambda: self.imperialUnit("m3"))
        self.button_feet3.clicked.connect(lambda: self.imperialUnit("ft3"))
        self.button_cm3.clicked.connect(lambda: self.imperialUnit("cm3"))

        #esto se uso para que el layout_left tuviera diseño
        self.styleLayout = QFrame()
        self.styleLayout.setLayout(layout_left)
        self.styleLayout.setObjectName("styleLayout")
        self.styleLayout.setStyleSheet('#styleLayout {border-right: 2px solid white;}')
        layout_main.addWidget(self.styleLayout)


        #cosas del right
        self.text = QLabel("How it works...")
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imgP = QLabel()
        self.imgP.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img = QPixmap("cube.png")
        self.imgP.setPixmap(self.img.scaled(300,300))
        self.info = QLabel("Lenght x Width x Height")
        self.info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_right.addWidget(self.text)
        layout_right.addWidget(self.imgP)
        layout_right.addWidget(self.info)

        layout_main.addLayout(layout_right)

        container = QWidget()
        container.setLayout(layout_main)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def c_spinbox(self):
        """
        esta funcion de lo que se encarga es de crear un spinbox en la que se manejan los numeros que el usuario va ingresando
        """
        spinbox = QDoubleSpinBox()
        spinbox.setMinimum(0)
        spinbox.setMaximum(1000000000000000000)
        spinbox.setDecimals(2)
        spinbox.setValue(100)
        spinbox.setSingleStep(0.01)
        spinbox.setFixedSize(150, 40)
        spinbox.setStyleSheet("background-color: white; color: black;")
        return spinbox

    def rows_units(self, label, inputs):
        """
        esta funcion en lo que ayuda es en crear el layout de la fila en donde se encuentra el label y el spinbox
        """
        layout = QHBoxLayout()
        layout.addSpacing(60)
        layout.addWidget(label)
        layout.addWidget(inputs)
        layout.addSpacing(60)
        return layout

    def row_buttons(self, button1, button2, button3):
        """
        esta funcion es un poco similar a la anterior, solo que en esta manejamos el orden de los botones de cambio de unidad, ya sea a m3, ft3 o cm3
        """
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addSpacing(40)
        layout.addWidget(button2)
        layout.addSpacing(40)
        layout.addWidget(button3)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return layout

    def unit(self, unit):
        """
        esta funcion se encarga de que al momento de dar clic a uno de los botones de unidades, ya sea cm o inch, manda la unidad a esta funcion
        y esta la procesa, para que dependiendo de la unidad, en el spinbox le va a poner el valor correspondiente
        """
        if self.current_unit == unit:
            return

        self.lenght_input.blockSignals(True)
        self.widht_input.blockSignals(True)
        self.height_input.blockSignals(True)

        array = [self.button_cm, self.button_inch]
        for a in array:
            a.setStyleSheet("background-color: #19347F; color: white; padding: 10px; border: none;")

        """
            esta es la funcion que cambia el valor al spinbox dependiendo de la unidad seleccionada
        """
        if unit == "cm":
            self.button_cm.setStyleSheet("background-color: #3164cb; border: none; color: white; padding: 10px;")
            self.lenght_input.setValue(self.lenght_input.value() * 2.54)
            self.widht_input.setValue(self.widht_input.value() * 2.54)
            self.height_input.setValue(self.height_input.value() * 2.54)
        elif unit == "inch":
            self.button_inch.setStyleSheet("background-color: #3164cb; border: none; color: white; padding: 10px;")
            self.lenght_input.setValue(self.lenght_input.value() / 2.54)
            self.widht_input.setValue(self.widht_input.value() / 2.54)
            self.height_input.setValue(self.height_input.value() / 2.54)

        self.lenght_input.blockSignals(False)
        self.widht_input.blockSignals(False)
        self.height_input.blockSignals(False)
        self.current_unit = unit

    def change_color_imperialUnits(self, unit):
        """
        esta funcion lo que hace es que cambia el color de los botones seleccionados por el usuario, es para los botones de m3, ft3 y cm3
        """
        array = [self.button_meters3, self.button_feet3, self.button_cm3]
        for arrayp in array:
            arrayp.setStyleSheet("background-color: #1B3B89; border-radius: 10px; border: none;")
        if unit == "m3":
            self.button_meters3.setStyleSheet("background-color: white; border-radius: 10px; border: none;")

        elif unit == "ft3":
            self.button_feet3.setStyleSheet("background-color: white; border-radius: 10px; border: none;")

        elif unit == "cm3":
            self.button_cm3.setStyleSheet("background-color: white; border-radius: 10px; border: none;")

    def imperialUnit(self, unit):
        """
        esta es la funcion que llama al dar clic a los botones ya sea de m3, ft3 o cm3
        """
        self.imperial_unit = unit
        self.change_color_imperialUnits(unit)
        self.update_volume()

    def update_volume(self):
        """
        esta funcion es la mas importante, ya que aqui es donde se calcula el volumen
        """
        length = self.lenght_input.value()
        width = self.widht_input.value()
        height = self.height_input.value()

        if self.current_unit == "inch":
            length *= 2.54
            width *= 2.54
            height *= 2.54

        if self.imperial_unit == "m3":
            volume = (length * width * height) / 1000000
            self.volume_label.setText("{:.2f} m3".format(volume))
            self.unit_text.setText("Meters Cubed")
        elif self.imperial_unit == "ft3":
            volume = (length * width * height) / 28316.8466
            self.volume_label.setText("{:.2f} ft3".format(volume))
            self.unit_text.setText("Feets Cubed")
        elif self.imperial_unit == "cm3":
            volume = length * width * height
            self.volume_label.setText("{:.2f} cm3".format(volume))
            self.unit_text.setText("Cubic CM")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()