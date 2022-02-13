from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout

from PyQt5.QtGui import QPixmap, QImage

import numpy as np


class Panel(QWidget):

    def __PrivateMethod(self):
        print("private method, value of")
        return

    def __init__(self):
        QWidget.__init__(self)
        self.initWidgets()
        pass

    def resizePanel(self, w , h ):
        self._width = w
        self._height = h
        self.resize(w, h)
        return

    def initWidgets(self):
        self.resizePanel(800, 600);

        # control
        self.btnOpenCamera=QPushButton(self)
        self.btnOpenCamera.setText("Open")

        self.btnCloseCamera=QPushButton(self)
        self.btnCloseCamera.setText("Close")

        self.btnStopCamera=QPushButton(self)
        self.btnStopCamera.setText("Stop")

        # img show
        self.lbl_img = QLabel(self)
        self.lbl_img1 = QLabel(self)
        self.lbl_img2 = QLabel(self)
        self.lbl_img3 = QLabel(self)

        self.lbl_img.resize(400, 300)
        self.lbl_img1.resize(400, 300)
        self.lbl_img2.resize(400, 300)
        self.lbl_img3.resize(400, 300)

        layCtl = QHBoxLayout()
        layCtl.addWidget(self.btnOpenCamera)
        layCtl.addWidget(self.btnStopCamera)
        layCtl.addWidget(self.btnCloseCamera)

        lay = QGridLayout()
        lay.addWidget(self.lbl_img, 0, 0)
        lay.addWidget(self.lbl_img1, 1, 1)
        lay.addWidget(self.lbl_img2, 1, 0)
        lay.addWidget(self.lbl_img3, 0, 1)

        mainLay = QVBoxLayout()
        mainLay.addLayout(layCtl)
        mainLay.addLayout(lay)

        self.setLayout(mainLay)

        return

    def showCvImg(self, cv_img):

        h, w, d = cv_img.shape
        qimg = QImage(cv_img.data, w, h, w*d, QImage.Format_Grayscale16)
        pix_map = QPixmap(qimg)
        pix_map = pix_map.scaled(400, 300)

        qimg1 = QImage(cv_img.data, w, h, w*d, QImage.Format_RGB888)
        pix_map1 = QPixmap(qimg1)
        pix_map1 = pix_map1.scaled(400, 300)

        self.lbl_img.setPixmap(pix_map)
        self.lbl_img1.setPixmap(pix_map1)
        pass
