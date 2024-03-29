### This module is learned from Youtube: https://youtu.be/VF2NtNnK9wM
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
    print("Today, We are talking about the various stars and different facts about astronomy.")
    time.sleep(2)

 #########################################################################################
    #All the information collected from here the Link: https://en.wikipedia.org/wiki/Stellar_classification
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
##########################################################################
# all the above information from here : https://en.wikipedia.org/wiki/Stellar_classification        
###########################################################################
# These information got from here: https://seedscientific.com/astronomy-statistics/   
def facts_astronomy():
    print("Hey Guys, If I give you more data on facts of Astronomy, ")
    time.sleep(2)
    print("There are some facts, Which is very important for your astronomy knowledge and You should know about this.")
    time.sleep(2)
    print("What facts do you want to know?: ")
    time.sleep(2)
    print("Our solar system history")
    time.sleep(2)
    print("The largest asteroid in our solar system—Ceres")
    time.sleep(2)
    print("The North Star")
    time.sleep(2)
    print("Temperatures on Venus")
    time.sleep(2)
    print("One light year")
    time.sleep(2)
    print("types of galaxies: spiral, elliptical, and irregular")
    time.sleep(2)
    print("Halley’s comet")
    time.sleep(2)
    print("Hubble Space Telescope")
    time.sleep(2)
    p = input("Which facts are you most interested in knowing about? ")
    g = p.split()
    for fact in g:
        if fact=="Our solar system history" or fact=="solar system" or fact=="history of solar system" or  fact=="SOLAR SYSTEM" or fact=="History" or fact=="HISTORY OF SOLAR SYSTEM" or fact=="Solar system":
            print("Our solar system is about 4.5 billion years old.")
            time.sleep(2)
            print("The universe we call home is located in an outer spiral arm of the Milky Way galaxy. It consists of our star, the Sun, and everything bound to its gravity, such as the planets, moons, asteroids, comets, and meteoroids.")
            time.sleep(2)
            print("Various astronomy facts and information indicate that our solar system formed from a dense cloud of interstellar gas and dust.")
            time.sleep(2)
            print("Once the cloud collapsed, possibly due to a supernova of a nearby exploding star, it formed a solar nebula — the swirling disk of material. The gravity at the center pulled more and more material in, and eventually, our Sun was born.")
            time.sleep(2)
        elif fact == "The largest asteroid in our solar system—Ceres" or fact=="The largest asteroid " or fact=="Ceres" or fact=="solar system—Ceres " or fact=="The largest asteroid in our solar system—Ceres" or fact=="CERES" or fact=="THE LARGEST ASTEROID" :
            print("he largest asteroid in our solar system—Ceres—has a diameter of 580 miles (940 km).")
            time.sleep(2)
            print("In 1801, Giuseppe Piazzi discovered Ceres in the main asteroid belt between Mars and Jupiter. The asteroid contains roughly one-third of the entire asteroid belt’s mass.")
            time.sleep(2)
            print("Facts about our solar system show that Ceres is the only dwarf planet inside Neptune’s orbit and the largest object in the main asteroid belt.")
            time.sleep(2)
        elif fact=="The North Star" or fact=="the north star" or fact=="THE NORTH STAR" or fact=="star" or fact=="STAR" or fact=="thenorthstar" or fact=="thenorth":
            print("The North Star changes every 26,000 years.")
            time.sleep(2)
            print("Earth’s axis goes through a process known as precession — a change in the orientation of a rotating body’s rotational axis.")
            time.sleep(2)
            print("Because of that, our perception of the north gradually shifts to different stars over a 26,000-year cycle.")
            time.sleep(2)
            print("Our ancestors began understanding astronomy millennia ago and used the North Star for navigation. Several thousand years ago, Vega was the North Star, and it will gain that status again in around 12,000 years. However, in 26,000 years, Polaris will return to its original position as the Earth’s polar star.")
            time.sleep(2)
        elif fact=="Temperatures on Venus" or fact=="TEMPERATURES ON VENUS" or fact=="Temperatures" or fact=="Venus" or fact=="VENUS" or fact=="TEMPERATURE":
            print("emperatures on Venus reach 880 degrees Fahrenheit (471 °C).")
            time.sleep(2)
            print("Even though Mercury is the closest planet to the Sun, Venus is the hottest planet in our solar system. Various astronomer facts and observations show that Mercury’s temperature varies from the extreme 800 degrees Fahrenheit (430 °C) during the day to -290 degrees Fahrenheit (-180 °C) at night.")
            time.sleep(2)
            print("However, Venus has many gasses in its atmosphere that create a greenhouse effect and trap heat, keeping it at a cozy 880 degrees Fahrenheit (471 °C).")
            time.sleep(2)
            print("Believe it or not, according to research by NASA’s Goddard Institute for Space Studies, Venus might have been habitable early in its history.")
            time.sleep(2)
        elif fact=="One light year" or fact=="light year" or fact=="ONE LIGHT YEAR" or fact=="LIGHT YEAR" or fact=="light" or fact=="LIGHT" or fact=="onelightyear":
            print("One light-year is about 6 trillion miles (9 trillion km).")
            time.sleep(2)
            print("Scientists from various fields of astronomy use light-years to measure the distance between celestial objects. It is the distance light travels in an Earth year.")
            time.sleep(2)
            print("Light travels at a speed of 186,000 miles per second (300,000 km/s), and one light-year is about 6 trillion miles (9 trillion km). Since light needs so much time to reach us, whenever we are looking at celestial objects, we see them in the past.")
            time.sleep(2)
            print("For example, the Sun is 8.3 light minutes away from us, so each time we look at it, we always see it as it was 8.3 minutes ago.")
            time.sleep(2)
        elif fact=="types of galaxies: spiral, elliptical, and irregular" or fact=="galaxies" or fact=="spiral, elliptical, and irregular" or fact=="TYPES OF GALAXIES" or fact=="GALAXIES" or fact=="spiral" or fact=="elliptical" or fact=="irregular" or fact=="types of galaxies":
            print("There are three types of galaxies: spiral, elliptical, and irregular. Galaxies are classified by their shape, which is most likely due to their interactions with other galaxies.")
            time.sleep(2)
            print("There are many cool things in space, and galaxies are undoubtedly one of them. They consist of stars, interstellar gas, stellar remnants, dust, and dark matter, all bound by gravity.")
            time.sleep(2)
            print("Scientists estimate that billions of galaxies exist in the universe. When it comes to our own, we reside in the Milky Way, a spiral galaxy that belongs to a group of galaxies known as the Local Group.")
            time.sleep(2)
        elif fact=="Halley’s comet" or fact=="Halleys comet" or fact=="HALLEY’S COMET" or fact=="comet" or fact=="COMET" or fact=="Halley" or fact=="HALLEY" or fact=="Halleyscomet" or fact=="Halley'scomet":
            print("Halley’s comet makes an appearance every 75–76 years. Astronomers noticed Halley’s comet for the first time in 239 BC.")
            time.sleep(2)
            print("However, the English astronomer Edmond Halley understood that some reports of a comet approaching Earth from the previous years had actually been reappearances of the same comet and predicted it would come again in 1758.")
            time.sleep(2)
            print("According to solar system statistics, thousands of comets roam freely in our solar system, but Hailey’s comet is unquestionably the best-known one.")
            time.sleep(2)
            print("The comet is visible to the naked eye, and it was last spotted in 1986. The comet’s next perihelion will be on July 28, 2061, so make sure you don’t miss it.")
            time.sleep(2)
        elif fact=="Hubble Space Telescope" or fact=="Hubble" or fact=="Telescope" or fact=="Space" or fact=="HUBBLE FACT TELESCOPE" or fact=="HUBBLE" or fact=="SPACE" or fact=="TELESCOPE" or fact=="hubble space telescope" or fact=="hubblespacetelescope":
            print("Astronomers have made more than 1.4 million observations using the Hubble Space Telescope.")
            time.sleep(2)
            print("The Hubble Space Telescope is one of the most productive scientific instruments ever built. It was launched on April 24, 1990, and it explores the universe from Earth’s orbit.")
            time.sleep(2)
            print("According to the latest data from NASA regarding the Hubble Telescope, astronomers have published more than 18,000 scientific papers using astronomy information and data from the telescope — a number that continues to grow.")
            time.sleep(2)
            print("The telescope is as big as a school bus and weighs two adult elephants. It orbits the Earth at a speed of 17,000 miles per hour (27,000 km/h).")
            time.sleep(2)
