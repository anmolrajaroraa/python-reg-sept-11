import turtle
s = turtle.Screen()
s.bgcolor('black') #background color
t = turtle.Pen()
t.color('white')
t.shape('turtle')
t.width(3)
t.turtlesize(2,2)  #it takes ratio - 2,2 means double the width and height
'''t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)'''
#t.circle(50)

#for variable_name in list/range:
for x in range(4):
    print('X is', x)
    print('Going to print another line')
    t.forward(100)
    print('Going to turn 90 degress')
    t.left(90)
    print('Done!')
t.left(90)
t.forward(100)
t.write("Square", font=("Arial", 16, "normal"))
t.hideturtle()
print('Loop completed')
