# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()
    win.startVideo()

    sys.exit(app.exec_())
