import requests
from datetime import datetime
import os


GENDER = "female"
WEIGHT_KG = 55
HEIGHT_CM = 175
AGE = 18

APP_ID = "a2fa1ee5"
API_KEY = "7d3c059d0c1437f1a2f93f29ea0065fa"

sheet_endpoint = "https://api.sheety.co/9ed470e51988f7d967b8478c10d9756b/workout/sheet1"
basic_auth_token = "YmhhdmlzaHlhMjgxMDpOYXJyQDI4MTA="
exercise_text = input("Tell me which exercises you did: ")

# Headers for Nutritionix
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": f"Basic {basic_auth_token}"
}

for exercise in result.get("exercises", []):
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_headers)
    print(sheet_response.text)
