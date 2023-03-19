import planet

def getUserInput(message):
    i = input(message + '\n')
    return i

def isQuestion(str):
    """Return True if the given string contains ?. It analyses if the user's input is a qustion or not."""
    return str.find('?') != -1

def findWord(str, word):
    return str.find(word) != -1

def startChat():
    userInput = getUserInput('Hello!')
    while True:
        if userInput == '' or userInput.find('Bye') != -1:
            break

#getUserInput()
#print(planet.getPlanet('Earth'))
startChat()