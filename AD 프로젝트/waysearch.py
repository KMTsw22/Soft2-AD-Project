# *-- Geocoding 활용 코드 --*
import json
import urllib
from urllib.request import Request, urlopen

# *-- 3개의 주소 geocoding으로 변환한다.(출발지, 도착지, 경유지) --*

# 주소에 geocoding 적용하는 함수를 작성.
def get_location(loc):
    client_id = 'nx8qe8tkiq'
    client_secret = 'LgsS28y7H6HD7iw6OlhViTBsmYAELvKEb1yuleDD'
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=" \
          + urllib.parse.quote(loc)

    # 주소 변환
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)

    response = urlopen(request)
    res = response.getcode()
    Error = "Error"
    if (res == 200):  # 응답이 정상적으로 완료되면 200을 return한다
        response_body = response.read().decode('utf-8')
        response_body = json.loads(response_body)
        #이상한 값이 들어올경우
        if response_body["status"] == "INVALID_REQUEST":
            return Error
        # 주소가 존재할 경우 total count == 1이 반환됨.
        if response_body['meta']['totalCount'] == 1:
            # 위도, 경도 좌표를 받아와서 return해 줌.
            lat = response_body['addresses'][0]['y']
            lon = response_body['addresses'][0]['x']
            return (lon, lat)
        else:
            return Error

    else:
        return Error


option = ""

def get_optimal_route(start, goal, option=option):
    client_id = 'nx8qe8tkiq'
    client_secret = 'LgsS28y7H6HD7iw6OlhViTBsmYAELvKEb1yuleDD'
    # start=/goal=/(waypoint=)/(option=) 순으로 request parameter 지정
    url = f"https://naveropenapi.apigw.ntruss.com/map-direction-15/v1/driving? \
    start={start[0]},{start[1]}&goal={goal[0]},{goal[1]}"
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)

    response = urllib.request.urlopen(request)
    res = response.getcode()

    if (res == 200):
        response_body = response.read().decode('utf-8')
        return json.loads(response_body)

    else:
        return Error
