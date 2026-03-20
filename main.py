import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
my_api = os.environ.get("OWN_API")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TKN")

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
        thunderstorm = False
        rain = False
        light_rain = False
        fog = False
        snow = True
    elif 200 <= weatherper3 <= 232:
        thunderstorm = True
        rain = False
        light_rain = False
        fog = False
        snow = False
    elif 500 <= weatherper3 <= 531:
        thunderstorm = False
        rain = True
        light_rain = False
        fog = False
        snow = False
    elif 300 <= weatherper3 <= 321:
        thunderstorm = False
        rain = False
        light_rain = True
        fog = False
        snow = False
    elif 701 <= weatherper3 <= 781:
        thunderstorm = False
        rain = False
        light_rain = False
        fog = True
        snow = False
        
if snow:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+13185944642",
        body="❄️ Snow Alert ❄️\n\n"
                "Snow expected. Dress warmly and wear boots.\n"
                "Watch for slippery surfaces and keep warm. 🧤🧣",
        to="+962795466752"
    )
elif thunderstorm:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+13185944642",
        body="⛈ Thunderstorm Alert ⛈\n\n"
                "Thunderstorms expected today. Bring a strong jacket and stay indoors if possible.\n"
                "Avoid open areas and be careful of lightning. ⚡",
        to="+962795466752"
elif rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+13185944642",
        body="🌧 Rain Alert 🌧\n\n"
                "Rain expected. Bring a waterproof jacket and umbrella.\n"
                "Travel carefully and avoid puddles. ☔",
        to="+962795466752"
elif light_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+13185944642",
        body="🌦 Light Rain Alert 🌦\n\n"
                "Drizzle expected. Carry a light jacket or umbrella.\n"
                "Footwear with grip is recommended to avoid slipping. ☂️",
        to="+962795466752"
elif fog:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+13185944642",
        body="🌫 Visibility Alert 🌫\n\n"
                "Low visibility expected due to fog, haze, or dust.\n"
                "Drive carefully and watch your surroundings. 👀",
        to="+962795466752"
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+13185944642",
        body="☀️ Weather Update ☀️\n\n"
                "No rain expected. Wear your usual clothes and enjoy the day! 😎",
        to="+962795466752"
    )
print(message.status)


