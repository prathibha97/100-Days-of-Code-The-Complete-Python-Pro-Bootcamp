from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

news = soup.find_all(class_="titleline")
for heading in news:
    print(heading.find(name="a").get("href"))
    print(heading.find(name="a").getText())

scores = soup.find_all(class_="score")
for score in scores:
    print(score.getText().split(" ")[0])

