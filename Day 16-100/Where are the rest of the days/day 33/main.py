import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "bhavishyanarravula@gmail.com"
MY_PASSWORD = "vruofmqisbimoupv"
MY_LAT = 42.736980  # Your latitude
MY_LONG = -84.483698  # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS Position → Lat: {iss_latitude}, Long: {iss_longitude}")

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        print(" ISS is overhead!")
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour  # Should use UTC to match API

    print(f"Sunrise at {sunrise}, Sunset at {sunset}, Now (UTC): {time_now}")

    if time_now >= sunset or time_now <= sunrise:
        print("🌑 It's currently dark!")
        return True
    return False

while True:
    time.sleep(60)
    print("Checking conditions...")
    if is_iss_overhead() and is_night():
        print("Sending email...")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky!"
            )
        print("Email sent!")
