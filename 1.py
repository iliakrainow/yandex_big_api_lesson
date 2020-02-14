import os
import pygame
import requests
from PIL import Image
from io import BytesIO
from toponym_envelope import get_toponym_envelope


size = width, height = 600, 500
screen = pygame.display.set_mode(size)


toponym_to_find = "Москва, ул. Академика Королева 12"

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json",
}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
    "GeoObject"
]


ll, spn = get_toponym_envelope(toponym)
map_params = {"ll": ll, "spn": spn, "l": "map"}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
pygame.init()

file = open("1.png", "wb")
file.write(response.content)
file.close()
screen.blit(pygame.image.load("1.png"), (0, 50))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
