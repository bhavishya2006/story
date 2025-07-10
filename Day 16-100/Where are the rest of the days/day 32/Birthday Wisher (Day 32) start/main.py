# #dxbp foxg wrqf yjst
#
# import smtplib
#
# my_email = "bhavishyanarravula@gmail.com"
# app_password = "dxbpfoxgwrqfyjst"
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=app_password)
#
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="narravulabhavishya@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )

import datetime
import random
import smtplib
from email.mime.text import MIMEText

today = datetime.datetime.now().strftime("%A")

with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

quote = random.choice(quotes)

sender_email = "bhavishyanarravula@gmail.com"
receiver_email = "narravulabhavishya@gmail.com"
password =  "dxbpfoxgwrqfyjst"

subject = f"Motivational Quote for {today}"
body = f"{quote}\n\nHave a great {today}!"

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print(" Email sent successfully.")
except Exception as e:
    print(f"Error sending email: {e}")

