import turtle
import random
schildpad = turtle.Turtle()
turtle.speed(0)
schildpad.hideturtle()
schildpad.pensize(1)
schildpad.penup()
schildpad.goto(200,-200)
schildpad.pendown()
schildpad.screen.bgcolor('black')
schildpad.speed(0)
for _ in range(4):

    list = []
    for _ in range(1000):
        getal = random.randint(0,300)
        list.append(getal)
        
    a = random.sample(list,50)
    turtle.colormode(255)
    schildpad.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    for getal in a :
        
        schildpad.circle(getal)
        #schildpad.left(50)
        #schildpad.right(25**(getal/7-getal//7))

    schildpad.penup()
    schildpad.left(random.randint(45,135))
    schildpad.forward(300)
    schildpad.pendown()
turtle.done()
