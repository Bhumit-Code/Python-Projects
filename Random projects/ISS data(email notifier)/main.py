import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

Longitude = response.json()["iss_position"]["longitude"]
Latitude = response.json()["iss_position"]["latitude"]
print(Longitude,Latitude)

