import random

def displayMenu():
    print("Let's play Rock Paper Scissors.");
    print("The rules of the game are:")
    print("   Rock smashes Scissors")
    print("   Scissors cut Paper")
    print("   Paper covers Rock")
    print("   If both the choices are the same, it's a tie")

def getComputerChoice():
    return random.randint(0,2)

def getPlayerChoice():
    inp = -1
    while (inp < 0 or inp > 2):
        print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
        inp = int(input(">"))
    return inp

def playRound(computerChoice, playerChoice):
    if (computerChoice == 0 and playerChoice == 1):
        return 1
    elif (computerChoice == 0 and playerChoice == 2):
        return -1
    elif (computerChoice == playerChoice):
        return 0
    elif (computerChoice == 1 and playerChoice == 0): 
        return -1
    elif (computerChoice == 1 and playerChoice == 2):
        return 1
    elif (computerChoice == 2 and playerChoice == 0):
        return -1
    elif (computerChoice == 2 and playerChoice == 1):
        return 1

#No parameters, will retrun true if continue to play and false if not
def continueGame():
    inp = input("Do you want to continue playing(y or n)?")
    if inp.lower() in "y":
        return True
    return False

#Main program, no parameters
#Runs the entire program
def main():
    ties = 0 
    wins = 0 
    loses = 0 
    cont = True
    while (cont):
        displayMenu()
        computerChoice = getComputerChoice()
        playerChoice = getPlayerChoice()
        result = playRound(computerChoice,playerChoice)
        if result == -1:
            print("Computer wins.")
            loses += 1
        elif result == 1:
            print("You win!")
            wins += 1
        elif result == 0:
            print("Tied.")
            ties += 1
        cont = continueGame()
    print("You won " + str(wins) + " games(s).")
    print("The computer won " + str(loses) + " games(s).")
    print("You tied with the computer " + str(ties) + " time(s).")

main()



