from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import *
import requests,json

form_weatherwindow = uic.loadUiType("weather.ui")[0]


class weatherwindow(QDialog, QWidget, form_weatherwindow):
    def __init__(self):
        try:
            super(weatherwindow, self).__init__()
            self.initUI()
            self.show()  # 두번째창 실행
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        except Exception as e:
            print("__init", e)


    def initUI(self):
        try:
            self.setupUi(self)
            button = self.sender()
            city = button.text()  # 도시
            apiKey = "8a3b627677918db38cedf281fd6f94c6"
            lang = "kr"  # 언어
            units = "metric"  # 화씨 온도를 섭씨 온도로 변경
            api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

            result = requests.get(api)
            result = json.loads(result.text)
            self.Area.setText(result['name'])  # 지역
            self.Lon.setText(str(result['coord']['lon']))  # 경도
            self.Lat.setText(str(result['coord']['lat'])) # 위도
            self.weat.setText(result['weather'][0]['main'])  # 날씨
            self.temper.setText(str(result['main']['temp']))  # 온도
            self.hum.setText(str(result['main']['humidity']))  # 습도
            self.Back.clicked.connect(self.back)

        except Exception as e:
            print("initUi", e)

    def back(self):
        try:
            self.close()
        except Exception as e:
            print("Back", e)
