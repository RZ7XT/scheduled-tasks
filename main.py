import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
my_api = os.environ.get("OWN_API")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TKN")

client = Client(account_sid, auth_token)

# 32.040917
# 35.931787
params = {
    "lat": 32.040917,
    "lon": 35.931787,
    "appid": my_api,
    "cnt": 4,
}

response = requests.get(url=OWN_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()


id_list = []

thunderstorm = False
rain = False
light_rain = False
fog = False
snow = False

for three_hour_window in range(3):
    id_num = weather_data["list"][three_hour_window]["weather"][0]["id"]
    id_list.append(id_num)

for weatherper3 in id_list:
    if 600 <= weatherper3 <= 622:
        snow = True
    elif 200 <= weatherper3 <= 232:
        thunderstorm = True
    elif 500 <= weatherper3 <= 531:
        rain = True
    elif 300 <= weatherper3 <= 321:
        light_rain = True
    elif 701 <= weatherper3 <= 781:
        fog = True

# Send one message based on priority
if thunderstorm:
    body = "⛈ Thunderstorm Alert ⛈\n\nThunderstorms expected today. Bring a strong jacket and stay indoors if possible.\nAvoid open areas and be careful of lightning. ⚡"
elif snow:
    body = "❄️ Snow Alert ❄️\n\nSnow expected. Dress warmly and wear boots.\nWatch for slippery surfaces and keep warm. 🧤🧣"
elif rain:
    body = "🌧 Rain Alert 🌧\n\nRain expected. Bring a waterproof jacket and umbrella.\nTravel carefully and avoid puddles. ☔"
elif light_rain:
    body = "🌦 Light Rain Alert 🌦\n\nDrizzle expected. Carry a light jacket or umbrella.\nFootwear with grip is recommended to avoid slipping. ☂️"
elif fog:
    body = "🌫 Visibility Alert 🌫\n\nLow visibility expected due to fog, haze, or dust.\nDrive carefully and watch your surroundings. 👀"
else:
    body = "☀️ Weather Update ☀️\n\nNo rain expected. Wear your usual clothes and enjoy the day! 😎"

message = client.messages.create(
    from_="+13185944642",
    body=body,
    to="+962795466752"
)
print(message.status)



