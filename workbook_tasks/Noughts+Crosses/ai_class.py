import random

class NaCAI:
    
    def all_values_present(self, arrayUnknown, arrayKnown): #Checks if all values in array2 are in array1
        
        a1 = arrayUnknown
        a2 = arrayKnown

        for element in a1:
            if element in a2:
                a2.remove(element)
        
        if len(a2) == 0:
            return True
        
        return False

    def make_move(self, board):

        ### First section checks for if AI can win ###
        
        position = [0,0]
        
        for y in range(3): #Check winning move across
            if self.all_values_present(board[y],[0,2,2]):
                print("winning across")
                x = board[y].index(0)
                return [y,x]

        for x in range(3): #Check winning move down
            if self.all_values_present([board[0][x], board[1][x], board[2][x]], [0,2,2]):
                print("winning down")
                y = 0
                while board[y][x] != 0:
                    y += 1
                return [y,x]
        

        if self.all_values_present([board[0][0], board[1][1], board[2][2]], [0,2,2]): #Check winning move diagonal(L 2 R)
            for x in range(3):
                if board[x][x] == 0:
                    return [x,x]

        if self.all_values_present([board[0][2], board[1][1], board[2][0]], [0,2,2]): #Check winning move diagonal(R 2 L)
            for x in range(3):
                if board[x][2-x] == 0:
                    return [x,2-x]


        #    1   2   3
        #  a 00  01  02
        #  b 10  11  12
        #  c 20  21  22


        ### Second section checks if Opponent can win, and Blocks ###
        for y in range(3): #Check opp. across
            if self.all_values_present(board[y], [0,1,1]):
                x = board[y].index(0)
                return [y,x]

        for x in range(3): #Check opp. down
            if self.all_values_present([board[0][x], board[1][x], board[2][x]], [0,1,1]):
                y = 0
                while board[y][x] != 0:
                    y += 1
                return [y,x]
        
        if self.all_values_present([board[0][0], board[1][1], board[2][2]], [0,1,1]): #Check opp. diagonal(L 2 R)
            for x in range(3):
                if board[x][x] == 0:
                    return [x,x]

        if self.all_values_present([board[0][2], board[1][1], board[2][0]], [0,1,1]): #Check opp. move diagonal(R 2 L)
            for x in range(3):
                if board[x][2-x] == 0:
                    return [x,2-x]

        #Play in centre if free
        if board[1][1] == 0:
            return (1,1)
        
        #If there is no better option, the AI picks randomly where to play
        while True:
            position = (random.randint(0,2), random.randint(0,2))
            if board[position[0]][position[1]] == 0:
                return position


if __name__ == "__main__":
    ai = NaCAI()
    board = [
                [1,0,0],
                [0,0,2],
                [1,0,0]
            ]

    print(ai.make_move(board))
    print(board)