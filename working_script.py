import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class my_window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.UISetup()
        
    def UISetup(self):
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400,400))
        self.button = QPushButton("Press Me!")
        
        self.button.setCheckable(True)
        self.button.setChecked(True)
        #self.button.toggle()
        self.button.clicked.connect(self.ButtonClickedEvent)
        # self.button.clicked.connect(self.ButtonToggledEvent)
        self.windowTitleChanged.connect(self.WindowTitleChangedEvent)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
        # self.setFixedSize(QSize(400, 300))
        self.setMaximumSize(QSize(400,300))
        
    def ButtonClickedEvent(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
    def ButtonToggledEvent(self, checked):
        self.button.setText(str(self.button.isChecked()))
        # self.button.setEnabled(False)
        
    def WindowTitleChangedEvent(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)
        
app = QApplication([])

window = my_window()
window.show()

app.exec()