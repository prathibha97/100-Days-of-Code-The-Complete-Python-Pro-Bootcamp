from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        '<h1 style="text-align: center">Hello, World!</h1>'
        "<p>This is a paragraph</p>"
        '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzRhd3d2cXQwMTJ4enVpMDE1cWc2NHRuMzEybHRjMjNjMGcyaHN6diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/gKHGnB1ml0moQdjhEJ/giphy.gif"/>'
    )


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye!"


@app.route("/<path:name>/<int:age>")
def greet(name, age):
    return f"Greetings, {name}!, Your age is {age}"


if __name__ == "__main__":
    app.run()
