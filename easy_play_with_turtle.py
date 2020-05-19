i = 100
def how_to_use():    
    import turtle
    print("for shapes enter polygon() the number of sides a coma")
    print("then the a space lastly the size. ")
    print('circle(size) creates a circle.')

def polygon(length, sides):
    import turtle
    for side in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)
        print("side done")
    print("complete!")

def circle(size):
    import turtle
    for size in range (size + 30):
        turtle.forward(size)
        turtle.right(size)        


