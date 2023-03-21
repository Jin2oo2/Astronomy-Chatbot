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

    planetInfo = ''
    if response.status_code == requests.codes.ok:
        parsed = response.json()[0]
        planetInfo = 'Name: ' + parsed['name'] + '\n' + 'Mass: ' + str(parsed['mass']) + 'x10^27kg\n' + 'Orbital period: ' + str(parsed['period']) + ' days\n' + 'Temperature: ' + str(round(parsed['temperature']-273.15, 2)) + '°C\n' + 'Distance from Earth: ' + str(parsed['distance_light_year']) + ' light years\n'
    else:
        planetInfo = 'Could not find the planet...'

    return planetInfo

def getRandomPlanet():
    planet = planets[random.randint(0, len(planets)-1)]
    return getPlanet(planet)

#print(getRandomPlanet())

#print(getPlanet('Earth'))                                