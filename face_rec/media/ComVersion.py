# This Python file uses the following encoding: utf-8
import cv2
from PyQt5 import QtGui


class CameraControl:

    def __init__(self):
        self.isCameraOpen = False
        pass

    def open(self):
        print("open camera")
        self.capture = cv2.VideoCapture(0)
        self.isCameraOpen = True
        return

    def open(self):
        print("open camera")
        self.capture = cv2.VideoCapture(0)
        self.isCameraOpen = True
        return

    def close(self):
        self.isCameraOpen = False

        print("close camera")
        if self.isCameraOpen:
            self.capture.release()
            # cv2.destroyAllWindows

    def getFrame(self):
        if not self.isCameraOpen:
            print("camera is not open!")
            return False, None
        else:
            ret, frame = self.capture.read()
            return True, frame
