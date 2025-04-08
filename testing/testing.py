from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 600)
        self.setLayout(QVBoxLayout())


app=QApplication([])
window=calculator()
window.show()
app.exec_()