import turtle
import random
schildpad = turtle.Turtle()
schildpad.hideturtle()
schildpad.pensize(1)
schildpad.screen.bgcolor('black')
schildpad.speed(0)
for _ in range(6):

    list = []
    for _ in range(1000):
        getal = random.randint(20,50)
        list.append(getal)
        
    a = random.sample(list,36)
    turtle.colormode(255)
    schildpad.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    for getal in a :
        
        schildpad.circle(getal)
        #schildpad.left(50)
        #schildpad.right(25**(getal/7-getal//7))

    schildpad.penup()
    schildpad.left(60)
    schildpad.forward(200)
    schildpad.pendown()
turtle.done()