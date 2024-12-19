import datetime
from random import randint

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", random_number=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    genderResponse = requests.get(gender_url)
    gender_data = genderResponse.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    ageResponse = requests.get(age_url)
    age_data = ageResponse.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
