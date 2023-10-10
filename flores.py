import turtle 

rick = turtle.Turtle()

import turtle 

rick = turtle.Turtle()

def desenhe_flor():
    for _ in range(6):
        for _ in range(8):
            rick.forward(20)
            rick.right(30)
        rick.right(60)


desenhe_flor()
rick.penup()
rick.forward(150)
rick.pendown()
desenhe_flor()
rick.penup()
rick.forward(150)
rick.pendown()
desenhe_flor()
