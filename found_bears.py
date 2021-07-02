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


class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        uic.loadUi('widget.ui', self)
        self.setGeometry(250, 55, 780, 671)

        self.load_im.clicked.connect(self.select_image)
        self.select_dir.clicked.connect(self.select_directory)

        self.loader_file = QMovie("images/find_bears1.png")
        self.loader_file.start()
        self.loader_label.setMovie(self.loader_file)
        self.loader_label.adjustSize()
        self.loader_label.show()
        overlayLabel = QLabel(self.loader_label)
        overlayLabel.move(0, 0)
        overlayLabel.show()
        self.pbar.hide()

    def select_image(self):
        self.label.hide()
        fname = QFileDialog.getOpenFileName(self, 'Выберите картинку', '',
                                            'Картинка (*.jpg);')
        if fname[0]:
            dir_name = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения", ".")
            if not dir_name:
                x = QMessageBox.information(self, "Информация", "Вы не выбрали директорию для сохранения",
                                            QMessageBox.SaveAll, QMessageBox.Cancel)
                if x == 4096:
                    dir_name = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения", ".")
            if dir_name:
                self.label.show()
                x = dir_name + '/' + os.path.basename(f'{fname[0]}')[:-4] + '_1' + '.jpg'
                #x = func(fname[0], x)
                # передача пути к изображению нейросети и путь куда нужно сохранить фото
                # возвращает True или False в зависимости от наличия медведей
                conn = sqlite3.connect("db/bears_pic.db")
                cur = conn.cursor()
                cur.execute(f"""INSERT INTO data(dir, date, bear) 
                   VALUES("{x}", "{datetime.datetime.today().date()}", False);""")
                conn.commit()
                self.label.setStyleSheet('''background-color: white;''')
                pixmap = QPixmap(x)
                if pixmap.height() < pixmap.width():
                    pixmap = pixmap.transformed(QTransform().rotate(90))
                pixmap = pixmap.scaledToHeight(650)
                self.label.setPixmap(pixmap)
                self.label.show()

    def select_directory(self):
        self.label.hide()
        fname = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        if fname:
            dir_name = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения", ".")
            if not dir_name:
                x = QMessageBox.information(self, "Информация", "Вы не выбрали директорию для сохранения",
                                            QMessageBox.SaveAll, QMessageBox.Cancel)
                if x == 4096:
                    dir_name = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения", ".")
            if dir_name:
                self.label.show()
                listOfFiles = os.listdir(fname)
                pattern = "*.jpg"
                self.pbar.show()
                files = [fname + '/' + entry for entry in listOfFiles if fnmatch.fnmatch(entry, pattern)]
                step = 100 // len(files)
                value = step
                for file in files:
                    save_dir = dir_name + '/' + os.path.basename(f'{file}')[:-4] + '_1' + '.jpg'
                    self.label.setStyleSheet(f'''background-color: white;''')
                    pixmap = QPixmap(file)
                    if pixmap.height() < pixmap.width():
                        pixmap = pixmap.transformed(QTransform().rotate(90))
                    pixmap = pixmap.scaledToHeight(650)
                    self.label.setPixmap(pixmap)
                    self.label.show()
                    self.pbar.setValue(value)

                    # func(fname + '/' + entry, save_dir)
                    # путь к изображению идет в нейросеть
                    conn = sqlite3.connect("db/bears_pic.db")
                    cur = conn.cursor()
                    cur.execute(f"""INSERT INTO data(dir, date, bear) 
                                       VALUES("{save_dir}", "{datetime.datetime.today().date()}", True);""")
                    conn.commit()
                    value += step
                self.pbar.setValue(0)
                self.pbar.hide()

