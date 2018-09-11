# Getting depencies
from turtle import *
from random import randint

# Global vars
turn_degrees = 720
x_start_line = -160


# draw lines for turtle's race
# =============================
penup() # dont draw
goto(-140,150)
speed(15)
for step in range(17):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

# =============================
# Creating the turtles

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(x_start_line, 130)
laura.right(turn_degrees)
laura.pendown()

maria = Turtle()
maria.color('green')
maria.shape('turtle')
maria.penup()
maria.goto(x_start_line, 100)
maria.left(turn_degrees)
maria.pendown()

claudia = Turtle()
claudia.color('blue')
claudia.shape('turtle')
claudia.penup()
claudia.goto(x_start_line, 70)
claudia.right(turn_degrees)
claudia.pendown()

sonia = Turtle()
sonia.color('yellow')
sonia.shape('turtle')
sonia.penup()
sonia.goto(x_start_line, 40)
sonia.left(turn_degrees)
sonia.pendown()

diana = Turtle()
diana.color('magenta')
diana.shape('turtle')
diana.penup()
diana.goto(x_start_line, 10)
diana.right(turn_degrees)
diana.pendown()

# =============================
# move turtles
for movement in range(100):
    laura.forward(randint(1,6)) 
    maria.forward(randint(1,6))
    claudia.forward(randint(1,5))
    sonia.forward(randint(1,6))
    diana.forward(randint(1,5))
