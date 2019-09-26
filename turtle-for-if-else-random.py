import turtle
import random

s = turtle.Screen()
s.bgcolor('black') #background color
t = turtle.Pen()
t.color('white')
t.shape('turtle')
t.width(3)
t.turtlesize(2,2)  #it takes ratio - 2,2 means double the width and height
t.speed(0) #1 - slow, 10 - fast, by default it takes 0 which is fastest
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise']
coordinates = list(range(-300,301))
#shapes = ["square", "triangle", "circle", "dot", "octagon"]
shapes = list(range(5))
print(shapes)

for i in range(50):
    x = random.choice(coordinates)
    y = random.choice(coordinates)
    shape = random.choice(shapes)
    #print(shape)
    t.color(random.choice(colors))
    t.penup()
    t.setposition(x,y)
    t.pendown()
    #if shape == "square":   #  == is used for comparison between two values
    '''print("Checking for square!!")
    if shape == 0:
        for j in range(4):
            t.forward(100)
            t.left(90)
        print("Square drawn!!")
    #if shape == "triangle":
    print("Checking for triangle!!")
    if shape == 1:
        for j in range(3):
            t.forward(100)
            t.left(120)
    #if shape == "circle":
    print("Checking for circle!!")
    if shape == 2:
        t.circle(100)
    #if shape == "dot":
    print("Checking for dot!!")
    if shape == 3:
        t.dot(100)
    #if shape == "octagon":
    print("Checking for octagon!!")
    if shape == 4:
        for i in range(8):
            t.forward(100)
            t.left(45)'''

    if shape == 0:
        for j in range(4):
            t.forward(100)
            t.left(90)
        print("Square drawn!!")
    #else and then if
    elif shape == 1:
        for j in range(3):
            t.forward(100)
            t.left(120)
    elif shape == 2:
        t.circle(100)
    elif shape == 3:
        t.dot(100)
    else:
        for i in range(8):
            t.forward(100)
            t.left(45)

