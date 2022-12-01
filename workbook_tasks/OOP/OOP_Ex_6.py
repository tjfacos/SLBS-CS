import random

class Die:
    __value = 0
    
    def __init__(self,sides) -> None:
        self.__sides = sides
        
    
    def set_sides(self, sides):
        self.__sides = sides

    def roll(self):
        self.__value = random.randint(1, self.__sides)
        return self.__value
    