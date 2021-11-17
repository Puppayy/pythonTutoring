import TicTacToeHelper

board = ['1', '2', '3', '4', '5', '6', '7', '8']

def isValidMove(boardList, spot):
    if spot in boardList:
        return True
    else:
        return False

def updateBoard(boardList, spot, playerLetter):
    for i in range(0,9):
        if boardList[i] == spot:
            boardList[i] = playerLetter


def playGame(): 
    play = 'y'
    while play.lower() == 'y':
        board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        moves = 0
        winner = "n"
        player = 0

        #Determines first player
        firstPlayer = input("Which player starts? (x or o) ")
        while (not (firstPlayer == 'o' or firstPlayer == 'x')):
            firstPlayer = input("Which player starts? (x or o) ")
        if (firstPlayer == 'o'):
            player += 1

        TicTacToeHelper.printPrettyBoard(board)
        
        #Main game
        while (winner == "n"):
            p = 'n'
            if player % 2 == 0:
                p = 'x'
            else:
                p = 'o'
            choice = str(input("Player " + p + ", pick a spot: "))
            while (int(choice) < 0 or int(choice) > 8 or not isValidMove(board, choice)):
                choice = str(input("Player " + p + ", pick a spot: "))
            updateBoard(board, choice, p)
            moves += 1
            winner = TicTacToeHelper.checkForWinner(board, moves)
            player += 1
            TicTacToeHelper.printPrettyBoard(board)

        #Game over section
        print("Game over!")
        if (winner == 's'):
            print("Stalemate reached!")
        else:
            print("Player " + winner + " is the winner!")
        play = input("Would you like the play another round? (y or n): ")
    print("Goodbye!")



playGame()
        