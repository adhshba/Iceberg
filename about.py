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
        <p style=" font-size:xx-large; border: 3px solid #08013D; padding: 10px; border-radius: 7px;">Нашей командой было разработано приложение, которое заметно облегчит работу пользователю. 
        Его основной функцией является обнаружение белого медведя на аэрофотоснимке. 
        С помощью кнопки «Найти медведя» пользователь может загрузить фото, после чего начнется поиск. 
        Также, пользователю доступна история поиска. Данная функция позволит быстро найти снимок, который был обработан раннее. 
        Для просмотра дополнительной информации о программе доступны кнопки «Помощь» и «О проекте».;</p>
    </h1><br>
    <h1 align="center" style=" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
        <p style=" font-size:xx-large; border: 3px solid #08013D; padding: 10px; border-radius: 7px;">О проекте:
Участниками команды S.O.L.T. хакатона Цифрового Прорыва было создано приложение, позволяющее ученым быстро и легко находить белых медведей на аэрофотоснимках. 
Также, мы разработали бота в Вк. 
Благодаря хорошо обученной нейросети точность определения медведя крайне высокая, а удобный интерфейс позволит каждому разобраться в работе приложения.</p>
    </h1>
</body>
</html>'''


class AboutWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        uic.loadUi('about.ui', self)
        self.setGeometry(200, 40, 900, 737)
        self.a = QWebEngineView(self)
        self.a.setHtml(x)
        self.gridLayout.addWidget(self.a)

