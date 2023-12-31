import requests
import smtplib
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall?"
api_key = os.environ.get("OWM_API_KEY")
print(api_key)

MY_EMAIL = "prathibha@gmail.com"
MY_PASSWORD = "tiqfiacjuvsfbmw"

params = {
    "lat": 7.2955,
    "lon": 80.6356,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=params)
response.raise_for_status()

weather_data = response.json()
# get first 12 dictionaries
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Weather Alert\n\nMake sure to bring an umbrella"
        )
