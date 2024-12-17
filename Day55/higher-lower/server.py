from random import randint

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    )


@app.route("/<int:guessed_number>")
def guess(guessed_number):
    random_number = randint(0, 9)
    if guessed_number > random_number:
        return (
            "<h2 style='color: purple'>Too high, try again!</h2>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
        )

    elif guessed_number < random_number:
        return (
            "<h1 style='color: red'>Too low, try again!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
        )
    else:
        return (
            "<h2 style='color: green'>You found me!</h2>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
        )


if __name__ == "__main__":
    app.run()
