from flask import Flask, render_template, request
import smtplib
import os
from dotenv import load_dotenv
import requests

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        email_message = f"Subject: New Contact Form Submission\n\n" \
                        f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=email_message.encode("utf-8")
                )
            return render_template("contact.html", msg_sent=True)
        except Exception as e:
            print(f"Failed to send email: {e}")
            return render_template("contact.html", msg_sent=False)

    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = next((post for post in posts if post["id"] == index), None)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
