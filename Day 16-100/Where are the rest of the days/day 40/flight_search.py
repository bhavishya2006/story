import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

print(f"AMADEUS_API_KEY = {os.getenv('AMADEUS_API_KEY')}")
print(f"AMADEUS_SECRET = {os.getenv('AMADEUS_SECRET')}")

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def __init__(self, debug=False):
        self.debug = debug
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]

        if self.debug:
            print(f"[DEBUG] API Key: {self._api_key}")
            print(f"[DEBUG] API Secret: {self._api_secret}")


        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)

        if self.debug:
            print(f"[DEBUG] Token request status code: {response.status_code}")
            print(f"[DEBUG] Token response: {response.text}")

        response.raise_for_status()

        token = response.json()['access_token']
        expires_in = response.json().get('expires_in', 'unknown')

        if self.debug:
            print(f"[DEBUG] Your token is {token}")
            print(f"[DEBUG] Your token expires in {expires_in} seconds")

        return token

    def get_destination_code(self, city_name):
        if self.debug:
            print(f"[DEBUG] Using this token to get destination code: {self._token}")

        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=params
        )

        if self.debug:
            print(f"[DEBUG] Status code {response.status_code}. Response: {response.text}")

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {"Authorization": f"Bearer {self._token}"}
        # nonStop must be "true" or "false" string. Python booleans won't work
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "USD",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=params,
        )

        if self.debug:
            print(f"[DEBUG] check_flights() response status code: {response.status_code}")
            print(f"[DEBUG] Response body: {response.text}")

        if response.status_code != 200:
            print("There was a problem with the flight search.")
            print("Check the API documentation for details on status codes:")
            print("https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference")
            return None

        return response.json()
