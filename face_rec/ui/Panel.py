from PyQt5.QtWidgets import QWidget, QLabel
import numpy as np

class Panel(QWidget):

    def __PrivateMethod(self):
        print("private method, value of a: ", a)

    def __init__(self):
        QWidget.__init__(self)
        self.initWidgets()
        pass

    def initWidgets(self):
        self.outputPanel = QLabel(self)
        self.outputPanel.setText("Hello World")
        self.outputPanel.resize(800, 600)
        self.resize(800, 600)
        pass

    def showImg(self, pix_map):
        self.outputPanel.setPixmap(pix_map)
