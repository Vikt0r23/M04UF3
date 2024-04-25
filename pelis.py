#!/usr/bin/python3

import requests

url = "https://search.imdbot.workers.dev/"



title = input ("Introduce el titulo de la pelicula")

url = url + '/?q=' + title

film = requests.get(url)

fi = film.json()

print(f"Titulo: ", fi['descripcion'][0]['#TITLE'], '\n', fi['descripcion'][0]['#YEAR'])








