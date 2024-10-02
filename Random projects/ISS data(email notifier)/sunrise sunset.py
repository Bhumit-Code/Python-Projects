import requests
from datetime import datetime

My_lat = 48.762150
My_long = 11.425390
formatted = 0
parameters = {
    "lat": My_lat,
    "lng": My_long,
    "formatted": formatted
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)