import requests
from datetime import datetime
import env

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:

    def __init__(self):
        self._api_key = env.AMADEUS_API_KEY
        self._api_secret = env.AMADEUS_SECRET
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        data = response.json()
        print("Token response:", data)

        if 'access_token' in data and 'expires_in' in data:
            print(f"Your token is {data['access_token']}")
            print(f"Your token expires in {data['expires_in']} seconds")
            return data['access_token']
        else:
            raise Exception(f"Failed to get access token. Response: {data}")

    def get_destination_code(self, city_name):
        print(f"Using token {self._token} to get destination {city_name}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        print(f"Status code {response.status_code}. Response: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            print(f"Airport IATA code not found for {city_name}. Returning 'N/A'.")
            return "N/A"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "USD",
            "max": "10",
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            print(f"Flight search failed with status code: {response.status_code}")
            print("Response:", response.text)
            return None

        return response.json()
