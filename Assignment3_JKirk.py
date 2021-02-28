""" 
Author: Jamey Kirk
Title: Assignment3_Turtle2
Date: 02/28/2021
Description: use turtle to draw more polygons
"""

## setup turtle
import turtle
s = turtle.getscreen()
t = turtle.getturtle()


## function defs
def angle(sides: 'int') -> 'int':
    """
    calculates turn angle of polygon given sides entered by user
    """
    return 360/sides

def drawShape(Turtle, sides, length: 'int'):
    """
    draws polygon based on user input of # of sides and side length
    """
    ## as a side is drawn subtract 1 from the sidesTot
    while sides > 0:
        t.fd(length)
        t.lt(360/sides)
        if abs(t.pos()) < 1:
            break

def spinPolygon(Turtle, sides, angle, length, repeat: 'int'):
    """
    draws polygon after each turn to the left
    """
    pass

def scalePolygon(Turtle, sides, length, sfactor: 'int', number: 'int'):
    """
    draws copies of polygon for a given number ~> each copy grows (length x sfactor) times the previous length
    """
    pass


## user values
sides = 5
length = 100
repeat = 0
sFactor = 0
number = 0

## fuction calls
drawShape(t, sides, length)

turtle.exitonclick()