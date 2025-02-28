from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(400, 400))

        self.setWindowTitle("Calculadora")
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        #first column
        self.button = QPushButton("7")
        self.button2 = QPushButton("8")
        self.button3 = QPushButton("9")
        self.button4 = QPushButton("/")

        #second column
        self.button5 = QPushButton("4")
        self.button6 = QPushButton("5")
        self.button7 = QPushButton("6")
        self.button8 = QPushButton("*")

        #third column
        self.button9 = QPushButton("1")
        self.button10 = QPushButton("2")
        self.button11 = QPushButton("3")
        self.button12 = QPushButton("-")

        #fourth column
        self.button13 = QPushButton("0")
        self.button14 = QPushButton("=")
        self.button15 = QPushButton("+")

        self.button.clicked.connect(self.the_button_was_clicked)

        self.input2 = QLineEdit()

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()

        layout.addWidget(self.input)

        layout.addLayout(layout2)
        layout2.addWidget(self.button)
        layout2.addWidget(self.button2)
        layout2.addWidget(self.button3)
        layout2.addWidget(self.button4)

        layout3.addWidget(self.button5)
        layout3.addWidget(self.button6)
        layout3.addWidget(self.button7)
        layout3.addWidget(self.button8)
        layout.addLayout(layout3)

        layout4.addWidget(self.button9)
        layout4.addWidget(self.button10)
        layout4.addWidget(self.button11)
        layout4.addWidget(self.button12)
        layout.addLayout(layout4)

        layout5 = QHBoxLayout()
        layout5.addWidget(self.button13)
        layout5.addWidget(self.button14)
        layout5.addWidget(self.button15)
        layout.addLayout(layout5)


        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)
    def the_button_was_clicked(self):
        self.button.setEnabled(False)
        #cadena=self.input.text()
        print("Clicked! " + self.input.text())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()