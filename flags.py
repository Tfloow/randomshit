import turtle
import random
import math

turtle.bgcolor("#F3F4ED")
turtle.title("Made by Thomas")
turtle.setup(1080, 720, 0, 0)
turtle.speed(0)
belgium = ["black", "yellow", "red", "v"]
france = ["#265B9C", "white", "red", "v"]
deutschland = ["black", "red", "yellow", "h"]
netherlands = ["red", "white","#265B9C", "h"]
luxemburg = ["red", "white", "#12B3E3", "h"]
colorLgbtq = ["red", "orange", "yellow", "green", "blue", "purple"]
colorLgbtqi = ["black", "#945300", "#78D3FE", "#FAB8EC", "white", "#FFFB01"]
turtle.penup()

def Square(size, color):
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


def Rectangle(height, width, color, rot):
    turtle.penup()
    turtle.pendown()
    turtle.setheading(rot)
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

def Flags(height, width, name, pos1, pos2, rot):
    if name[3] == "h":
        for c in range(len(name)-1):
            turtle.goto(pos1, pos2 - c * height//3)
            turtle.pendown()
            Rectangle(height//3,width,name[c], rot)
            turtle.penup()
    elif name[3] == "v":
        for c in range(len(name)-1):
            turtle.goto(pos1 + c * width//3, pos2)
            turtle.pendown()
            Rectangle(height, width // 3, name[c], rot)
            turtle.penup()

#thomas

def Star(heightStar, number, color, rot, height,width, pos1, pos2):
    angle = 360 / number
    turtle.penup()
    turtle.color(color)
    turtle.goto(pos1 + math.ceil(width//4), pos2 - height//2 + heightStar//2)
    print(turtle.pos())
    for f in range(0, number):
        turtle.setheading(-90 + f * angle + rot)
        turtle.circle(width//4, angle)
        turtle.begin_fill()
        turtle.left(18)
        turtle.setheading(-72)
        turtle.pendown()
        for a in range(0, 5):
            turtle.forward(heightStar)
            turtle.left(-144)
        turtle.end_fill()
        turtle.penup()


def Brasil(height, width, pos1, pos2, rot):
    turtle.goto(pos1, pos2)
    turtle.setheading(0)
    Rectangle(height, width, "#00923E", rot)
    turtle.penup()
    turtle.goto(pos1 + width//12, 0)
    turtle.color("#F8C100")
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(35)
    turtle.forward(305)
    turtle.right(70)
    turtle.forward(305)
    turtle.right(110)
    turtle.forward(305)
    turtle.right(70)
    turtle.forward(305)
    turtle.end_fill()
    turtle.penup()
    turtle.color("#28166F")
    turtle.goto(-100,0)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.goto(97, -20)
    turtle.width(15)
    turtle.color("white")
    turtle.setheading(150)
    turtle.circle(400, 28)
    turtle.pensize(1)
    turtle.up()
    turtle.setheading(-90)
    turtle.fd(10)
    turtle.color("#00923E")
    turtle.write("ORDEM",True, align="left")
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(45)
    turtle.write("E ",True, align="left")
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(13)
    turtle.write("PRO",True, align="left")
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(3)
    turtle.write("GRE",True, align="left")
    turtle.fd(1)
    turtle.right(90)
    turtle.fd(10)
    turtle.write("SSO",True, align="left")
    turtle.goto(50,-20)
    turtle.color("white")
    for f in range(20):
        turtle.goto(float(random.randrange(-90,80)), float(random.randrange(-60, 0)))
        turtle.pendown()
        turtle.setheading(-72)
        turtle.begin_fill()
        length = random.randrange(1, 10)
        for a in range(0, 5):
            turtle.forward(length)
            turtle.left(-144)
        turtle.end_fill()
        turtle.penup()


def Lgbtq(height, width, pos1, pos2, rot):
    for i in range(6):
        turtle.goto(pos1, pos2 - i * height/6)
        Rectangle(height/6,width, colorLgbtq[i], rot)
    turtle.penup()
    for z in range(len(colorLgbtqi)):
        turtle.goto(pos1 + width//4 - z * width//20 ,pos2)
        turtle.pendown()
        turtle.color(colorLgbtqi[z])
        turtle.begin_fill()
        turtle.setheading(-45)
        turtle.fd(math.sqrt(height**2//2))
        turtle.right(90)
        turtle.fd(math.sqrt(height ** 2 // 2))
        turtle.right(45)
        turtle.forward(width//5)
        turtle.setheading(90)
        turtle.fd(height)
        turtle.right(90)
        turtle.fd(width//5)
        turtle.end_fill()
        turtle.penup()
    turtle.goto(pos1,pos2)
    turtle.setheading(-90)
    Rectangle(pos2 + height//2,pos1 + width//16,"#F3F4ED", 0)
    turtle.penup()
    turtle.setheading(-90)
    turtle.goto(pos1 + width//14, pos2 - height//2)
    turtle.color("#9C36EE")
    turtle.pensize(height//40)
    turtle.pendown()
    turtle.circle(50)
    turtle.pensize(1)
    turtle.penup()
    turtle.setheading(0)

def Europe(height, width, heightStar, number, color, rot, pos1,pos2):
    Rectangle(height, width, "#0A4EAB", rot)
    Star(heightStar, number, color, rot, height, width,pos1,pos2)


Flags(200,300, netherlands,-640,0,0)
Flags(200,300, luxemburg,-340 ,-60,0)
Flags(200,300, deutschland,-40, -160,0)
Flags(200,300, belgium, 260, -60,0)
Flags(200,300, france,-40, 40,0)
posEuX = int(turtle.textinput("posEu", "x EU?"))
posEuY = int(turtle.textinput("posEu", "y EU?"))
heightEu = int(turtle.textinput("Height flag", "height ?"))
turtle.goto(posEuX, posEuY)
Europe(heightEu, heightEu*1.5, heightEu//10, 12, "#FBD13D",0, posEuX, posEuY)

Brasil(400, 600, -300, 200, 0)
ans = str(turtle.textinput("square", "do you want a square ?"))
if ans == "yes":
    Square(300, "red")
elif ans == "phoebe":
    Lgbtq(heightEu, heightEu*1.5, posEuX, posEuY, 0)
turtle.goto(1000,0)
turtle.exitonclick()
