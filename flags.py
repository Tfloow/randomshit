import turtle
turtle.speed(0)
belgium = ["black", "yellow", "red", "v"]
france = ["blue", "white", "red", "v"]
deutschland = ["black", "red", "yellow", "h"]
netherlands = ["red", "white","#265B9C", "h"]
luxemburg = ["red", "white", "#12B3E3", "h"]


def Square(size, color):
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def Rectangle(height, width, color):
    turtle.penup()
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(1, 3):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    return height
    return width

def Flags(height, width, name):
    if name[3] == "h":
        for c in range(len(name)-1):
            turtle.goto(-width/2, height//2 - c * height//3)
            Rectangle(height//3,width,name[c])
    elif name[3] == "v":
        for c in range(len(name)-1):
            turtle.goto(-width/2 + c * width//3, height//2)
            Rectangle(height, width // 3, name[c])

#thomas 

def Star(heightStar, number, color):
    angle = 360 / number
    turtle.penup()
    turtle.color(color)
    turtle.goto(0, 0)
    for f in range(0, number):
        turtle.goto(-150, heightStar / 2)
        turtle.setheading(-90)
        turtle.circle(150, angle + angle * f)
        turtle.begin_fill()
        turtle.left(18)
        turtle.setheading(-72)
        turtle.pendown()
        for a in range(0, 5):
            turtle.forward(heightStar)
            turtle.left(-144)
        turtle.end_fill()
        turtle.penup()



Flags(400,600, netherlands)
Flags(400,600, luxemburg)
Flags(400,600, deutschland)
Flags(400,600, belgium)
Flags(400,600, france)
turtle.goto(-300, 200)
Rectangle(400, 600, "#0A4EAB")
Star(40, 12, "#FBD13D")
if str(turtle.textinput("square", "do you want a square ?")) == "yes":
    Square(300, "red")
turtle.exitonclick()
