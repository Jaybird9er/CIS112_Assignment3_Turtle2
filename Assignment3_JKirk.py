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
def angle(sides: 'int') -> 'float or int':
    """
    calculates turn angle of polygon given sides entered by user
    """
    return 360/sides

def drawShape(Turtle, sides, length: 'int'):
    """
    draws polygon based on user input of # of sides and side length
    """
    ## as a side is drawn subtract 1 from the sidesTot
    draw = True
    while draw:
        t.fd(length)
        t.lt(360/sides)
        if abs(t.pos()) < 1:
            draw = False

def spinPolygon(Turtle, sides, angle, length, repeat: 'int'):
    """
    after each polygon is drawn, turn Turtle to the left by 'angle' degrees
    """
    count = 0
    draw = True
    while draw:
        drawShape(t, sides, length)
        t.lt(angle)
        count += 1
        if count == repeat:
            draw = False

def scalePolygon(Turtle, sides, length, sfactor: 'int', number: 'int'):
    """
    draws copies of polygon for a given number ~> each copy grows (length x sfactor) times the previous length
    """
    pass


## user values
sides = 5
length = 100
repeat = 5
sFactor = 0
number = 0
angle = angle(sides)

## main program (fuction calls)
spinPolygon(t, sides, angle, length, repeat)
t.reset()
# scalePolygon(urtle, sides, length, sfactor, number)

turtle.exitonclick()