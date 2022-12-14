#Skeleton Program for the AQA AS1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA AS1 Programmer Team
#developed in a Python 3 programming environment

#Version Number 1.0

import random

def GetRowColumn():
  print()
  Column = int(input("Please enter column: "))
  Row = -1
  while Row not in range(10):
      Row = int(input("Please enter row: "))
      if Row not in range(10):
          print('Invalid value entered')

  print()
  return Row, Column
            
def MakePlayerMove(Board, Ships):
  Row, Column = GetRowColumn()
  if Board[Row][Column] == "m" or Board[Row][Column] == "h":
    print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
  elif Board[Row][Column] == "-":
    print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
    Board[Row][Column] = "m"
  else:
    print("Hit at (" + str(Column) + "," + str(Row) + ").")
    CheckSunk(Board, Ships, Row, Column)
    Board[Row][Column] = "h"


def MakePlayerTorpedoMove(Board, Ships):
    Row, Column = GetRowColumn()
    while Row > -1:
        if Board[Row][Column] in ["-", "m"]: 
            Board[Row][Column] = "m"
        else: 
            print("Hit at (" + str(Column) + "," + str(Row) + ").")
            CheckSunk(Board, Ships, Row, Column)
            Board[Row][Column] = "h"
            return None
        Row -= 1
    print("Torpedo hit nothing!")



def SetUpBoard():
  Board = []
  for Row in range(10):
    BoardRow = []
    for Column in range(10):
      BoardRow.append("-")
    Board.append(BoardRow)
  return Board

def LoadGame(Filename, Board, Ships):
  try:
    BoardFile = open(Filename, "r")
  except:
    PlaceRandomShips(Board, Ships)
    return
  

  for Row in range(10):
    Line = BoardFile.readline()
    for Column in range(10):
      Board[Row][Column] = Line[Column]
  BoardFile.close()
    
def PlaceRandomShips(Board, Ships):
  for Ship in Ships:
    Valid = False
    while not Valid:
      Row = random.randint(0, 9) 
      Column = random.randint(0, 9) 
      HorV = random.randint(0, 1)
      if HorV == 0:
        Orientation = "v" 
      else:
        Orientation = "h" 
      Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation)
    print("Computer placing the " + Ship[0])
    PlaceShip(Board, Ship, Row, Column, Orientation)

def PlaceShip(Board, Ship, Row, Column, Orientation):
  if Orientation == "v":
    for Scan in range(Ship[1]):
      Board[Row + Scan][Column] = Ship[0][0]
  elif Orientation == "h":
    for Scan in range(Ship[1]):
      Board[Row][Column + Scan] = Ship[0][0]

def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
  if Orientation == "v" and Row + Ship[1] > 10:
    return False
  elif Orientation == "h" and Column + Ship[1] > 10:
    return False
  else:
    if Orientation == "v":
      for Scan in range(Ship[1]):
        if Board[Row + Scan][Column] != "-":
          return False
    elif Orientation == "h":
      for Scan in range(Ship[1]):
        if Board[Row][Column + Scan] != "-":
          return False
  return True

def CheckWin(Board):
  for Row in range(10):
    for Column in range(10):
      if Board[Row][Column] in ["A","B","S","D","P"]:
        return False
  return True

def CheckSunk(Board, Ships, Row, Column):
    for ship in Ships:
        if Board[Row][Column] == ship[0][0]:
            ship[1] -= 1
        if ship[1] == 0:
            print(ship[0] + " is sunk!")
        

 
def PrintBoard(Board):
  print()
  print("The board looks like this: ")  
  print()
  print (" ", end="")
  for Column in range(10):
    print(" " + str(Column) + "  ", end="")
  print()
  for Row in range(10):
    print (str(Row) + " ", end="")
    for Column in range(10):
      if Board[Row][Column] == "-":
        print(" ", end="")
      elif Board[Row][Column] in ["A","B","S","D","P"]:
        print(" ", end="")                
      else:
        print(Board[Row][Column], end="")
      if Column != 9:
        print(" | ", end="")
    print()
       
def DisplayMenu():
  print("MAIN MENU")
  print()
  print("1. Start new game")
  print("2. Load training game")
  print('3: Continue from last saved game')
  print("9. Quit")
  print()
    
def GetMainMenuChoice():
  print("Please enter your choice: ", end="")
  Choice = int(input())
  print()
  return Choice

def PlayGame(Board, Ships):
  GameWon = False
  usedTorpedo = False
  while not GameWon:
    
    AutoSaveGame(Board)
    PrintBoard(Board)

    choice = ""
    if not usedTorpedo:
        choice = input("Fire a Torpedo? Y/N: ")

    if choice and choice.upper() == "Y":
            MakePlayerTorpedoMove(Board, Ships)
            usedTorpedo = True
    else:   
        MakePlayerMove(Board, Ships)
                
    GameWon = CheckWin(Board)

    if GameWon:
      print("All ships sunk!")
      print()

def AutoSaveGame(Board):
  with open(SAVEGAME, 'w') as file:
    for row in Board:
      file.write(''.join(row) + '\n')

if __name__ == "__main__":
  TRAININGGAME = "Training.txt"
  SAVEGAME = 'SaveGame.txt'
  MenuOption = 0
  while not MenuOption == 9:
    Board = SetUpBoard()
    Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]]
    DisplayMenu()
    MenuOption = GetMainMenuChoice()
    if MenuOption == 1:
      PlaceRandomShips(Board, Ships)
      PlayGame(Board,Ships)
    if MenuOption == 2:
      LoadGame(TRAININGGAME, Board, Ships)
      PlayGame(Board, Ships)
    if MenuOption == 3:
      LoadGame(SAVEGAME, Board, Ships)
      PlayGame(Board, Ships)   
