# this part of the chatbot will provide some generic information about 8 planets in solar system.
import therory
import planet
import star


def get_planet_info(planet):
    distance_from_sun = {
        "Mercury": "58 million kilometers",
        "Venus": "108 million kilometers",
        "Earth": "150 million kilometers",
        "Mars": "228 million kilometers",
        "Jupiter": "778 million kilometers",
        "Saturn": "1.4 billion kilometers",
        "Uranus": "2.9 billion kilometers",
        "Neptune": "4.5 billion kilometers",
    }

    temperature = {
        "Mercury": "around 167 degrees Celsius",
        "Venus": "around 464 degrees Celsius",
        "Earth": "around 15 degrees Celsius",
        "Mars": "around -63 degrees Celsius",
        "Jupiter": "around -145 degrees Celsius",
        "Saturn": "around -178 degrees Celsius",
        "Uranus": "around -197 degrees Celsius",
        "Neptune": "around -201 degrees Celsius",
    }

    if planet in distance_from_sun and planet in temperature:
        return f"Here is some general information about the planet you asked for.\n {planet} is approximately {distance_from_sun[planet]} away from the Sun and has an average temperature of {temperature[planet]}. \n \nWould like to get some more information on any other planet? if not type 'exit'."
    else:
        return "I do apologive for that, I'm still learning to fetch more and more information. \nAt the moment, I don't have any information about that planet. Would you like to enter another planet name? "


def planet_astronomy():
    print("Hi, \nAs the Astronomy Chatbot, I can provide you well established information on planets in our solar system!,I can tell you about fascinating theories,stars and other habitable planets and if you don't know where to start,just type in 101! \nWhich planet would you feel like to learn about?")
    while True:
        user_input = input(">>> ").lower()
        if user_input == "exit":
            break
        elif user_input == "mercury":
            print(get_planet_info("Mercury"))
        elif user_input == "venus":
            print(get_planet_info("Venus"))
        elif user_input == "earth":
            print(get_planet_info("Earth"))
        elif user_input == "mars":
            print(get_planet_info("Mars"))
        elif user_input == "jupiter":
            print(get_planet_info("Jupiter"))
        elif user_input == "saturn":
            print(get_planet_info("Saturn"))
        elif user_input == "uranus":
            print(get_planet_info("Uranus"))
        elif user_input == "neptune":
            print(get_planet_info("Neptune"))
        elif user_input == '101':
            print(therory.astro_101())
        elif user_input=="theories" or user_input=='Theories':
            print(therory.tHeories())
        elif user_input=="habitable" or user_input=="Habitable":
            print(therory.tHeories())
        elif user_input=="greeting" or user_input=="Greeting" or user_input=="GREETING":
            print(star.astronomyFact())
        elif user_input=="stars" or user_input=="Stars" or user_input=="STARS":
            print(star.star_theories())
        elif user_input=="facts" or user_input=="Facts" or user_input=="FACTS":
            print(star.facts_astronomy())
        

        else:
            print("\nI'm sorry, I don't recognize that planet. Here is the list of 8 planets:\n \n Mercury \n Venus \n Earth \n Mars \n Jupiter \n Saturn \n Uranus \n Neptune \n \nTry enetering one of these planet names or type 'exit' to terminate.")

planet_astronomy()
