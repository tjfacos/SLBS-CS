# Imports go at the top
from microbit import *
from random import randint
from time import ticks_ms

compass.calibrate()




score = 0

bearing = randint(1,360)

while True:

    direction = compass.heading()

    difference = direction - bearing

    #If difference is within 5 degrees of 0, give point
    #If difference is within 45 of 0, point north
    #If negative, point right (east)
    # if positive, point left (west) 

    if -22.5 < difference <= 22.5:
        display.show(Image.ARROW_N)

#FIX FROM THIS POINT

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
        
    
    if abs(difference) < 5:
        print("1 Point!")
        score += 1
        display.show(Image.SMILE)
        sleep(1000)
        bearing = randint(1,360)