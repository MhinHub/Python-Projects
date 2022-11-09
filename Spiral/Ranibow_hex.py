from turtle import *

bgcolor('black')
colors=['violet', '#4b0082', 'green', 'blue', 'yellow', 'orange', 'red']
speed(11)

for i in range(200):
    pencolor(colors[i%9])
    pensize(0)
    forward(i)
    left(59)
    
done()