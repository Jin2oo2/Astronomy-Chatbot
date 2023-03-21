import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()
API_KEY = os.environ['API_KEY']

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

def getPlanet(planet):
    """Return given planet information"""
    planet = planet.capitalize()
    url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(planet)
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
    return response.text

def getRandomPlanet():
    planet = planets[random.randint(0, len(planets)-1)]
    return getPlanet(planet)

#print(getRandomPlanet())

#print(getPlanet('Earth'))                                