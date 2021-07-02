import sys

import traceback
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QTransform
from PyQt5 import uic, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QStatusBar, QScrollArea
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QColor, QFont, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import os
from found_bears import MainWidget
from about import AboutWidget
from history import HistoryWidget
from help import HelpWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.main = MainWidget(self)
        self.main.show()
        self.about = AboutWidget(self)
        self.about.hide()
        self.history = HistoryWidget(self)
        self.history.hide()
        self.help = HelpWidget(self)
        self.help.hide()

        oImage = QImage("images/main_page.jpg")
        sImage = oImage.scaled(QSize(1119, 737))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.history_btn.clicked.connect(self.history_show)
        self.main_btn.clicked.connect(self.main_show)
        self.about_btn.clicked.connect(self.about_show)
        self.about_btn_2.clicked.connect(self.help_show)

    def main_show(self):
        self.main.show()
        self.help.hide()
        self.history.hide()
        self.about.hide()

    def about_show(self):
        self.main.hide()
        self.help.hide()
        self.about.show()
        self.history.hide()

    def history_show(self):
        self.history = HistoryWidget(self)
        self.history.show()
        self.help.hide()
        self.main.hide()
        self.about.hide()

    def help_show(self):
        self.main.hide()
        self.help.show()
        self.about.hide()
        self.history.hide()


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)


sys.excepthook = excepthook
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())