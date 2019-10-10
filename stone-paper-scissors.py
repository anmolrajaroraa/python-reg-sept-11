import turtle
import random

'''choice = input("What do you want to draw: ")

gameContinue = true

s = turtle.Screen()
s.bgcolor('black')

fred = turtle.Pen()
fred.width(4)
fred.shape('turtle')
fred.color('white')
fred.turtlesize(2,2)'''

userWins = 0
cpuWins = 0
draw = 0
gameChoices = [ 'stone' , 'paper' , 'scissors' ]


'''if choice == 'square':
    for i in [ 0 , 1 , 2 , 3 ] :
        fred.forward( 100 )
        fred.left( 90 )
elif choice == 'circle':
    fred.circle(50)   #radius
elif choice == 'dot':
    fred.dot(100)   #diameter
else:
    print('Shape not found!')'''

while True:

    #print('''1. Stone
#2. Paper
#3. Scissors''')

    userChoice = input( "Enter your choice : " )

    if userChoice == 'end':
        quit()
    elif userChoice not in gameChoices:
        print('Wrong choice')
        continue

    #gameChoice = range(3)
    cpuChoice = random.choice( gameChoices )
    print( cpuChoice )


    if userChoice == cpuChoice:
        print('game draw')
        draw = draw + 1
    elif userChoice == 'stone':
        if cpuChoice == 'paper':
            print('Cpu won')
            cpuWins = cpuWins + 1
        else:
            print('User won')
            userWins = userWins + 1
    elif userChoice == 'paper':
        if cpuChoice == 'scissors':
            print('Cpu won')
            cpuWins = cpuWins + 1
        else:
            print('User won')
            userWins = userWins + 1
    elif userChoice == 'scissors':
        if cpuChoice == 'stone':
            print('Cpu won')
            cpuWins = cpuWins + 1
        else:
            print('User won')
            userWins = userWins + 1

    print(f"Score -> User : {userWins}, CPU : {cpuWins}, Drawn : {draw}, Matches Played : {userWins + cpuWins + draw}" )