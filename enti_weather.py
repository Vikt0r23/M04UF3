#!/usr/bin/python3

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=41.4&longitude=2.12&current=temperature_2m,wind_speed_10m&hourly=temperature_2m"


weather_enti = requests.get(url)

w = weather_enti.json()

print("La temperatura es: "+str(w['current']['temperature_2m']))













