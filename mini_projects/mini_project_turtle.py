# Python Tutorial for Beginners: Episode 8, Mini Project
# Turtle Drawings using turtle package

# import turtle
import turtle

# Let's get a nice set-up in turtle
turtle.bgcolor("black") # background color is black
turtle.pensize(2) # set pen size = 2
turtle.color("red")
turtle.speed(0) # speeds up instantaneous
# turtle.speed(10) # sets speed to 10

# draw a square
# turtle.forward(50) # move forward 50
# turtle.left(90) # turn 90 degrees
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done() # allows turtle to stay on screen

# Create a pretty graph
# for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colors)
#     turtle.circle(100)
#     turtle.left(60)
# turtle.done()

# make the drawing cooler
for i in range(6):
    for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)
turtle.done()