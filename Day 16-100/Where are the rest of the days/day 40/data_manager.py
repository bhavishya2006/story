import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


load_dotenv()

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, auth=self._authorization)
        data = response.json()
        pprint(data)
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, auth=self._authorization)
        data = response.json()
        pprint(data)
        self.customer_data = data["formResponses2"]
        return self.customer_data
