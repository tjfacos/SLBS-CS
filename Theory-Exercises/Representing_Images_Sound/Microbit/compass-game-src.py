# Microbit Project - Compass Game/Treasure Hunt - Thomas Facos

# This code is designed to run on a microbit V1
# You can import this python src code, or the hex file, into 
# the BBC micro:bit Python simulator found at the link below to see how it works

# https://python.microbit.org/v/3/



# Source Code: main.py


# Imports go at the top
from microbit import *
from random import randint
from time import ticks_ms

compass.calibrate()

print("Game Thingy V0.1")
print("Find the treasure!")



score = 0

bearing = randint(1,360)

while True:

    direction = compass.heading()

    upper_limit = bearing - 22.5
    if upper_limit < 0:
        upper_limit += 360
    
    if upper_limit <= direction or direction < bearing+22.5:
        display.show(Image.ARROW_N)
    elif bearing+45-22.5 <= direction and direction < bearing+45+22.5:
        display.show(Image.ARROW_NE)
    elif direction < bearing+90+22.5:
        display.show(Image.ARROW_E)
    elif direction < bearing+135+22.5:
        display.show(Image.ARROW_SE)
    elif direction < bearing+180+22.5:
        display.show(Image.ARROW_S)
    elif  direction < bearing+225+22.5:
        display.show(Image.ARROW_SW)
    elif direction < bearing+270+22.5:
        display.show(Image.ARROW_W)
    else:
        display.show(Image.ARROW_NW)

    print(str(abs(direction-bearing)) + " Degrees away!")

    if ticks_ms() > 20_000:
        print("Time's UP!")
        print(score)
        if score > 4:
            print("You win!!!")
            display.show(Image.YES)
        else:
            print("You lose!!!")
            display.show(Image.NO)

        break
        
    
    if direction in range(bearing-5, (bearing+5)%360):
        print("1 Point!")
        score += 1
        display.show(Image.SMILE)
        sleep(1000)
        bearing = randint(1,360)