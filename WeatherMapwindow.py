from PyQt5.QtWidgets import *
from PyQt5 import uic                       #날씨맵 UI 열기 위함
from PyQt5 import QtCore
from PyQt5.QtGui import *
from WeatherWindow import weatherwindow     #날씨정보 알려주는 창으로 넘어가기 위함

form_WeatherMapwindow = uic.loadUiType("weathermapwindow.ui")[0]       #designer를 이용한 ui open


class WeatherMapwindow(QDialog, QWidget, form_WeatherMapwindow):
    def __init__(self):
        try:
            super(WeatherMapwindow, self).__init__()
            self.initUI()               #initUI 함수 실행
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #프로그램창을 항상 맨위에 있게 해주면서 제목 없애줌
        except Exception as e:
            print("__init", e)
    def buttonclicked_area(self):                   #지역버튼이 눌렸을떄 실행 되는 함수
        try:
            self.weather = weatherwindow()          #날씨 정보 알려주기 위해 weatherwindow 호출
            self.weather.exec()                     #event loop 실행
        except Exception as e:
            print("area_button", e)

    def initUI(self):
        try:
            self.qPixmapVar = QPixmap("우리나라-지도.jpg.webp")       #지도 이미지를 받아오기 위함.
            self.labelimage = QLabel(self)                          #받아온 이미지를 넣기 위한 라벨생성
            self.labelimage.setPixmap(self.qPixmapVar)              # 이미지 세팅
            self.labelimage.setContentsMargins(10, 10, 10, 10)     #바탕화면이랑 이미지를 구분하기위해 10만큼 떨어뜨림
            self.labelimage.resize(self.qPixmapVar.width(), self.qPixmapVar.height()) #라벨을 이미지 크기만큼 키움
            self.setupUi(self)                                          #setupUi 함수 실행
            self.home_button.clicked.connect(self.Home)                  #Home 버튼이 눌리면 Home 함수 실행

            self.Seoul.clicked.connect(self.buttonclicked_area)
            self.Busan.clicked.connect(self.buttonclicked_area)         #지역이름 눌리면 지역함수 실행
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
            self.close() #Home 버튼 눌리면 그 창 끔
        except Exception as e:
            print("home", e)
