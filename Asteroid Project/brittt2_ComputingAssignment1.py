"""
Thomas Brittain
brittt2@mcmaster.ca
400650099

An asteroid shooter program, which generates random asteroids and has the user enter coordinates to try to hit them and earn points.
"""

import turtle
import math
import random
import time
from pixels import check_pixel_color

#Window Config
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Incredible and amazing super fun space game!"

#Creating Window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)

# Create the turtle objects
bgsketch = turtle.Turtle()
explosionsketch = turtle.Turtle()
scoresketch = turtle.Turtle()
shotssketch = turtle.Turtle()

#Removes turtles and drawing to increase performance
bgsketch.hideturtle() 
explosionsketch.hideturtle()
scoresketch.hideturtle()
shotssketch.hideturtle()
screen.tracer(False)

#Game Variables and window config
screen.bgcolor(0.1,0,0.2)

SCORE=0
BLUE_PTS=50
PINK_PTS=10

MIN_STARS=10
MAX_STARS=100

MIN_AST=10
MAX_AST=25

####Start of Main Game Code

#Draws a random number of stars between my min and max values
for i in range(0,random.randint(MIN_STARS,MAX_STARS)):
    rand_colour=random.uniform(0.2,1)
    bgsketch.color(rand_colour,rand_colour,rand_colour)
    bgsketch.up()
    bgsketch.goto(random.randint(-SCREEN_WIDTH//2, SCREEN_WIDTH//2), random.randint(-SCREEN_HEIGHT//2, SCREEN_HEIGHT//2))
    bgsketch.down()
    bgsketch.begin_fill()
    bgsketch.circle(random.randint(1,5))
    bgsketch.end_fill()

####Asteroid creation

#Single asteroid at (0,0)

#Super epic 50/50 random colour generator
colour=random.randint(0,1)
for i in range(0,colour):
    bgsketch.color('blue')
for i in range(0,0**colour):
    bgsketch.color('pink')

#Actual drawing logic
bgsketch.setheading(random.randint(0,359))
length=random.randint(5,30)
bgsketch.up()
bgsketch.goto(0,0)
bgsketch.forward(length)
bgsketch.down()
bgsketch.left(120)
bgsketch.begin_fill()
for i in range(6):
    bgsketch.forward(length)
    bgsketch.left(60)
bgsketch.end_fill()

#Generating all the rest of the asteroids using the same logic and random positions
for i in range(0,random.randint(MIN_AST,MAX_AST)):
    colour=random.randint(0,1)
    for j in range(0,colour):
        bgsketch.color('blue')
    for j in range(0,0**colour):
        bgsketch.color('pink')
    bgsketch.setheading(random.randint(0,359))
    length=random.randint(5,30)
    bgsketch.up()
    bgsketch.goto(random.randint(-SCREEN_WIDTH//2, SCREEN_WIDTH//2), random.randint(-SCREEN_HEIGHT//2, SCREEN_HEIGHT//2))
    bgsketch.forward(length)
    bgsketch.left(120)
    bgsketch.down()
    bgsketch.begin_fill()
    for j in range(6):
        bgsketch.forward(length)
        bgsketch.left(60)
    bgsketch.end_fill()


#Oh functions, how I yearn for your sweet embrace.
####This following block of code has the main shooting loop, explosion animations and the score & shots remaining display.

#Some config for drawings.
explosionsketch.color('red')
explosionsketch.pensize(5)
scoresketch.color('green')
shotssketch.color('green')

attempts=screen.numinput("CHOOSE YOUR SHOTS TODAY","How many shots do you want to take?", maxval=500, minval=0)

#Main game loop
for i in range(int(attempts)):
    x=screen.numinput("X pos prompt","Choose an coordinate for your shot (-450 to 450)", minval=-450, maxval=450)
    y=screen.numinput("Y pos prompt","Choose an coordinate for your shot (-225 to 225)", minval=-225, maxval=225)

#Checks if the colour is not blue or pink and shows a miss if that's the case.
    for j in range(0**(check_pixel_color(x,y,'blue')+check_pixel_color(x,y,'pink'))):
        screen.tracer(True)
        scoresketch.up()
        scoresketch.goto(x-16,y)
        scoresketch.down()
        scoresketch.write(str('miss'))

#Checks if the colour is blue. If yes (on an asteroid), makes a little explosion and increments the points.
    for j in range(check_pixel_color(x,y,'blue')):
        explosionsketch.setheading(270)
        for k in range(1,20):
            screen.tracer(False)
            explosionsketch.up()
            explosionsketch.goto(x-k,y)
            explosionsketch.down()
            explosionsketch.begin_fill()
            explosionsketch.circle(k)
            explosionsketch.end_fill()
            screen.tracer(True)
            time.sleep(0.01)
#Shows the points and increments them
        scoresketch.up()
        scoresketch.goto(x-8,y)
        scoresketch.down()
        scoresketch.write(str('+'+str(BLUE_PTS)))
        SCORE+=BLUE_PTS

#Same code again but for pink asteroids
    for j in range(check_pixel_color(x,y,'pink')):
        explosionsketch.setheading(270)
        for k in range(1,20):
            screen.tracer(False)
            explosionsketch.up()
            explosionsketch.goto(x-k,y)
            explosionsketch.down()
            explosionsketch.begin_fill()
            explosionsketch.circle(k)
            explosionsketch.end_fill()
            screen.tracer(True)
            time.sleep(0.01)
        scoresketch.up()
        scoresketch.goto(x-8,y)
        scoresketch.down()
        scoresketch.write(str('+'+str(PINK_PTS)))
        SCORE+=PINK_PTS

    time.sleep(1)

#Score update! - The score clearing on the hits and misses is intentional to remove visual clutter. I could just use another turtle if I cared to keep it.
    scoresketch.up()
    scoresketch.goto(380, 205)
    scoresketch.down()
    scoresketch.clear()
    scoresketch.write(str('score:'+str(SCORE)))

#Shots remaining update!
    shotssketch.up()
    shotssketch.goto(-430,205)
    shotssketch.down()
    shotssketch.clear()
    shotssketch.write(str("Shots remaining:"+str(attempts-(i+1))))

    time.sleep(1)

####My lazy way of finishing the game because it doesn't feel complete without it
time.sleep(2)
bgsketch.clear()
explosionsketch.clear()
scoresketch.clear()
shotssketch.clear()

scoresketch.up()
scoresketch.goto(-150,0)
scoresketch.down()
scoresketch.write(str('GAME OVER!   FINAL SCORE:'+str(SCORE)+'   CLICK ANYWHERE TO EXIT'))

screen.exitonclick()