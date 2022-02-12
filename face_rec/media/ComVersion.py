# This Python file uses the following encoding: utf-8
import cv2
from PyQt5 import QtGui


class CameraControl:

    def __init__(self):
        self.isCameraOpen = False
        pass

    def open(self):
        self.capture = cv2.VideoCapture(0)
        self.isCameraOpen = True

    def close(self):
        if self.isCameraOpen:
            self.capture.release()
            cv2.destroyAllWindows

    def matToQPixmap(self, cvimg):
        h, w, d = cvimg.shape
        # cving = QtGui.QImage(cvimg.data, w, h, w*d, QtGui.QImage.Format_Grayscale16)
        cving = QtGui.QImage(cvimg.data, w, h, w*d, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap( cving )

    def getFrame(self):
        if not self.isCameraOpen:
            print("camera is not open!")
            return
        else:
            ret, frame = self.capture.read()
            return frame
