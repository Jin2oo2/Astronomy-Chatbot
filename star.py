import time ## This module is learned from Youtube: https://youtu.be/VF2NtNnK9wM
def astronomyFact():
    print("This chatbot is specifically made for those, who have interest in astronomy ")
    time.sleep(2)
    print("Astronomy is the study of everything in the universe beyond Earth’s atmosphere ")
    time.sleep(2)
    print("That includes objects we can see with our naked eyes, like the Sun , the Moon , the planets, and the stars ")
    time.sleep(2)
    print("It also includes objects we can only see with telescopes or other instruments, like faraway galaxies and tiny particles ")
    time.sleep(2)
    print("And it even includes questions about things we can't see at all, like dark matter and dark energy")
    time.sleep(2)
    print("Today, We are talking about the various stars in astronomy.")
    time.sleep(2)

def star_theories():
    print("which star groups are you most interested in? ")
    time.sleep(2)
    print("There are some different stars : ")
    time.sleep(2)
    print("Alnitak")
    time.sleep(2)
    print("Rigel")
    time.sleep(2)
    print("Vega")
    time.sleep(2)
    print("Procyon")
    time.sleep(2)
    print("The Sun")
    time.sleep(2)
    print("Pollux")
    time.sleep(2)
    print("Betelgeuse")
    time.sleep(2)
    #All the information collected from here the Link: https://en.wikipedia.org/wiki/Stellar_classification
    s = input("Which star do you want to take information about? " )
    t = s.split()
    for a in t:
        if a=="Alnitak" or a=="alnitak" or a=="ALNITAK":
            print(" Class: O, Effective temperature: 30,000 K or more than 30,000 K")
            time.sleep(2)
            print("Vega-relative chromaticity: Blue, Chromaticity: Blue")
            time.sleep(2)
            print("Hydrogenlines: Weak, Fraction of all main-sequence stars: ~0.00003% ")
            time.sleep(2)
            print("Alnitak is a triple star system in the constellation of Orion. It has the designations ζ Orionis, which is Latinised to Zeta Orionis and abbreviated Zeta Ori or ζ Ori, and 50 Orionis, abbreviated 50 Ori.")
            time.sleep(2)
            print("The system is located at a distance of several hundred parsecs from the Sun and is one of the three main stars of Orion's Belt along with Alnilam and Mintaka.")
            time.sleep(2)
        elif a=="Rigel" or a=="rigel" or a=="RIGEL":
            print("Class: B, Effective temperature: 10,000 To 30,000 K")
            time.sleep(2)
            print("Vega-relative chromaticity: Blue White, Chromaticity: Deep Blue White")
            time.sleep(2)
            print("Hydrogenlines: Medium, Fraction of all main-sequence stars: 0.13% ")
            time.sleep(2)
            print("Rigel is a blue supergiant star in the constellation of Orion.  It has the Bayer designation β Orionis, which is Latinized to Beta Orionis and abbreviated Beta Ori or β Ori. Rigel is the brightest and most massive component and the eponym of a star system of at least four stars that appear as a single blue-white point of light to the naked eye")
            time.sleep(2)
            print("This system is located at a distance of approximately 860 light-years (260 pc) from the Sun.")
            time.sleep(2)
        elif a=="Vega" or a=="vega" or a=="VEGA":
            print("Class: A, Effective temperature: 7,500 To 10,000 K")
            time.sleep(2)
            print("Vega-relative chromaticity: White, Chromaticity: Blue White")
            time.sleep(2)
            print("Hydrogenlines: Strong, Fraction of all main-sequence stars: 0.6% ")
            time.sleep(2)
            print("Vega is the brightest star in the northern constellation of Lyra. It has the Bayer designation α Lyrae, which is Latinised to Alpha Lyrae and abbreviated Alpha Lyr or α Lyr. This star is relatively close at only 25 light-years (7.7 parsecs) from the Sun, and one of the most luminous stars in the Sun's neighborhood.")
            time.sleep(2)
            print("It is the fifth-brightest star in the night sky, and the second-brightest star in the northern celestial hemisphere, after Arcturus.")
            time.sleep(2)
        elif a=="Procyon" or a=="procyon" or a=="PROCYON":
            print("Class: F, Effective temperature: 6,000 To 7,500 K")
            time.sleep(2)
            print("Vega-relative chromaticity: Yellow White, Chromaticity: White")
            time.sleep(2)
            print("Hydrogenlines: Medium, Fraction of all main-sequence stars: 3% ")
            time.sleep(2)
            print("")
            time.sleep(2)
            print("")
            time.sleep(2)
        elif a=="The Sun" or a=="the sun" or a=="The sun" or a=="THE SUN" or a=="SUN" or a=="the Sun" or a=="the" or a=="sun" or a=="Sun":
            print("Class: G, Effective temperature: 5,200 To 6,000 K")
            time.sleep(2)
            print("Vega-relative chromaticity: Yellow, Chromaticity: Yellow Wish White")
            time.sleep(2)
            print("Hydrogenlines: Weak, Fraction of all main-sequence stars: 7.6% ")
            time.sleep(2)
            print("The Sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion reactions in its core. The Sun radiates this energy mainly as light, ultraviolet, and infrared radiation, and is the most important source of energy for life on Earth.")
            time.sleep(2)
            print("The Sun's radius is about 695,000 kilometers (432,000 miles), or 109 times that of Earth. The Sun has eight known planets orbiting around it respectively: four terrestrial planets (Mercury, Venus, Earth, and Mars), two gas giants (Jupiter and Saturn), and two ice giants (Uranus and Neptune )")
            time.sleep(2)
        elif a=="Pollux" or a=="pollux" or a=="POLLUX":
            print("Class: K, Effective temperature: 3,700 To 5,200 K")
            time.sleep(2)
            print("Vega-relative chromaticity: Light Orange, Chromaticity: Pale Yellow Orange")
            time.sleep(2)
            print("Hydrogenlines: Very Weak, Fraction of all main-sequence stars: 12.1% ")
            time.sleep(2)
            print("Pollux is the brightest star in the constellation of Gemini. It has the Bayer designation β Geminorum, which is Latinised to Beta Geminorum and abbreviated Beta Gem or β Gem.")
            time.sleep(2)
            print("This is an orange-hued, evolved giant star located at a distance of 34 light-years, making it the closest giant to the Sun. In 2006 an extrasolar planet (designated Pollux b or β Geminorum b, later named Thestias) was confirmed to be orbiting it.")
            time.sleep(2)
        elif a=="Betelgeuse" or a=="betelgeuse" or a=="BETELGEUSE":
            print("Class: M, Effective temperature: 2,400 To 3,700 K")
            time.sleep(2)
            print("Vega-relative chromaticity: Orange Red, Chromaticity: Light Orange Red")
            time.sleep(2)
            print("Hydrogenlines: Very Weak, Fraction of all main-sequence stars: 76.45% ")
            time.sleep(2)
            print("Betelgeuse is a red supergiant of spectral type M1-2 and one of the largest stars visible to the naked eye. It is usually the tenth-brightest star in the night sky and, after Rigel, the second-brightest in the constellation of Orion.")
            time.sleep(2)
            print("At near-infrared wavelengths, Betelgeuse is the brightest star in the night sky. Its Bayer designation is α Orionis, Latinised to Alpha Orionis and abbreviated Alpha Ori or α Ori.")
            time.sleep(2)
        
  
astronomyFact()
star_theories()