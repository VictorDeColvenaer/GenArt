import turtle
import random
schildpad = turtle.Turtle()
schildpad.hideturtle()
schildpad.pensize(3)
schildpad.speed(0)

for _ in range(200):

    list = []
    for _ in range(1000):
        getal = random.randint(100,200)
        list.append(getal)
        
    a = random.sample(list,4)
    turtle.colormode(255)
    schildpad.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    for getal in a :

        schildpad.forward(getal)
        schildpad.penup()
        schildpad.left(random.randint(85,95))
        schildpad.forward(random.randint(0,50))
        schildpad.pendown()
