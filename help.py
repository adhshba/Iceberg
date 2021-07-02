import sys
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QTransform
from PyQt5 import uic, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QStatusBar, QScrollArea
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog, QGridLayout
from PyQt5.QtGui import QColor, QFont
import os
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


x = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        p {color: #81A9EE;}
       p:hover {
        color: #455596;
       }
    </style>
</head>
<body>
    <h1 align="center" style=" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:xx-large; font-weight:600;">Iceberg.</span></h1>
    
    <h1 align="center" style=" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
        <p style=" font-size:xx-large; border: 3px solid #08013D; padding: 10px; border-radius: 7px;">Справка по приложению
1. Чтобы приступить к работе, нажмите кнопку «Загрузить медведя»
2. Выберите фото, и после некоторой обработки, в папку с программой будет сохранен результат.
3. Если Вы хотите увидеть недавно обработанные снимки, то нажмите на кнопку «История поиска»
4. Если Вы хотите узнать информацию о проекте, то нажмите на кнопку «О проекте»
5. В случае ошибок, вопросов, пожеланий и предложений, обращайтесь по адресу iceberg@it.com
Спасибо за использование нашей программы!</p>
    </h1>
</body>
</html>'''


class HelpWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        uic.loadUi('about.ui', self)
        self.setGeometry(200, 40, 900, 850)
        self.a = QWebEngineView(self)
        self.a.setHtml(x)
        self.gridLayout.addWidget(self.a)