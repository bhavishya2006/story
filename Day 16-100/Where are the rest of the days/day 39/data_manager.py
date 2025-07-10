import requests
from requests.auth import HTTPBasicAuth
import env  # your env.py

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c4ddfcd4a2a2597483ac168cf042ecc9/untitledSpreadsheet/sheet1"


class DataManager:

    def __init__(self):
        self._user = env.SHEETY_USERNAME
        self._password = env.SHEETY_PASSWORD
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        print("Full JSON response:", data)  # Debug
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {  # Wrap inside root 'sheet1' per Sheety requirement
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
