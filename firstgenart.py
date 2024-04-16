import turtle
import random
schildpad = turtle.Turtle()
#schildpad.hideturtle()
schildpad.pensize(1)
for _ in range(200):

    list = []
    for _ in range(1000):
        getal = random.randint(1,20)
        list.append(getal)
        
    a = random.sample(list,100)
    turtle.colormode(255)
    schildpad.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    for getal in a :
        
        schildpad.forward(getal)
        schildpad.left(getal)
        #schildpad.right(25**(getal/7-getal//7))

    schildpad.penup()
    schildpad.left(random.randint(1,360))
    schildpad.forward(100)
    schildpad.pendown()
