import turtle
import random
schildpad = turtle.Turtle()
schildpad.penup()
schildpad.goto(-700,400)
schildpad.pendown()
#schildpad.hideturtle()
schildpad.pensize(1)
schildpad.screen.bgcolor('black')
schildpad.speed(0)
for _ in range(150):

    list = []
    for _ in range(1000):
        getal = random.randint(10,40)
        list.append(getal)
        
    a = random.sample(list,)
    turtle.colormode(255)
    schildpad.color((random.randint(0,160),random.randint(0,50),random.randint(250,255)))
    for getal in a :
        schildpad.left(getal)
        schildpad.forward(100)
        schildpad.right(2*getal)
        schildpad.forward(100)
        schildpad.left(getal)
    schildpad.penup()
    schildpad.right(90)
    schildpad.forward(1)
    schildpad.right(90)
    schildpad.pendown()
    for getal in a :
        schildpad.right(getal)
        schildpad.forward(100)
        schildpad.left(2*getal)
        schildpad.forward(100)
        schildpad.right(getal)
    schildpad.penup()
    schildpad.left(90)
    schildpad.forward(1)
    schildpad.left(90)
    schildpad.pendown()

schildpad.goto(-700,400)
schildpad.right(90)

for _ in range(300):

    list = []
    for _ in range(1000):
        getal = random.randint(10,40)
        list.append(getal)
        
    a = random.sample(list,5)
    turtle.colormode(255)
    schildpad.color((random.randint(200,255),random.randint(250,255),random.randint(0,255)))
    for getal in a :
        schildpad.left(getal)
        schildpad.forward(100)
        schildpad.right(2*getal)
        schildpad.forward(100)
        schildpad.left(getal)
    schildpad.penup()
    schildpad.left(90)
    schildpad.forward(1)
    schildpad.left(90)
    schildpad.pendown()
    for getal in a :
        schildpad.right(getal)
        schildpad.forward(100)
        schildpad.left(2*getal)
        schildpad.forward(100)
        schildpad.right(getal)
    schildpad.penup()
    schildpad.right(90)
    schildpad.forward(1)
    schildpad.right(90)
    schildpad.pendown()


""" for _ in range(200):

    list = []
    for _ in range(1000):
        getal = random.randint(1,50)
        list.append(getal)
        
    a = random.sample(list,300)
    turtle.colormode(255)
    schildpad.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    for getal in a :
        
        schildpad.forward(getal)
        schildpad.left(getal)
        #schildpad.right(25**(getal/7-getal//7))

    schildpad.penup()
    schildpad.left(random.randint(1,360))
    schildpad.forward(100)
    schildpad.pendown() """

turtle.done()
    
