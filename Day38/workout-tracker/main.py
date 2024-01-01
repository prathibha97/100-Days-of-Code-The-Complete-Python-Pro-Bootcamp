import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.environ["SHEETY_ENDPOINT"]

GENDER = "Male"
WEIGHT_KG = 60
HEIGHT_CM = 169
AGE = 26

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

body = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=API_ENDPOINT, headers=headers, json=body)
exercises = response.json()["exercises"]
today = datetime.now()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety API Call & Authentication
for exercise in exercises:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    
    print(f"Sheety Response: \n {sheet_response.text}")
