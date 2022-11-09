import turtle as t

t.bgcolor('black')
t.pencolor('blue')
t.speed(0)

for i in range(190):
    for j in range(6):
        t.forward(i)
        t.left(46)
        t.hideturtle()
    t.left(33)
t.done()