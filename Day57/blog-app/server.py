import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/blog")
def blog():
    blog_url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<blog_id>")
def post(blog_id):
    blog_url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    post = [post for post in all_posts if post["id"] == int(blog_id)]
    return render_template("post.html", post=post[0])


if __name__ == "__main__":
    app.run(debug=True)
