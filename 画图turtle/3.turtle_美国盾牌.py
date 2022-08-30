import turtle
turtle.penup()
turtle.goto(0,-90)
turtle.pendown()
turtle.color('red')
#turtle.speed(0)
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-40)
turtle.pendown()
turtle.color('white')

turtle.begin_fill()         #填充开始
turtle.circle(150)
turtle.end_fill()           #填充结束



turtle.penup()
turtle.goto(0,10)
turtle.pendown()
turtle.color('red')

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(0,60)
turtle.pendown()
turtle.color('blue')

turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(-49,125)
turtle.pendown()
turtle.color('white')

turtle.begin_fill()

for i in range(5):
    turtle.forward(97)          #向前
    turtle.right(144)

turtle.end_fill()
turtle.hideturtle()             #补全turtle
turtle.done()

