import os
import requests


class DataManager:
    def __init__(self):

        self.SHEETY_BEARER = os.environ.get("FD_SHEETY_BEARER")
        self.sheety_url = "https://api.sheety.co/a48f21f851b75862d9bc81bc6d5cfc39/qusai'sFlightTwin/prices"
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
