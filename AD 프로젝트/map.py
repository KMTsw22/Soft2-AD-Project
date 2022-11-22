import folium
import waysearch
from PyQt5.QtWidgets import *
from PyQt5 import uic
import io
import traceback
import sys
# from PyQt5 import QtCore
# from secondwindow import secondwindow
# #from img import imgwindow
# import json
# import urllib
# from PyQt5.QtWebEngineWidgets import QWebEngineView
#from urllib.request import Request, urlopen

form_mapwindow = uic.loadUiType("mapwindow.ui")[0]

class MapWindow(QDialog, QWidget, form_mapwindow):
    def __init__(self):
        super(MapWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        try:
            self.setupUi(self)
            self.address.clicked.connect(self.buttonClicked)
            self.nextbutton.clicked.connect(self.button_clicked_next)
            self.Backbutton.clicked.connect(self.button_back)
        except Exception as e:
            print("initUi", e)

    def buttonClicked(self):
        try:
            self.how.clear()
            start = self.startplace.text()
            goal = self.goalplace.text()
            print(len(start), start)
            print(len(goal), goal)

            start = waysearch.get_location(start) # 출발좌표
            goal = waysearch.get_location(goal) #도착좌표
            if start == "Error" or goal =="Error":
                self.ErrorText.setText("Error: 위치 정보가 잘못되었습니다")
                return True
            print(start)
            option = ""
            results = waysearch.get_optimal_route(start, goal, option=option)
            # *-- 목적지까지의 guidence와 각각의 거리, 소요시간 정보 추출 --*
            self.temp = [(guide['instructions'], guide['distance'], guide['duration'] / 1000) \
                         for guide in results['route']['traoptimal'][0]['guide']]

            self.start_func = start
            self.goal_func = goal
            m2 = folium.Map(location=[float(self.start_func[1]), float(self.start_func[0])],
                            zoom_start=14,
                            )
            # 출발
            folium.Marker([float(self.start_func[1]), float(self.start_func[0])],
                          popup=f'<div style="width:300px;">{start}</div>').add_to(m2)  # 마커 찍고싶은 좌표를 구해와서 원본 m에다 표시/추가
            # 도착

            folium.Marker([float(self.goal_func[1]), float(self.goal_func[0])],  # 성수역 마커에다간 기본 세팅에서 옵션 추가
                          popup=f'<div style="width:300px;">{goal}</div>').add_to(m2)  # popup: 마커 클릭시 팝업으로 상세내용 표시되는 옵션 추가
            print("hererererere")
            # save map data to data object
            data = io.BytesIO()
            m2.save(data, close_file=False)

            self.webview.setHtml(data.getvalue().decode())


        except Exception as e:
            print(traceback.format_exc())
            print("buttonclicked", e)

    def button_clicked_next(self):
        try:
            if len(self.temp) != 0:
                String = "  ".join(map(str, self.temp[0]))
                self.how.append(String)
                del self.temp[0]
            else:
                self.how.append("도착")

        except Exception as e:
            print("next", e)
            print(traceback.format_exc())
    def button_back(self):
        try:
            self.close()
        except Exception as e:
            print("button_back", e)

