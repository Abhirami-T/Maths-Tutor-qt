import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QPushButton, QMessageBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QVBoxLayout, QWidget, QFrame
)
from PyQt6.QtGui import QColor, QPalette, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Maths tutor")

        # Change background color
        self.set_background_color(QColor(255, 255, 255))  # You can adjust the RGB values

    def set_background_color(self, color):
        palette = self.palette()
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, color)
        self.setPalette(palette)

        button = QPushButton("Quit", self)
        button.clicked.connect(self.close)
        button.resize(120, 60)
        button.move(1100, 700)
        button.setStyleSheet("color:black; background-color:#D3D3D3; font:bold 20pt;")

        # Connect the button's clicked signal to a custom slot (function)
        button.clicked.connect(self.button_clicked)

        button1 = QPushButton("Start", self)
        button1.resize(120, 40)
        button1.move(590, 300)
        button1.setStyleSheet("color:black; background-color:#D3D3D3; font:bold 20pt;")

        # Connect the button's clicked signal to a custom slot (function)
        button1.clicked.connect(self.button_startclicked)

        button2 = QPushButton("Load your questions", self)
        button2.resize(200, 40)
        button2.move(550, 360)
        button2.setStyleSheet("color:#990000; background-color:	#F5F5F5 ; font:bold 15pt;")

        # Connect the button's clicked signal to a custom slot (function)
        button2.clicked.connect(self.button_loadclicked)

        button3 = QPushButton("About", self)
        button3.resize(120, 60)
        button3.move(95, 700)
        button3.setStyleSheet("color:black; background-color:#D3D3D3; font:bold 20pt;")

        # Connect the button's clicked signal to a custom slot (function)
        button3.clicked.connect(self.button_aboutclicked)

        button4 = QPushButton("Help", self)
        button4.resize(120, 60)
        button4.move(600, 700)
        button4.setStyleSheet("color:black; background-color:#D3D3D3; font:bold 20pt;")

        # Connect the button's clicked signal to a custom slot (function)
        button4.clicked.connect(self.button_helpclicked)

        label = QLabel("Maths-Tutor", self)
        label.move(500, 00)  # Adjust the position as needed

        # Change font color, font, and background color
        label.setStyleSheet("font: 30pt 'Algerian'; color: red;")

        # First combo box and label
        label_operator = QLabel("Choose the operator:", self)
        label_operator.move(400, 200)

        font = label_operator.font()
        font.setPointSize(15)
        label_operator.setFont(font)

        label_operator.setStyleSheet("color: black; font: 15pt 'Calibri ';")

        combo_box_operator = QComboBox(self)
        combo_box_operator.addItem("Addition (+)")
        combo_box_operator.addItem("Subtraction (-)")
        combo_box_operator.addItem("Division (/)")
        combo_box_operator.addItem("Multiplication (*)")
        combo_box_operator.move(620, 200)
        combo_box_operator.resize(200, 30)

        combo_box_operator_font = QFont()
        combo_box_operator_font.setPointSize(12)
        combo_box_operator.setFont(combo_box_operator_font)

        item_font_operator = QFont()
        item_font_operator.setItalic(True)

        # Second combo box and label
        label_level = QLabel("Choose the level:", self)
        label_level.move(400, 250)

        font = label_level.font()
        font.setPointSize(15)
        label_level.setFont(font)

        label_level.setStyleSheet("color: black; font: 15pt 'Calibri(body)';")

        combo_box_level = QComboBox(self)
        combo_box_level.addItem("Low")
        combo_box_level.addItem("Medium")
        combo_box_level.addItem("Hard")
        combo_box_level.move(620, 250)
        combo_box_level.resize(200, 30)

        # Use the same styling as the first combo box
        combo_box_level.setStyleSheet(combo_box_operator.styleSheet())

        combo_box_level_font = QFont()
        combo_box_level_font.setPointSize(12)
        combo_box_level.setFont(combo_box_level_font)

        item_font_level = QFont()
        item_font_level.setItalic(True)

    def button_clicked(self):
        # This function will be called when the button is clicked
        print('Quit Button Clicked!')

    def button_startclicked(self):
        # This function will be called when the "Start" button is clicked
        print('Start Button Clicked!')

    def button_loadclicked(self):
            # This function will be called when the "Start" button is clicked
        print('load Button Clicked!')

    def button_aboutclicked(self):
        # This function will be called when the "Start" button is clicked
        print('about Button Clicked!')

    def button_helpclicked(self):
        # This function will be called when the "Start" button is clicked
        print('help Button Clicked!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


