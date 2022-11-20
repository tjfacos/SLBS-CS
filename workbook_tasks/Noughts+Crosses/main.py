import os
from ai_class import NaCAI


class NoughtsAndCrosses:
    board = [[0 for x in range(3)] for y in range(3)]
    won = False
    AI_last_move = ""

    def clearScreen(self):
        if os.name == 'nt':
            #Clear on Windows
            os.system('cls')
        else:
            #Clear on Linux
            os.system('clear')

        print("============== Noughts and Crosses ==============", end="\n\n")
        

    def check(self, position, placeholder): #returns True if game is won
        if self.board[position[0]] == [placeholder for x in range(3)]:
            return True, False #returns if_won, and if_draw
        if [self.board[x][position[1]] for x in range(3)] == [placeholder for x in range(3)]:
            return True, False
        if position[0] == position[1] and [self.board[x][x] for x in range(3)] == [placeholder for x in range(3)]: #diagonal down left2right
            return True, False
        if position[0]+position[1] == 2 and [self.board[x][2-x] for x in range(3)] == [placeholder for x in range(3)]: #diagonal down right2left
            return True, False
        
        for line in self.board:
            for place in line:
                if place == 0:
                    return False, False
        
        return False, True
    
    
    def makeNaC(self, digit):
        if digit == 0:
            return "-"
        elif digit == 1:
            return "X"
        else:
            return "O"


    def outputBoard(self):
        self.clearScreen()

        
        output_board = [list(map(self.makeNaC, self.board[0])), list(map(self.makeNaC, self.board[1])), list(map(self.makeNaC, self.board[2]))]


        print("  {} {} {}".format(1,2,3))
        print("A {} {} {}".format(output_board[0][0], output_board[0][1], output_board[0][2]))
        print("B {} {} {}".format(output_board[1][0], output_board[1][1], output_board[1][2]))
        print("C {} {} {}".format(output_board[2][0], output_board[2][1], output_board[2][2]))
        print()

    def move(self, player, ai_player = False, invalid=False):
        self.outputBoard()
        placeholder = 0

        if player == "X":
            placeholder = 1
        elif ai_player:
            placeholder = 2
            player = "AI"
        else:
            placeholder = 2
        
        move = []
        
        if player != "AI":
            if self.AI_last_move:
                print(self.AI_last_move)
            prompt_insert = ""
            if invalid:
                prompt_insert = "VALID"
            move = list(input(f"Player {player}, enter {prompt_insert} move: "))

            if not len(move) == 2 or not move[0].lower() in ["a","b","c"] or not move[1] in ["1","2","3"]:
                self.outputBoard()
                return self.move(player, invalid=True)

        #    1   2   3
        #  a 00  01  02
        #  b 10  11  12
        #  c 20  21  22

            position = (ord(move[0].lower()) % ord('a'), int(move[1]) - 1)
        
            if not self.board[position[0]][position[1]]:
                self.board[position[0]][position[1]] = placeholder
            else:
                print("Space is already taken")
                self.move(player, invalid=True)
        
        
        else: #if player is AI
            position = ai_player.make_move(self.board)
            self.AI_last_move = f"AI Player plays {chr(position[0]+65)}{position[1]+1}"
            self.board[position[0]][position[1]] = placeholder

        win, draw = self.check(position, placeholder)

        if win:
            self.outputBoard()
            print(f"Player {player} wins!!!")
            self.won = True
        elif draw:
            self.outputBoard()
            print("Draw!!!")
            self.won = True

    def __call__(self): #Starts Game
        self.clearScreen()

        #Reset values
        self.won = False
        self.board = [[0 for x in range(3)] for y in range(3)]
        self.AI_last_move = ""

        mode = ""
        while not mode in ["S", "M"]:
            mode = input("Enter S for Singleplayer, or M for Multiplayer: ").upper()
            if not mode in ["S", "M"]:
                self.clearScreen()
                print("Invalid! ", end="")
        
        players = ["X", "O"]
        
        ai_player = False
        if mode == "S":
            ai_player = NaCAI()
        
        round = 0
        while not self.won:
            
            p = players[round%2]
            self.move(p, ai_player)

            round += 1
        

        again = ""
        while not again in ["Y", "N"]:
            again = input("\n\nPlay again? [Y/N]: ").upper()[0]
            if not again.upper() in ["Y", "N"]:
                self.clearScreen()
                print("Invalid! ", end="")
        
        if again.upper() == "Y":
            return self.__call__()
        
        return True
        
        
x = NoughtsAndCrosses()
x()