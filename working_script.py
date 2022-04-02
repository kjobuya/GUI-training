import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class my_window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.UISetup()
        
    def UISetup(self):
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        
        self.button.setFixedSize()

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
        # self.setFixedSize(QSize(400, 300))
        self.setMaximumSize(QSize(400,300))
        
app = QApplication([])

window = my_window()
window.show()

app.exec()