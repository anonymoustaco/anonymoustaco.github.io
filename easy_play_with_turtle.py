def how_to_use():
    import turtle
    print("for shapes enter polygon() the number of sides a coma")
    print("then the a space lastly the size. ")

def polygon(length, sides):
    import turtle
    for side in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)
        print("side done")
    print("complete!")



