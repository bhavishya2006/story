# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper
#
# def make_underlined(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#     return wrapper

from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
