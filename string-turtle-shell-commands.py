Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = 'python is very easy to learn learn, it has got easy syntax, it\'s has "very" reliable data structures, but it has got no switch case'
>>> str1.split()
['python', 'is', 'very', 'easy', 'to', 'learn', 'learn,', 'it', 'has', 'got', 'easy', 'syntax,', "it's", 'has', '"very"', 'reliable', 'data', 'structures,', 'but', 'it', 'has', 'got', 'no', 'switch', 'case']
>>> #tokenization
>>> str1.split(',')
['python is very easy to learn learn', ' it has got easy syntax', ' it\'s has "very" reliable data structures', ' but it has got no switch case']
>>> str1.partition(',')
('python is very easy to learn learn', ',', ' it has got easy syntax, it\'s has "very" reliable data structures, but it has got no switch case')
>>> str1 = 'python is very easy to learn learn$ it has got easy syntax$ it\'s has "very" reliable data structures$ but it has got no switch case'
>>> str1.split('$')
['python is very easy to learn learn', ' it has got easy syntax', ' it\'s has "very" reliable data structures', ' but it has got no switch case']
>>> str1.partition('$')
('python is very easy to learn learn', '$', ' it has got easy syntax$ it\'s has "very" reliable data structures$ but it has got no switch case')
>>> str1.rpartition('$')
('python is very easy to learn learn$ it has got easy syntax$ it\'s has "very" reliable data structures', '$', ' but it has got no switch case')
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import turtle
>>> turtle.Pen()
<turtle.Turtle object at 0x10c9be1d0>
>>> turtle.shape('turtle')
>>> turtle.turtlesize(2,2)
>>> turtle.forward(100)
>>> turtle.width(3) #size for line drawn by turtle
>>> turtle.forward(100)
>>> turtle.reset()
>>> turtle.width(3)
>>> turtle.turtlesize(2,2)
>>> turtle.forward(100)
>>> turtle.color('red')
>>> turtle.forward(100)
>>> turtle.forward(100)
>>> turtle.left(20)
>>> turtle.left(20)
>>> turtle.left(50)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
>>> str1
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    str1
NameError: name 'str1' is not defined
>>> str1 = 'hello'
>>> str1[0]
'h'
>>> str1[0:2]
'he'
>>> str1[0:3]
'hel'
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(10,14))
[10, 11, 12, 13]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10,14))
[10, 11, 12, 13]
>>> list(range(10,50))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list(range(50))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> 
>>> 
>>> list(range(10,50,2))
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> list(range(10,50,3))
[10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49]
>>> list(range(10,50,-1))
[]
>>> list(range(50,10,-1))
[50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> range(10,50,-1)
range(10, 50, -1)
>>> reversed(range(10,50,1))
<range_iterator object at 0x1027bcd50>
>>> list(reversed(range(10,50,1)))
[49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> list(range(10,50,1))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list(reversed(range(10,50,1)))
[49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
>>> 
>>> 
>>> list(range(4))
[0, 1, 2, 3]
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
0
1
2
3
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
X is 0
Going to print another line
Going to turn 90 degress
Done!
X is 1
Going to print another line
Going to turn 90 degress
Done!
X is 2
Going to print another line
Going to turn 90 degress
Done!
X is 3
Going to print another line
Going to turn 90 degress
Done!
Loop completed
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
X is 0
Going to print another line
Going to turn 90 degress
Done!
X is 1
Going to print another line
Going to turn 90 degress
Done!
X is 2
Going to print another line
Going to turn 90 degress
Done!
X is 3
Going to print another line
Going to turn 90 degress
Done!
Loop completed
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
X is 0
Going to print another line
Going to turn 90 degress
Done!
X is 1
Going to print another line
Going to turn 90 degress
Done!
X is 2
Going to print another line
Going to turn 90 degress
Done!
X is 3
Going to print another line
Going to turn 90 degress
Done!
Loop completed
>>> import turtle
>>> turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    turtle.Pen()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3816, in __init__
    visible=visible)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2557, in __init__
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2660, in _update
    self._update_data()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    turtle.Pen()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3816, in __init__
    visible=visible)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2557, in __init__
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2660, in _update
    self._update_data()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/turtle-basics.py 
X is 0
Going to print another line
Going to turn 90 degress
Done!
X is 1
Going to print another line
Going to turn 90 degress
Done!
X is 2
Going to print another line
Going to turn 90 degress
Done!
X is 3
Going to print another line
Going to turn 90 degress
Done!
Loop completed
>>> 
