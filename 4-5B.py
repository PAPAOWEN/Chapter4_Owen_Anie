import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
owen = turtle.Turtle()
owen.speed(20)
owen.color("blue")
side=5
owen.penup()
owen.goto(0,0) 
owen.pendown()
owen.pensize(3)

for i in range (91):
    owen.forward(side)
    owen.left(91)
    side=side+5


owen.penup()
owen.goto(500,500)