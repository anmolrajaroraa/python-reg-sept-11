from datetime import *
import os
import random
import subprocess #for mac only

helloIntent = ['hello', 'hi', 'hola', 'bonjour', 'helloooo', 'vanakkam']
timeIntent = ['what\'s the time', 'tell me the current time', 'time please']
dateIntent = ["what's the date today", 'tell me today\'s date', 'date please']
musicIntent = ['play a random song', 'play some song', 'play a song for me', 'music please']

while True:
    message = input( "Enter your message: " )

    # if message == 'hello' or message == 'hi' or message == 'hola' or message == 'bonjour':
    if message in helloIntent:
        print('hi!')
    elif message == 'how are you' or message == 'how you doing':
        print("I am fine! What about you?")
    elif message == 'i am great' or message == 'i am fine':
        print("That's great!!")
    elif message in timeIntent:
        now = datetime.now( )
        print(now.strftime("%a %d %b %Y %H:%M:%S %p"))
        print()
    elif message in dateIntent:
        today = date.today( )
        print(f"Date is: {today.day}/{today.month}/{today.year}" )
    elif message in musicIntent:
        os.chdir('/Users/anmolrajarora/Documents/aws' )
        songs = os.listdir( )
        song = random.choice( songs )
        #os.startfile( song ) # for windows
        subprocess.call( [ 'open' , song ] )  # for mac
    elif message == 'new':
        print('nothing new')
    elif message == 'bye' or message == 'stop':
        print('see you later!')
        break
    else:
        print('Unable to understand :(')



'''a = 10000
b = 1000


if a > b:
    print('a is greater')
elif b > a:
    print('b is greater')
else:
    print('a and b are equal')'''












