import random

spacer = "-"*30

def doorAssignment():
    choices = ["Car", "Goat", "Goat"]
    doors = []
    for i in range(3):
        new = (random.choice(choices))
        doors.append(new)
        choices.remove(new)
    return doors


def hostOpenDoor(doors, doorChoice):
    doorNums = ["1", "2", "3"]
    doorNums.remove(doorChoice)

    for i in range(2):
        if doors[int(doorNums[i]) - 1] == "Car":
            doorNums.remove(doorNums[i])
            break
    hostChoice = int(random.choice(doorNums))
    return hostChoice


def switchChoice(switchDoor):
    print(f"Host: You have switched to door number {switchDoor}!")
    doorChoice = switchDoor
    return doorChoice


def reveal(finalChoice, doors):
    print("It's time to see what you win!")
    print(f"Behind door number {finalChoice} is...")
    print(f"A {doors[int(finalChoice)-1]}")
    print(spacer)
    if doors[int(finalChoice)-1] == "Car":
        print("Congratulations! You've won a brand new sports car!")
    else:
        print("Better luck next time. Enjoy your goat!")


def startingText():
    print("""
Welcome to the Monty Hall problem (also known as the goat and car game)!
You will be presented with three doors. Your objective is to win a brand new sports car!
    """)
    print(spacer)
    print("""
Behind one door is the car, behind the others are goats. Your host will know what is behind each door.
Get ready to choose a door!
    """)
    print(spacer)
    print("Let's play!")


def playGame():
    print("Host: Hello! I'm your host, Monty Hall!")

    while True:
        doorChoice = input("Host: Pick a door (1, 2, 3): ")
        if doorChoice not in ("1", "2", "3"):
            print("Host: Invalid response! Try again")
        else:
            break

    print(f"You picked door number {doorChoice}.")
    print(spacer)

    doors = doorAssignment()
    hostChoice = hostOpenDoor(doors, doorChoice)
    print(f"Host: Before we reveal what is behind door number {doorChoice}...I'm going to open door number {hostChoice}!")
    print(f"Door number {hostChoice} has a {doors[hostChoice-1]}")
    remaining = ["1", "2", "3"]
    remaining.remove(str(doorChoice))
    remaining.remove(str(hostChoice))

    while True:
        switch = input(f"Host: Do you like door number {doorChoice}, or would you like to switch to door {remaining[0]}? (y/n): ")
        if switch.lower() == "y":
            finalChoice = switchChoice(remaining[0])
            break
        elif switch.lower() == "n":
            print(f"Host: You are sticking with door number {doorChoice}!")
            finalChoice = doorChoice
            break
        else:
            print("Host: Invalid response! Try again")

    print(spacer)
    reveal(finalChoice, doors)








# To run from this file
# startingText()
# playGame()