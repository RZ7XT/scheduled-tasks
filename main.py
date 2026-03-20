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

umbrella = False

for three_hour_window in range(3):
    id_num = weather_data["list"][three_hour_window]["weather"][0]["id"]
    id_list.append(id_num)

for weatherper3 in id_list:
    if weatherper3 < 700:
        umbrella = True

if umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+14155238886",
        body="It's going to rain in school, make sure to bring a jacket. 🧥",
        to="+962795466752"
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's NOT going to rain in school, feel free to wear whichever you want. 😉",
        to="whatsapp:+962795466752"
    )
print(message.status)


