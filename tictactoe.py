import random

board=["-" for _ in range(9)]
currentPlayer="X"
winner=None
gameRunning=True

def printBoard(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2] + "   1 | 2 | 3")
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5] + "   4 | 5 | 6")
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8] + "   7 | 8 | 9")
    print("--+---+--")
    print()

def playerInput(board):
    while True:
        try:
            inp=int(input("enter a number 1-9: "))
            if 1<=inp<=9 and board[inp-1]=="-":
                board[inp-1]=currentPlayer
                break
            else:
                print("spot taken or invalid input. try again")
        except ValueError:
            print("please enter a valid number")

def checkWin(board):
    global winner, gameRunning
    winConditions=[
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in winConditions:
        if board[condition[0]]==board[condition[1]]==board[condition[2]]!="-":
            winner=board[condition[0]]
            gameRunning=False
            printBoard(board)
            print(f"the winner is {winner}")
            return 
        
def checkTie(board):
    global gameRunning
    if "-" not in board and winner is None:
        printBoard(board)
        print("it is a tie")
        gameRunning=False

def switchPlayer():
    global currentPlayer
    currentPlayer="O" if currentPlayer=="X" else "X"

def computerMove(board):
    while currentPlayer=="O":
        position=random.randint(0, 8)
        if board[position]=="-":
            board[position]="O"
            break

while gameRunning:
    printBoard(board)
    if currentPlayer=="X":
        playerInput(board)
    else:
        computerMove(board)
    checkWin(board)
    checkTie(board)
    if gameRunning:
        switchPlayer()