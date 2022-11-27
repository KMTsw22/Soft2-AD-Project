from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
import requests,json


form_weatherwindow = uic.loadUiType("weather.ui")[0] #날씨정보 ui 열기 위함
class weatherwindow(QDialog, QWidget, form_weatherwindow):
    def __init__(self):
        try:
            super(weatherwindow, self).__init__()
            self.initUI()                                       #initUI 함수 실행
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)   #제목 없애고 맨앞으로
        except Exception as e:
            print("__init", e)


    def initUI(self):
        try:
            self.setupUi(self)      #UI 생성
            button = self.sender()  #클릭된 버튼의 이름이 button으로 저장
            city = button.text()    # 도시
            apiKey = "8a3b627677918db38cedf281fd6f94c6" #날씨 api 키 openweathermap 에서 받아옴
            lang = "kr"  # 언어설정
            units = "metric"  # 화씨 온도를 섭씨 온도로 변경
            api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

            result = requests.get(api)                  #requsets라이브러리로 api 원격 호출
            result = json.loads(result.text)            #원격 호출한것을 JSON을 이용하여 파이썬 형태로 변환


            self.Area.setText(result['name'])                   # 지역
            self.Lon.setText(str(result['coord']['lon']))       # 경도
            self.Lat.setText(str(result['coord']['lat']))       # 위도
            self.weat.setText(result['weather'][0]['main'])     # 날씨
            self.temper.setText(str(result['main']['temp']))    # 온도
            self.hum.setText(str(result['main']['humidity']))   # 습도
            self.Back.clicked.connect(self.back)                # Back 버튼 눌릴시 Back 함수 실행

        except Exception as e:
            print("initUi", e)

    def back(self):
        try:
            self.close()                #Back 버튼 눌릴시 날씨정보창 닫음
        except Exception as e:
            print("Back", e)
