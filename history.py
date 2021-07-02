import sys
import time
import datetime
import sqlite3
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QTransform
from PyQt5 import uic, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QStatusBar, QScrollArea, QGridLayout
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog, QDialog, QMessageBox, QProgressBar
from PyQt5.QtGui import QColor, QFont, QImage, QPalette, QBrush, QMovie
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os, fnmatch


class HistoryWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        uic.loadUi('history_widget.ui', self)
        self.setGeometry(250, 30, 980, 737)
        self.loader_file = QMovie("images/history.jpg")
        self.loader_file.start()
        self.label_6.setMovie(self.loader_file)
        self.label_6.adjustSize()
        self.label_6.show()
        overlayLabel = QLabel(self.label_6)
        overlayLabel.move(0, 0)
        overlayLabel.show()
        conn = sqlite3.connect('db/bears_pic.db')
        cur = conn.cursor()
        self.x = cur.execute('''SELECT dir FROM data
                            WHERE bear == True
                            ORDER BY date''').fetchall()
        self.x = [d[0] for d in self.x if os.path.isfile(d[0])]
        self.load_image((self.label, self.label_2, self.label_3, self.label_4, self.label_5), *self.x)
        if len(self.x) < 6:
            self.pushButton.setEnabled(False)

        self.y = cur.execute('''SELECT dir FROM data
                            WHERE bear == False
                            ORDER BY date''').fetchall()
        self.y = [d[0] for d in self.y if os.path.isfile(d[0])]
        self.load_image((self.label_9, self.label_16, self.label_17, self.label_18, self.label_19), *self.y)
        if len(self.y) < 6:
            self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.next_2)
        self.pushButton.clicked.connect(self.next)

    def load_image(self, widget, *data):
        for d, widget in zip(data, widget):
            widget.setStyleSheet(f'''background-color: white;''')
            pixmap = QPixmap(d)
            if pixmap.height() < pixmap.width():
                pixmap = pixmap.transformed(QTransform().rotate(90))
            pixmap = pixmap.scaledToHeight(139)
            widget.setPixmap(pixmap)
            widget.show()

    def next(self):
        self.x = self.x[1:]
        if len(self.x) <= 5:
            self.pushButton.setEnabled(False)
        self.load_image((self.label, self.label_2, self.label_3, self.label_4, self.label_5), *self.x)

    def next_2(self):
        self.y = self.y[1:]
        if len(self.y) <= 5:
            self.pushButton_2.setEnabled(False)
        self.load_image((self.label_9, self.label_16, self.label_17, self.label_18, self.label_19), *self.y)