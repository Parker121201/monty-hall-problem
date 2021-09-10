import game
import simulate


spacer = "-"*30

choice = input("Welcome to the Monty Hall problem! Please select an option (play/simulate): ")

if choice.lower() == "play":
    try:
        playTimes = int(input("How many times would you like to play?: "))
        for i in range(playTimes):
            game.startingText()
            game.playGame()
            print(spacer)
            print(spacer)
            print(spacer)
    except ValueError:
        print("Invalid value, try again.")
elif choice.lower() == "simulate":
    doorChoice = None
    switchChoice = None

    doorOption = input("Door choice fixed or random? (fixed/random): ").lower()
    if doorOption == "fixed":
        doorChoice = input("Door choice (1, 2, 3): ")
    switchOption = input("Switch option fixed or random? (fixed/random): ").lower()
    if switchOption == "fixed":
        switchChoice = input("Switch doors? (yes/no): ").lower()
    simCount = input("Number of simulations (whole, positive number): ")

    simulate.simulate(doorOption, doorChoice, switchOption, switchChoice, int(simCount))
else:
    print("Invalid response! Try again")