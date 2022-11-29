import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic                           #desingner로 만든 ui를 열기 위해 사용
from WeatherMapwindow import WeatherMapwindow   # 날씨
from map import MapWindow                       #지도(네비게이션)
form_main = uic.loadUiType("main.ui")[0]        #메인 ui

class MyWindow(QMainWindow, QWidget, form_main):

    def __init__(self):
        try:
            super().__init__()
            self.initUI() #함수 initUI 실행
        except Exception as e:
            print("__init__", e)
    def initUI(self):
        try:
            self.setupUi(self)
            self.Weatherbutton.clicked.connect(self.button_Weather) #weather 버튼 클릭시 button_Weather 함수로 이동
            self.Map_button.clicked.connect(self.buttonMap)         #Map_button 클릭시 buttonMap 함수로 이동
        except Exception as e:
            print("initUi", e)


    def buttonMap(self):
        try:
            self.Map_ = MapWindow()             #buttonMap이 눌렸을 떄 Map 윈도우를 실행하기위함
            self.Map_.exec()                    #event loop 실행
        except Exception as e:
            print("buttonMap", e)

    def button_Weather(self):
        try:
            self.weather = WeatherMapwindow()       #Weather 윈도우를 실행하기 위함
            self.weather.exec()                     #event loop 실행
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
