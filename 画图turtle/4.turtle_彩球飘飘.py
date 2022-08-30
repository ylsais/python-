import turtle

#随机数
import random
turtle.speed(0)
for i in range(50):
    x=random.randint(-900,900)
    y=random.randint(-40,400)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.colormode(255)
    red=random.randint(0,255)
    green=red=random.randint(0,255)
    blue=red=random.randint(0,255)

    turtle.color(red,green,blue)
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.pensize(5)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.pensize(1)
turtle.done()
