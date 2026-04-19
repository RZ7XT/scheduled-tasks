import requests
import os

class NotificationManager:

    def __init__(self):
        self.BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.BOT_CHAT_ID = os.environ.get("TELEGRAM_BOT_CHAT_ID")

    def send_telegram_message(self, message):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage?chat_id={self.BOT_CHAT_ID}&text={message}"
        response = requests.get(url)
        return response.json()
