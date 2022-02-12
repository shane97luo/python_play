from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from PyQt5 import QtGui

import numpy as np

class Panel(QWidget):

    def __PrivateMethod(self):
        print("private method, value of a: ", a)

    def __init__(self):
        QWidget.__init__(self)
        self.initWidgets()

        pass

    def initWidgets(self):
        self.resize(800, 600)


        self.lbl_img = QLabel(self)
        self.lbl_img.resize(400, 300)
        self.lbl_img1 = QLabel(self)
        self.lbl_img1.resize(400, 300)

        lay = QVBoxLayout()
        lay.addWidget(self.lbl_img)
        lay.addWidget(self.lbl_img1)
        self.setLayout(lay)

        pass

    def showCvImg(self, cv_img):

        h, w, d = cv_img.shape
        qimg = QtGui.QImage(cv_img.data, w, h, w*d, QtGui.QImage.Format_Grayscale16)
        pix_map = QtGui.QPixmap(qimg)
        pix_map = pix_map.scaled(400, 200)

        qimg1 = QtGui.QImage(cv_img.data, w, h, w*d, QtGui.QImage.Format_RGB888)
        pix_map1 = QtGui.QPixmap(qimg1)
        pix_map1 = pix_map1.scaled(400, 200)

        self.lbl_img.setPixmap(pix_map)
        self.lbl_img1.setPixmap(pix_map1)
        pass
