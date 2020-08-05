import turtle
t = turtle.Turtle()
t.right(90)

def pig(steps, angle):
    #face
    roll(steps,angle)
    #nose
    t.left(82)
    t.penup()
    t.backward(150)
    t.pendown()
    roll(steps - 7, angle)
    #nostril
    t.left(82)
    t.penup()
    t.backward(20)
    t.pendown()
    roll(steps - 9, angle)
    t.left(8)
    t.penup()
    t.backward(30)
    t.pendown()
    roll(steps - 9, angle)
    #eyes
    t.right(90)
    t.penup()
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.pendown()
    roll(steps - 8, angle)
    t.left(210)
    t.penup()
    t.forward(90)
    t.pendown()
    roll(steps - 8, angle)
    #pupil
    t.right(90)
    t.penup()
    t.forward(10)
    t.pendown()
    roll(steps - 9.5, angle)
    t.right(115)
    t.penup()
    t.forward(95)
    t.pendown()
    roll(steps - 9.5, angle)


def roll(steps, angle):
    for i in range(360//angle):
        t.forward(steps)
        t.right(angle)
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('pink')
t.pensize(4)
pig(10, 5)
t.hideturtle()
turtle.done()