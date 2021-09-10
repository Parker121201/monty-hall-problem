import random

# simulate(doorOption, doorChoice, switchOption, switchChoice, simCount)

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


def switchTheChoice(switchDoor):
    doorChoice = switchDoor
    return doorChoice


def reveal(finalChoice, doors):
    if doors[int(finalChoice)-1] == "Car":
        return 1
    else:
        return 0


def simulate(doorOption, givenDoorChoice, switchOption, givenSwitchChoice, simCount):
    timesWon = 0
    timesLost = 0
    gamesPlayed = 0
    choiceSummary = f"""
You had a {doorOption} door choice. If fixed, you chose to select {givenDoorChoice}. 
You had a {switchOption} switch choice. If fixed, you chose {givenSwitchChoice}.
After running {simCount} simulations, your results are here:
"""
    for i in range(simCount):
        if doorOption == "fixed":
            doorChoice = givenDoorChoice
        elif doorOption == "random":
            doorChoice = random.choice(["1", "2", "3"])

        if switchOption == "fixed":
            switchChoice = givenSwitchChoice
        elif switchOption == "random":
            switchChoice = random.choice(["yes", "no"])

        doors = doorAssignment()
        hostChoice = hostOpenDoor(doors, doorChoice)

        remaining = ["1", "2", "3"]
        remaining.remove(str(doorChoice))
        remaining.remove(str(hostChoice))

        if switchChoice.lower() == "yes":
            finalChoice = switchTheChoice(remaining[0])
        elif switchChoice.lower() == "no":
            finalChoice = doorChoice

        outcome = reveal(finalChoice, doors)
        if outcome == 1:
            timesWon += 1
            gamesPlayed += 1
        elif outcome == 0:
            timesLost += 1
            gamesPlayed += 1

    summary(timesWon, timesLost, gamesPlayed, choiceSummary)


def summary(timesWon, timesLost, gamesPlayed, choiceSummary):
    percentWon = timesWon / gamesPlayed
    percentLost = timesLost / gamesPlayed
    print(choiceSummary)
    print(f"""
Times won: {timesWon}
Win percentage: {percentWon * 100}%
Times lost: {timesLost}
Loss percentage: {percentLost * 100}%
""")
