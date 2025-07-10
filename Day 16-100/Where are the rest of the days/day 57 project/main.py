from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get("https://api.npoint.io/bfbb5126bd58434d4e99")

post_objects = []

if response.status_code == 200:
    data = response.json()
    print(data)
    posts = data

    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
else:
    print("Failed to fetch posts. Status code:", response.status_code)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = next((post for post in post_objects if post.id == index), None)
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
