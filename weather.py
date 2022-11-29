import requests,json
apiKey = "8a3b627677918db38cedf281fd6f94c6" #openweathermap 이라는 API를 받아옴. 날씨정보 등을 받아올 수 있음.
lang = "kr"                                 #언어
units = "metric"                            #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)                  #requsets라이브러리로 api 원격 호출
result = json.loads(result.text)            #원격 호출한것을 JSON을 이용하여 파이썬 형태로 변환

name = result['name']                   #지역이름
lon = result['coord']['lon']            #경도
lat = result['coord']['lat']            #위도
weather = result['weather'][0]['main']  #날씨
temperature = result['main']['temp']    #온도
humidity = result['main']['humidity']   #습도
