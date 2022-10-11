import turtle
import os
import time


def drawShape(size, sides):
  angle = 360/sides
  
  for _ in range(sides):
    turtle.forward(size)
    turtle.left(angle)
  

drawShape(50, 9)
