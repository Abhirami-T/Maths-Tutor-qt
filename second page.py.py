import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class RandomMathApp(QWidget):
    #def __init__(self, max_levels=5):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)  # Increase the window size
        #self.max_levels = max_levels
        #self.current_level = 1
        self.init_ui()

    def init_ui(self):
        # Create widgets
        font = QFont("Arial", 16)  # Set a custom font and size
        self.display_label = QLabel('')
        self.display_label.setFont(font)

        self.message_label = QLabel('')
        self.message_label.setFont(font)

        self.answer_input = QLineEdit()
        self.answer_input.setFont(font)

        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(self.next_action)
        self.next_button.setFont(font)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.display_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.answer_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.message_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Set the layout for the main window
        self.setLayout(layout)


        # Connect the Enter key press event in the answer input field
        self.answer_input.returnPressed.connect(self.next_action)

        # Initialize the first math problem
        self.generate_math_problem()

        # Set up the main window
        self.setWindowTitle('Maths-Tutor')
        self.show()

    def generate_math_problem(self):
        # Generate two random numbers for the math problem
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 5)

        # Store the correct answer
        self.correct_answer = num1 + num2

        # Display the math problem in the label
        self.display_label.setText(f"{num1} + {num2} ")

    def next_action(self):
        # Check if the entered result is equal to the correct answer
        user_input = self.answer_input.text()
        try:
            user_result = int(user_input)
            if user_result == self.correct_answer:
                self.message_label.setText('Good! Correct answer.')
            else:
                self.message_label.setText(f'Incorrect. The correct answer is {self.correct_answer}. Try again.')
        except ValueError:
            self.message_label.setText('Invalid input. Enter a number.')
        finally:
            # Clear the answer entry field
            self.answer_input.clear()

        # Generate a new math problem for the next round
        self.generate_math_problem()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = RandomMathApp(max_levels=5)  # Set the desired number of levels
    ex = RandomMathApp()  # Set the desired number of levels
    sys.exit(app.exec())
