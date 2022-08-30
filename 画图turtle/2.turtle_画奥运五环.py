import turtle
#turtle.speed(0)
turtle.pensize(20)      #笔的大写

turtle.color('black')   #颜色
turtle.circle(100)

turtle.penup()          #抬笔
turtle.goto(-240,0)     #去的坐标
turtle.pendown()        #落笔

turtle.color('blue')
turtle.circle(100)

turtle.penup()
turtle.goto(240,0)
turtle.pendown()

turtle.color('red')
turtle.circle(100)

turtle.penup()
turtle.goto(120,-100)
turtle.pendown()

turtle.color('green')
turtle.circle(100)

turtle.penup()
turtle.goto(-120,-100)
turtle.pendown()

turtle.color('yellow')
turtle.circle(100)


turtle.done()