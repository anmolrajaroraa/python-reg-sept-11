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
'''t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)'''
#t.circle(50)

#Loop for drawing square
#for variable_name in list/range:
'''for x in range(4):
    print('X is', x)
    print('Going to print another line')
    t.forward(100)
    print('Going to turn 90 degress')
    t.left(90)
    print('Done!')
print('Loop completed')'''

#t.circle(100)  #100 is radius
#t.dot(50)      #50 is diameter

#for i in range(8):
#    t.forward(100)
#    t.left(45)

#Code for drawing triangle
'''t.penup()
t.setposition(-300,-300)
t.pendown()
for i in range(30):
    for j in range(3):
        t.forward(10 * i)
        t.left(120)
    print("Triangle drawn!!")
    t.forward(10)'''

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise']
coordinates = list(range(-300,301))
print(coordinates)
for i in range(50):
    x = random.choice(coordinates)
    y = random.choice(coordinates)
    print(x,y)
    t.penup()
    t.setposition(x,y)
    t.color(random.choice(colors))
    t.pendown()
    t.dot(50)

#Code for drawing a plus sign
'''t.forward(100)
t.penup()
t.setposition(50,50)
t.pendown()
t.right(90)
t.forward(100)'''

t.left(90)
t.penup()
t.forward(100)
t.pendown()
#t.write("Circle", font=("Arial", 16, "normal"))
t.hideturtle()

