import requests,json
city = "Daegu" #도시
apiKey = "8a3b627677918db38cedf281fd6f94c6"
lang = "kr" #언어
units = "metric" #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)
#print(result)

name = result['name']
lon = result['coord']['lon']  #경도
lat = result['coord']['lat']  #위도
weather = result['weather'][0]['main'] #날씨
temperature = result['main']['temp'] #온도
humidity = result['main']['humidity'] #습도


# print(name)
# print(lon, ', ', lat)
# print(weather)
# print(temperature)
# print(humidity)