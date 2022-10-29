def getBase(): #Returns a valid base from user
    while base not in [2, 10, 16]:
            try: base = int(input("Enter base: "))
            except: print("Only enter numbers. ", end="")
            
            if base not in [2, 10, 16]: print("Enter Base 2, 10, or 16. ", end="")

class conversions:
    def __init__(self, input_list, base):
        self.array = input_list
        self.binary = ""
        self.denary = ""
        self.hex = ""

        #Call conversions
    
    
    def D2B(self):
        value = int(''.join(self.array))
        i = len(self.array) * 4
        output = ""
        while value > 0:
            if value > 2**i:
                output += "1"
                value -= 2**i
            else:
                output += "0"
            i -= 1
        return output
              
    def B2D(self):
        value = 0
        for place in range(len(self.binary)):
            value += 2**place * int(self.binary[place])
        return str(value)

    #Unfinished
    def B2H(self):
        for x in range(0, len(self.array), 4):
            pass #Convert each 4 bits into denary, then to Hex
    def H2B(self):
        pass
    #MUST FINISHED


def converter(input_string): 
    letters = ["A","B","C","D","E","F"]
    base = 0
    input_list = []

    for character in input_string:
        #Check valid
        if character not in letters or not character.isnumeric():
            print('Invalid input')
            return None
        
        try:
            input_list.append(int(character))
        except TypeError:
            #If it can't be cast to an integer, but is still valid, there must be letters, so it's base 16
            base = 16
            input_list.append(character)
        
        #If the number added isn't 1 or 0, but the base isn't 16, its base 10
        if input_list[-1] > 1 and not base:
            base = 10
    
    #Otherwise, check which base it is
    if not base:
        print('START BASE: ', end="")
        base = getBase()
    
    print(f"Converting {base}...")
    
    converterObj = conversions(input_list)



            
if __name__ == "__main__":
    print(converter(input("Enter Data: ")))