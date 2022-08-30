import turtle

turtle.speed(0)
turtle.penup()
turtle.goto(-400,200)
turtle.color('red')
turtle.pendown()
turtle.begin_fill()
for i in range(4):
    if i%2==0:
        turtle.forward(800)
    else:
        turtle.forward(800*2/3)
    turtle.right(90)
#大
turtle.end_fill()
turtle.begin_fill()
turtle.penup()
turtle.color('yellow')
turtle.goto(-335,100)
turtle.pendown()
for i in range(5):
        turtle.forward(150)
        turtle.right(144)
turtle.end_fill()
#1
turtle.end_fill()
turtle.begin_fill()
turtle.penup()
turtle.right(30)
turtle.color('yellow')
turtle.goto(-180,12)
turtle.pendown()
for i in range(5):
        turtle.forward(50)
        turtle.right(144)
turtle.end_fill()
#2
turtle.end_fill()
turtle.begin_fill()
turtle.penup()
turtle.right(30)
turtle.color('yellow')
turtle.goto(-180,180)
turtle.pendown()
for i in range(5):
        turtle.forward(50)
        turtle.right(144)
turtle.end_fill()
#3
turtle.end_fill()
turtle.begin_fill()
turtle.penup()
turtle.right(30)
turtle.color('yellow')
turtle.goto(-100,60)
turtle.pendown()
for i in range(5):
        turtle.forward(50)
        turtle.right(144)
turtle.end_fill()
#4
turtle.end_fill()
turtle.begin_fill()
turtle.penup()
turtle.right(30)
turtle.color('yellow')
turtle.goto(-100,120)
turtle.pendown()
for i in range(5):
        turtle.forward(50)
        turtle.right(144)
turtle.end_fill()

turtle.hideturtle()
turtle.done()