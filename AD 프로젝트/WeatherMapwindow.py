import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import *
from WeatherWindow import weatherwindow

form_secondwindow = uic.loadUiType("weathermapwindow.ui")[0]


class secondwindow(QDialog, QWidget, form_secondwindow):
    def __init__(self):
        try:
            super(secondwindow, self).__init__()
            self.initUI()
            self.show() #두번째창 실행
            self.second_text = ""
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        except Exception as e:
            print("__init", e)
    def buttonclicked_area(self):
        try:
            self.close()
            self.weather = weatherwindow()
            self.weather.exec()
            self.show()
        except Exception as e:
            print("area_button", e)

    def initUI(self):
        try:
            self.qPixmapVar = QPixmap("우리나라-지도.jpg.webp")
            self.labelimage = QLabel(self)
            self.labelimage.setPixmap(self.qPixmapVar)  # 이미지 세팅
            self.labelimage.setContentsMargins(10, 10, 10, 10)
            self.labelimage.resize(self.qPixmapVar.width(), self.qPixmapVar.height())
            self.setupUi(self)
            self.home_button.clicked.connect(self.Home)
            #지금 이거 이렇게 바꿀라고하는데 잘안돼
            # list_area = [self.Seoul, self.Busan,self.Incheon, self.Daegu, self.Gwangju, self.jeju, self.Ulsan, self.Daejeon]
            # for area in list_area:
            #     if area.click:
            #         area.clicked.connect(self.buttonclicked_area)
            # self.Seoul.clicked.connect(self.buttonclicked_area)
            self.Busan.clicked.connect(self.buttonclicked_area)
            self.Incheon.clicked.connect(self.buttonclicked_area)
            self.Daegu.clicked.connect(self.buttonclicked_area)
            self.Gwangju.clicked.connect(self.buttonclicked_area)
            self.jeju.clicked.connect(self.buttonclicked_area)
            self.Ulsan.clicked.connect(self.buttonclicked_area)
            self.Daejeon.clicked.connect(self.buttonclicked_area)

        except Exception as e:
            print("initUi" , e)
    def Home(self):
        try:
            self.close()
        except Exception as e:
            print("home", e)
