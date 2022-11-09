import turtle as t

t.speed(0)
t.bgcolor("black")
t.pensize(1)

def tree(branchLen, t):
    if branchLen > 4:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
        
def main():
    myWin=t.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    tree(105,t)
    myWin.exitonclick()
    
main()