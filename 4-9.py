import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
owen = turtle.Turtle()
owen.speed(20)
owen.color("hotpink")
side=5
owen.penup()
owen.goto(0,0) 
owen.pendown()
owen.pensize(3)

for i in range(5):
    owen.forward(100)
    owen.left(144)
