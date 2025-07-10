from email.message import EmailMessage
import smtplib
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")


# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
url = "https://www.amazon.com/gp/product/B0D73MPT6L/ref=ox_sc_act_title_1?smid=AOWJ428WVPZ9P&th=1"


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
price_as_float = float(price.split("$")[1])

product_title = soup.find(id="productTitle").get_text().strip()

target_price = 15

if price_as_float < target_price:
    message_body = f"{product_title} is now {price}\n{url}"

    msg = EmailMessage()
    msg["Subject"] = "Amazon Price Alert!"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg.set_content(message_body)

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.send_message(msg)

    print("Email sent!")
else:
    print(f"Price is still above ${target_price}.")
