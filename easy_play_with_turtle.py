import sys

def rerun ():
    sys.exit
    

def polygon(length, sides):
    import turtle
    for side in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)
        print("side done")
    print("complete!")

def circle(size):
    import turtle
    for i  in range(100):
        turtle.forward(size/25)
        turtle.right(360/100)
    print('complete!')

def clear ():
    import turtle
    turtle.clear()

def goToUp(rightX, upY):
    import turtle
    turtle.penup()
    turtle.forward(rightX)
    turtle.left(90)
    turtle.forward(upY)
    turtle.right(90)
    turtle.pendown()
    print('complete!')
    
def goToDown (leftX, downY):
    import turtle
    turtle.penup()
    turtle.backward(leftX)
    turtle.left(90)
    turtle.backward(downY)
    turtle.right(90)
    turtle.pendown()
    print('complete!')

def demo ():
    circle(90)
    circle(-90)
    goToDown(0, 115)
    circle(90)
    goToUp(-30, 215)
    polygon(10, 4)
    goToUp(50, 0)
    polygon(10, 4)
    goToDown(30, 30)
    m = 10
    circle(9.5)
    for i in range(10):
        circle(m)
        m = m - 1
    goToDown(-5, 30)
    circle(20)
    goToUp(5, 125)
    n = 50
    for i in range(50):
        polygon(n, 4)
        n = n - 1
    goToDown(50, 0)
    n = 50
    for i in range(50):
        polygon(n, 4)
        n = n - 1

    goToUp(25, 50)
    n = 50
    for i in range(50):
        polygon(n, 4)
        n = n - 1

    goToUp(0, 50)
    n = 50
    for i in range(50):
        polygon(n, 4)
        n = n - 1
