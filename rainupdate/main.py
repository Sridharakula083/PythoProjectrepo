import requests

OWM_Endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"

api_key = "8ffb625b1660019bd67606fda5854add"

weather_params = {
    "lat": 18.112436,
    "lon": 79.019302,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
