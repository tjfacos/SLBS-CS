import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
Morbiest = None
gameRunning = True 
modeSelection = True
enemyPlayer = None

print("Welcome to Noughts and Crosses!")

# select game mode
def gameCheck():
    global enemyPlayer
    global modeSelection
    while modeSelection == True:
        print()
        print("What game mode would you like to play?")
        mode = input("1 player or 2 player: ")
        if mode == "1":
            enemyPlayer = 1
            modeSelection = False
        elif mode == "2":
            enemyPlayer = 2
            modeSelection = False
        elif mode != "1" or "2":
            print("Oops, I'm not sure how to play that mode.")
            modeSelection = True
       
# printing the game board
def printBoard(board):
    print("=======")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("=======")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("=======")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("=======")

# take player input
def playerInput(board):
    inp = int(input("Enter where you wish to place your counter (1-9):"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops that move could not be made, please enter again.")
        switchPlayer()

# check for win or tie
def checkHorizontal(board):
    global Morbiest
    if board[0] == board[1] == board[2] and board[0] != "-":
           Morbiest = board[0]
           return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
           Morbiest = board[3]
           return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
           Morbiest = board[6]
           return True
def checkVertical(board):
    global Morbiest
    if board[0] == board[3] == board[6] and board[0] != "-":
           Morbiest = board[0]
           return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
           Morbiest = board[1]
           return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
           Morbiest = board[2]
           return True
def checkDiagonal(board):
    global Morbiest
    if board[0] == board[4] == board[8] and board[0] != "-":
           Morbiest = board[0]
           return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
           Morbiest = board[2]
           return True
def checkTie(board):
       global gameRunning
       if "-" not in board:
            printBoard(board)
            print("Tough luck, it’s a tie!")
            gameRunning = False
def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print()
        print(f"{Morbiest}s have won!")
        print()
        gameRunning = False
        printBoard(board)

# monkeys on typewriters
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# checking for monke
def monkeCheck():
    global enemyPlayer
    if enemyPlayer == 1 and gameRunning == True:
        computer(board)
        checkWin()
        checkTie(board)


# while game is running
while gameRunning:
    gameCheck()
    printBoard(board)
    playerInput(board) 
    switchPlayer()
    checkWin()
    checkTie(board)
    monkeCheck()