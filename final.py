def start():
    print("Welcome to the Big City!")
    answer1 = input("What would you like to do?\n1. Signal a cab\n2. Walk down the street\n3. Go back into your new apartment to unpack\n")
    if answer1 == "1":
        signalCab()
    elif answer1 == "2":
        walkAround()
    elif answer1 == "3":
        goBackInside()
    else:
        print("Sorry but thats not an option, try again\n\n\n")
        start()
def signalCab():
    answer2 = input("Cool, you flag a taxi and once you get in the driver asks where you want to go\n1. Central Park\n2. Statue of liberty\n3. Art Gallery\n")
    if answer2 == "1":
        centralPark()
    elif answer2 == "2":
        ladyLiberty()
    elif answer2 == "3":
        artGallery()
    else:
        print("Sorry but thats not an option, try again\n\n\n")
        signalCab()
def centralPark():
    answer3 = input("GAME OVER.\nYou walked through the peaceful park without a care in the world, unfortunatly that means you didnt notice the wet paint sign before you sat on that bench. There was blue paint everywhere! No taxi would pick you up out of fear for getting paint on their car so you had to walk all the way home. By the time you got back you were exausted and went straight to bed.\n\n SLEEPY ENDING\n\n\nDo you want to try again\nY/N\n")
    if answer3 == "Y":
        start()
    elif answer3 == "N":
        print("okay, then leave ;-;")
    else:
        print("Sorry but thats not an option, try again")
        centralPark()
def ladyLiberty():
    answer4 = input("GAME OVER.\nWhile you were on the ferry to the Statue, it suddenly jolted and lets just say it only went down from there. literally, the ferry sank and unfortunatly you didn't know how to swim and you drowned.\n FERRY ENDING\n\n\nDo you want to try again?\nY/N\n")
    if answer4 == "Y":
        start()
    elif answer4 == "N":
        print("Jeez okay then")
    else:
        print("Sorry but thats not an option, try again\n\n\n")
        ladyLiberty()
def artGallery():
    answer5 = input("GAME OVER. \nWell that kinda sucks. I guess you want to know what happened then. Well all I can say is meteor.\nDo you want to play again?  Y/N\n")
    if answer5 == "Y":
        start()
    elif answer5 == "N":
        print("um okay i guess you can leave then *-*")
    else:
        print("Sorry but thats not an option, try again")
        artGallery()
def walkAround():
    answer6 = input("Alraight, a bit of walking never hurt anyone, as you're walking you notice a dark alley. Do you want to\n1. Go explore the alley\n2. Walk past it")
    if answer6 == "1":
        exploreTheAlley()
    elif answer6 == "2":
        walkPastAlley()