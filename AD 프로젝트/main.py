import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from WeatherMapwindow import secondwindow
from map import MapWindow
form_main = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, QWidget, form_main):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""


    def initUI(self):
        self.setupUi(self)
        self.Weatherbutton.clicked.connect(self.button_Weather)
        self.Map_button.clicked.connect(self.buttonMap)

    def buttonMap(self):
        try:
            self.close()
            self.Map_ = MapWindow()
            self.Map_.exec()
            self.show()
        except Exception as e:
            print("buttonMap", e)

    def button_Weather(self):
        try:
            self.close()
            self.weather = secondwindow()
            self.weather.exec()
            self.show()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()