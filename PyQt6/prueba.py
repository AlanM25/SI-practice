from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(800, 400))
        self.setWindowTitle("Volume Converter")
        self.setStyleSheet("background-color: #2C54C1; color: white;")

        # main
        main_layout = QHBoxLayout()

        # panel izquierdo
        left_panel = QVBoxLayout()

        # header
        unit_layout = QHBoxLayout()
        self.button_cm = QPushButton("CM")
        self.button_inch = QPushButton("Inch")
        self.button_cm.setStyleSheet("background-color: #1B3B89; color: white; padding: 10px; border: none;")
        self.button_inch.setStyleSheet("background-color: #1B3B89; color: white; padding: 10px; border: none;")
        self.button_cm.clicked.connect(lambda: self.set_unit("cm"))
        self.button_inch.clicked.connect(lambda: self.set_unit("inch"))
        unit_layout.addWidget(self.button_cm)
        unit_layout.addWidget(self.button_inch)
        left_panel.addLayout(unit_layout)

        # Dimension inputs
        self.length_label = QLabel("Length:")
        self.width_label = QLabel("Width:")
        self.height_label = QLabel("Height:")

        self.length_input = self.create_spinbox()
        self.width_input = self.create_spinbox()
        self.height_input = self.create_spinbox()

        self.length_input.valueChanged.connect(self.update_volume)
        self.width_input.valueChanged.connect(self.update_volume)
        self.height_input.valueChanged.connect(self.update_volume)

        left_panel.addLayout(self.create_input_row(self.length_label, self.length_input))
        left_panel.addLayout(self.create_input_row(self.width_label, self.width_input))
        left_panel.addLayout(self.create_input_row(self.height_label, self.height_input))

        # Volume display
        self.volume_label = QLabel("1.00 m³")
        self.volume_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.volume_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_panel.addWidget(self.volume_label)

        # Unit text
        self.unit_text = QLabel("Meters Cubed")
        self.unit_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_panel.addWidget(self.unit_text)



        # Add left panel to main layout
        main_layout.addLayout(left_panel)

        # Right panel
        right_panel = QVBoxLayout()

        # Cube diagram placeholder
        cube_label = QLabel()
        cube_label.setPixmap(cube_label.grab().scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
        cube_label.setStyleSheet("border: 2px solid white;")
        right_panel.addWidget(cube_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # How it works text
        explanation = QLabel("Length x Width x Height")
        explanation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        explanation.setStyleSheet("font-size: 16px;")
        right_panel.addWidget(explanation)

        # Add right panel to main layout
        main_layout.addLayout(right_panel)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Initial unit
        self.current_unit = "cm"

    def create_spinbox(self):
        spinbox = QDoubleSpinBox()
        spinbox.setRange(0, 10000)
        spinbox.setDecimals(2)
        spinbox.setValue(1.00)
        spinbox.setStyleSheet(
            "background-color: white; color: black; padding: 5px; border-radius: 5px;"
        )
        return spinbox

    def create_input_row(self, label, input_widget):
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(input_widget)
        return layout

    def set_unit(self, unit):
        self.current_unit = unit
        if unit == "cm":
            self.unit_text.setText("Meters Cubed")
        elif unit == "inch":
            self.unit_text.setText("Inches Cubed")
        self.update_volume()

    def update_volume(self):
        length = self.length_input.value()
        width = self.width_input.value()
        height = self.height_input.value()

        if self.current_unit == "cm":
            volume = (length * width * height) / 1000000  # Convert cm³ to m³
            self.volume_label.setText(f"{volume:.2f} m³")
        elif self.current_unit == "inch":
            volume = length * width * height  # Inches³
            self.volume_label.setText(f"{volume:.2f} in³")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
