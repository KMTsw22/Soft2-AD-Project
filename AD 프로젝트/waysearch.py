# *-- Geocoding 활용 코드 --*
import json
import urllib
from urllib.request import Request, urlopen     #URL을 가져오기 위한 파이썬 모듈

def get_location(loc):                        #위도, 경도를 알아오기 위한 함수 (위도, 경도를 리턴) 참조한 API는 Naver open api
    client_id = 'nx8qe8tkiq'                                                            #API id
    client_secret = 'LgsS28y7H6HD7iw6OlhViTBsmYAELvKEb1yuleDD'                          #API 코드
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=" \
          + urllib.parse.quote(loc) #API

    # 주소 변환
    request = urllib.request.Request(url)       #모든 URL 스킴을 처리하기 위해 Request 인터페이스 사용. “http://”, “ftp://”, “market://”과 같은 문자열을 url scheme이라 부릅니다.
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)     #웹서버에 클라이언트 ID 보냄
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)    #웹서버에 클라이언트 암호 보냄

    response = urlopen(request)     #이제 URL 오픈 가능
    res = response.getcode()        #만약 주소가 제대로 입력이 되었다면 200이 저장됨
    Error = "Error"
    if (res == 200):                                            # 응답이 정상적으로 완료되면 200을 return한다
        response_body = response.read().decode('utf-8')
        response_body = json.loads(response_body)
        if response_body["status"] == "INVALID_REQUEST":        #이상한 status에 "OK"가 아니라 이상한 값이 들어온경우
            return Error
        # 주소가 존재할 경우 total count == 1이 반환됨.
        if response_body['meta']['totalCount'] == 1:    #검색해보니 해당 문서에 대한 정보인 메타데이터(metadata) 라고함
            lat = response_body['addresses'][0]['y']
            lon = response_body['addresses'][0]['x']
            return (lon, lat)                           #위도, 경도 좌표를 받아와서 return 해줌
        else:
            return Error                                #주소가 없는경우

    else:
        return Error                                    #응답되지 않는경우

option = ""

def get_optimal_route(start, goal, option=option):                  #길안내를 위한 함수
    client_id = 'nx8qe8tkiq'                                        #클라이언트 id
    client_secret = 'LgsS28y7H6HD7iw6OlhViTBsmYAELvKEb1yuleDD'      #클라이언트 암호
    # start=/goal=/(waypoint=)/(option=) 순으로 request parameter 지정
    url = f"https://naveropenapi.apigw.ntruss.com/map-direction-15/v1/driving? \
    start={start[0]},{start[1]}&goal={goal[0]},{goal[1]}"           #시작 (위도,경도)   도착 (위도,경도)
    request = urllib.request.Request(url)                           #모든 URL 스킴을 처리하기 위해 Request 인터페이스 사용.
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)         #웹에 id 보냄
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)        #웹에 암호 보냄

    response = urllib.request.urlopen(request)                      #URL 오픈
    res = response.getcode()                                        #정상적으로 실행된다면 200을 저장

    if (res == 200):
        response_body = response.read().decode('utf-8') #URL에서 받아온것을 utf-8형식의 byte코드를 문자열로 변환.
        return json.loads(response_body)                #JSON 형식의 결과 데이터는 json.loads() 메소드를 통해서 파이썬에서 활용 가능한 객체 (예: dict) 로 변환하여 사용한다.

    else:
        return "Error"                                  #정상적으로 응답하지 못한경우 에러
