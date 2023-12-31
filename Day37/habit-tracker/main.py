import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.environ["TOKEN"],
    "username": os.environ["USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.environ['USERNAME']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": os.environ["TOKEN"]
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{os.environ['USERNAME']}/graphs/graph1"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{os.environ['USERNAME']}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{os.environ['USERNAME']}/graphs/graph1/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)