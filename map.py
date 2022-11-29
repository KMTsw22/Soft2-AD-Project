import folium                           #지도를 나타내기 위한 라이브러리
import waysearch                        #길찾기 기능을 실행하기 위한 함수들을 묶어놓은곳
from PyQt5.QtWidgets import *
from PyQt5 import uic                   #designer로 만든 ui를 이용하기 위함
import io                               #
import traceback
form_mapwindow = uic.loadUiType("mapwindow.ui")[0]       #map ui 호출

class MapWindow(QDialog, QWidget, form_mapwindow):
    def __init__(self):
        super(MapWindow, self).__init__()
        self.initUI()                           #initUI 함수 실행

    def initUI(self):
        try:
            self.setupUi(self)                                          #UI 보여줌
            self.address.clicked.connect(self.buttonClicked)            #address(주소입력) 버튼 클릭시 buttoncliked함수 실행
            self.nextbutton.clicked.connect(self.button_clicked_next)   #next버튼 클릭시 button_clicked_next 함수 실행
            self.Backbutton.clicked.connect(self.button_back)           #Back버튼 클릭시 button_back 함수 실행
        except Exception as e:
            print("initUi", e)

    def buttonClicked(self):
        try:
            self.how.clear()                   #네비게이션 길찾기 나오는 곳 초기화
            start = self.startplace.text()     #출발주소에 입력되어있는 텍스트(도로명주소)가 출발지점
            goal = self.goalplace.text()       #도착주소에 입력되어있는 텍스트(도로명주소)가 도착지점
            # print(len(start), start)
            # print(len(goal), goal)

            start = waysearch.get_location(start) # 출발좌표
            goal = waysearch.get_location(goal) #도착좌표
            if start == "Error" or goal =="Error":               #만약 출발좌표나 도착좌표가 없는경우, 오류난경우
                self.ErrorText.setText("Error: 위치 정보가 잘못되었습니다")
                return True #함수 종료하기 위함
            #print(start)
            results = waysearch.get_optimal_route(start, goal)   #result는 거리, 소요시간, 꺽는지점에 대한 포인트, 포인트까지 가는 길 등이 나와있음.
            # *-- 목적지까지의 guidence와 각각의 거리, 소요시간 정보 추출 --*
            self.temp = [(guide['instructions'], guide['distance'], guide['duration'] / 1000) \
                         for guide in results['route']['traoptimal'][0]['guide']] # 그중 우리는 목적지까지의 안내, 각각의 거리, 소요시간 만 필요.

            self.start_func = start     #출발지점에 마크를 찍기 위한 좌표 얻어놓음
            self.goal_func = goal       #도착지점에 마크를 찍기 위한 좌표 얻어놓음
            m2 = folium.Map(location=[float(self.start_func[1]), float(self.start_func[0])],
                            zoom_start=14,
                            )       #출발지점을 기준으로 지도 생성 zoom_start 는 확대 배율을 의미함.
            # 출발 마커 파랑
            folium.Marker([float(self.start_func[1]), float(self.start_func[0])], icon=folium.Icon(color = "blue"),
                          popup=f'<div style="width:300px;">Start: {start}</div>').add_to(m2)  # 마커 찍고싶은 좌표를 찍음. popup은 마커에 마우스 올려놓을시 그 위치를 나타내기위함.
            # 도착 마커 빨강

            folium.Marker([float(self.goal_func[1]), float(self.goal_func[0])], icon=folium.Icon(color = "red"),
                          popup=f'<div style="width:300px;">Goal: {goal}</div>').add_to(m2)   # popup은 마커에 마우스 올려놓을시 그 위치를 나타내기위함.

            # 지도 데이터를 저장하기 위한것들 (인터넷을 통해서 알게되었음.) 잘 이해가 되지는 않으나 조사해봄.
            data = io.BytesIO()                 #바이트데이터를 DATA에 저장
            m2.save(data, close_file=False)     #받아온 바이트 데이터를 저장

            self.webview.setHtml(data.getvalue().decode())


        except Exception as e:
            print(traceback.format_exc())
            print("buttonclicked", e)

    def button_clicked_next(self):                              #next 함수를 눌렀을떄 실행 되는 함수
        try:
            if len(self.temp) != 0:                             #받아온 네비게이션 정보가 있다면:
                String = "  ".join(map(str, self.temp[0]))      #temp[0]은 가이드 의미
                self.how.append(String)                         #how라는 textEdit에 입력
                del self.temp[0]                                #사용한 temp[0]는 삭제
            else:
                self.how.append("도착")                          #만약 temp에 남은 정보가 없다면 "도착"을 출력

        except Exception as e:
            print("next", e)
            print(traceback.format_exc())
    def button_back(self):                                      #Back 버튼을 눌렀을때 실행되는 함수
        try:
            self.close()                                        #즉시 그 창을종료
        except Exception as e:
            print("button_back", e) 