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
    
    def __str__(self):
        output =  f"{self.__sides} sided Die"

        for i in range(self.__sides):
            output += f"\n{i+1}"
        
        return output

twelve = Die(12)
six = Die(6)

print(twelve)
print(six)

print()
print()
print(twelve.roll()+six.roll())

sum = 0
for x in range(5):
    if x < 3:
        sum += Die(6).roll()
    else:
        sum += Die(12).roll()

print(f"Sum of 3 6-sided and 2 12-sided: {sum}")

dice = []
no_6, no_12 = list(map(int, input("Enter the number of 6-sided dice and 12 sided dice: ").split()))

for x in range(no_6):
    dice.append(Die(6))
for i in range(no_12):
    dice.append(Die(12))