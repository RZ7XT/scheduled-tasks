import os
import requests
from dotenv import load_dotenv

load_dotenv(r"C:\Users\Qusai Balaawi\PycharmProjects\.env.txt")


class DataManager:
    def __init__(self):

        self.SHEETY_BEARER = os.environ.get("FD_SHEETY_BEARER")
        self.sheety_url = "https://api.sheety.co/ad3d56f727b1cc13a3c5387c56d7f9e5/copyOfFlightDeals/prices"
        self.authorization = {
            "Authorization": f"Bearer {self.SHEETY_BEARER}"
        }
        self.prices_data = {}

    def get_destination_data(self):
        response = requests.get(self.sheety_url, headers=self.authorization)
        data = response.json()
        self.prices_data = data["prices"]

        return self.prices_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(f"{self.sheety_url}/{row_id}", json=new_data, headers=self.authorization)
