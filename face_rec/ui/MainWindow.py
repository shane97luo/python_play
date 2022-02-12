# This Python file uses the following encoding: utf-8

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from ui.Panel import Panel

from media.ComVersion import CameraControl

import cv2
import sys

sys.path.append("../media/")


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("PyQt")

        self.initPanel()
        self.cameraCtl = CameraControl()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        print("========init the mainwindow========")
        pass

    def initPanel(self):
        self.face_win = Panel()
        self.face_win.move(10, 10)
        self.face_win.show()
        pass

    def update(self):
        frame = self.cameraCtl.getFrame()
        self.face_win.showCvImg(frame)
        pass

    def startVideo(self):
        print("start the camrea")
        self.cameraCtl.open()
        self.timer.start()
        pass

    def stopVideo(self):
        print("stop the camrea")
        self.timer.stop()
        self.cameraCtl.close()
        pass
