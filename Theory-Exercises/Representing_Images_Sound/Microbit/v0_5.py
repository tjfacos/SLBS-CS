# Microbit Project - Compass Game/Treasure Hunt - Thomas Facos - Version 0.5

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

print("Game Thingy - V0.5")
print("Find the right direction!")


score = 0

bearing = randint(1,360)

while True:

    direction = compass.heading()
    
    difference = direction - bearing


    if abs(difference) in range(158, 203):
        # print("Down arrow")
        display.show(Image.ARROW_S)
    elif difference in range(-67, -22):
        # print("up right")
        display.show(Image.ARROW_NE)
    elif difference in range(-112, -67):
        # print("Right arrow")
        display.show(Image.ARROW_E)
    elif difference in range(-157,-112):
        # print("down right")
        display.show(Image.ARROW_SE)
    elif difference in range(23, 68):
        # print("up left")
        display.show(Image.ARROW_NW)
    elif difference in range(68, 113):
        # print("Left arrow")
        display.show(Image.ARROW_W)
    elif difference in range(113, 158):
        # print("left down")
        display.show(Image.ARROW_SW)
    else:
        # print("Up arrow")
        display.show(Image.ARROW_N)
    
    
    print(str(abs(difference)) + " Degrees away!")

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