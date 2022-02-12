# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *

from ui.MainWindow import MainWindow
from ui.Panel import Panel

from media.ComVersion import CameraControl

import cv2


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()
    win.startVideo()
#    face_win = Panel()
#    face_win.move(10, 10)
#    face_win.show()

#    cameraCtl = CameraControl()
#    cameraCtl.open()

#    while(True):
#        frame = cameraCtl.getFrame()
#        cv2.imshow('Video', frame)

#        pix_map = cameraCtl.matToQPixmap(frame)
#        face_win.showImg(pix_map)

#        if cv2.waitKey(50) & 0XFF==ord("q"):
#            print("dwe")

    sys.exit(app.exec_())
