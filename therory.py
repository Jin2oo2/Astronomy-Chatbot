#chatbot code#
from time import sleep 
########################

#This is the link from where i learned about the time function
#https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/
########################
def astro_101():#shunkh's function

            print("Ahoy there young astronaut! let me teach you about astronomy!")
            sleep(4)
            print("We live on a blue planet called Earth which revolves around the young bright star called The Sun")
            sleep(4)
            print("Like the Earth there are 7 other planets who revolve around the sun")
            sleep(4)
            print("But! earth is the only planet, perfect enough to sustain life")
            sleep(4)
            print("The reason behind that.......")
            sleep(4)
            print("IS the goldilock's zone")
            sleep(4)
            print("In simple terms , it's the zone where the planet has the perfect temperature to sustain life")
            sleep(4)
            print("To spark your curiosity........")
            sleep(4)
            print("There are other planets like Earth!!")
            sleep(4)




def tHeories():
    print("Which theory fascinates you the most?")
    sleep(2)
    print("I can tell you about:")
    sleep(2)
    print("The Big Bang")
    sleep(2)
    print("Whcih tells us about how the universe came into being.....")
    sleep(2)
    print("The flat earth")
    sleep(2)
    print("Where people seem to think the earth is flat :)")
    sleep(2)
    print("The Big Splat")
    sleep(2)
    print("Which explains the end of the universe")
    sleep(2)
    print("Multiverse")
    sleep(2)
    print("It contemplates that there are multiple universes just like ours")
    l=input("What would you like to talk about? ")
    v=l.split()
    for i in v:
         if i=="Big" or i=="Bang" or i=="big" or i=="bang":
            print("All right young astronaut")
            sleep(2)
            print("So you have chosen to go to the beginning of everything......")
            sleep(2)
            print("Let me take you back 13.77 Billion years ago")
            sleep(2)
            print("Seems a lot doesn't it :)")
            sleep(4)
            print("Alright so in the beginning when there was nothing,when the universe was just matter and temperature")
            sleep(4)
            print("THE cosmic event happened")
            sleep(4)
            print("The temperature of the matter reached so high that the matter exploded and the universe came into being")
            sleep(4)
            print("Giving birth to all life and celestial objects that soon came to be known as planets and stars and galaxies and whatnot!!")
            sleep(4)
            print("That my friend is known as The Big Bang")
         if i=="Flat" or i=="Earth" or i=="flat" or i=="earth":
            print("All rightyy")
            sleep(3)
            print("Of all the sentient human beings on planet earth with access to NASA's feed and images")
            sleep(3)
            print("There exist some special warriors")
            sleep(3)
            print("Who have never seen out of a window of a plane")
            sleep(3)
            print("They believe that instead of an eliptical ball we live on a plate??")
            sleep(3)
            print("It's not really a theory ")
            sleep(3)
            print("Just an old belief held by the medieval europeans")
            sleep(3)
            print("And that's it")
         elif i=="splat" or i=="splat":
            print("Alright sir The Big Splat it is")
            sleep(3)
            print("A cold sad end")
            sleep(3)
            print("Every beginning has it's end")
            sleep(3)
            print("Scientists believe.....")
            sleep(3)
            print("Eventually all the galaxies would become so distant that there would be no exchange of heat and light")
            sleep(3)
            print("The stars would start dying....")
            sleep(3)
            print("The universe would become a cold and distant void of nothing")
            sleep(3)
            print("With the remains of it's former beauty and mysteries")
            sleep(3)
            print("The universe would come to it's end")
         elif i=="multiverse" or i=="Multiverse":
            print("Alrighty so you wanna talk variants")
            sleep(2)
            print("Let's Go")
            sleep(2)
            print("Astronomers believe that the universe we live in has copies of it defined by the choices of the billions of people that live on earth resulting in infinite earths and universes")
            sleep(3)
            print("For ex if your parents didn't meet you never came to exist thus creating another earth")
            sleep(4)
            print("This is just an assumption")
            sleep(3)
            print("What we trully believe in is that space is a very vast place ")
            sleep(3)
            print("It would be ignorant to think that the big bang resulted in only 1 universe") 
      
         
def GetDataOnPlanets():
    print("Which planet would you like to know about?")
    sleep(3)
    print("I can tell you about habitable planets like Earth ")
    sleep(3)
    print("I can tell you about the keplers")
    sleep(3)
    print("Like kepler 1649c,kepler 296e,kepler 1229b or kepler 442b")
    print("So......")
    sleep(3)
    x=input("So which planet would you like to talk about?")
    j=x.split()
    for c in j:
        if c=="1649c":
            ###https://en.wikipedia.org/wiki/Kepler-1649c
            print(" Kepler 1649c is an Earth-sized exoplanet likely rocky orbiting within the habitable zone of the red dwarf star Kepler-1649")
            sleep(3)
            print("It is located about 301 light-years (92 pc) away from Earth, in the constellation of Cygnus.")
            sleep(3)
            print("And that's it")
        elif c=="296e":
            ###https://en.wikipedia.org/wiki/Kepler-296e
            print("Kepler-296e also known by its Kepler Object of Interest designation KOI-1422.05) is a confirmed Earth-sized exoplanet orbiting within the habitable zone of Kepler-296.")
            sleep(3)
            print("Kepler-296e is a super-Earth with a radius 1.75 times that of Earth. The planet orbits Kepler-296 once every 34.1 days.")
            sleep(3)
            print("And that's it")
        elif c=="1229b":
            ###https://en.wikipedia.org/wiki/Kepler-1229b
            print("Kepler-1229b also known by its Kepler Object of Interest designation KOI-2418.01) is a confirmed super-Earth exoplanet")
            sleep(3)
            print("likely rocky, orbiting within the habitable zone of the red dwarf Kepler-1229, located about 870 light years ")
            sleep(3)
            print("And that's it")
        elif c=="442b":
            ###https://en.wikipedia.org/wiki/Kepler-1229b
            print("Kepler-442b (also known by its Kepler object of interest designation KOI-4742.01) is a confirmed near-Earth-sized exoplanet")
            sleep(3)
            print("Likely rocky, orbiting within the habitable zone of the K-type main-sequence star[6] Kepler-442, about 1,206 light-years (370 pc) from Earth in the constellation of Lyra.")
            sleep(3)
            print("That's it")
      
        
from time import sleep
def get_inp():
    print("What would you like to talk about?: ")
    sleep(2)
    print("I can teach you about constellations,other planets like the earth")
    sleep(2)
    print("Or i can give you a rookie talk on space,if that then just type in 101")
    sleep(2)
    print("Or we can talk about some interesting theories")
    sleep(5)
    x=input("What would you like to talk about?: ")
    y=x.split()
    for i in y:
        if i=="Astronomy" or i=="101":
            astro_101()
        elif i=="habitable" or i=="earth" or i=="planets" or i=="Planets":
            GetDataOnPlanets()
        elif i=="Theories" or "theories":
            tHeories()


# get_inp()









