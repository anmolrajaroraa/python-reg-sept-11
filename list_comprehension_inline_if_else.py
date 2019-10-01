Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 33/2
16.5
>>> 33%2
1
>>> 33%7
5
>>> 35%7
0
>>> number = 97
>>> list(range(2,48.5))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(range(2,48.5))
TypeError: 'float' object cannot be interpreted as an integer
>>> list(range(2,number/2))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(range(2,number/2))
TypeError: 'float' object cannot be interpreted as an integer
>>> number / 2
48.5
>>> number // 2
48
>>> 
>>> 
>>> list(range(2, 48))
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
>>> list(range(2, 48+1))
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import os
>>> os.getcwd()    #get current working directory
'/Users/anmolrajarora/Documents'
>>> os.chdir('/Users/anmolrajarora/Documents/python')     #change directory
>>> os.listdir()
['01-PythonIntroduction.wmv', 'PythonPygame_2.wmv', '.DS_Store', 'PythonPygame_!.wmv', '01-Python.wmv', 'PythonFunctionsIntro_1.wmv', 'PythonFunctions_2.wmv', 'PythonFilterMapLambda.wmv', 'PythonFunctionsIntro.wmv', 'Crawling_2.wmv', 'PythonIfElse.wmv', 'Crawling_1.wmv', 'Python_IfElse+List.wmv']
>>> songs = os.listdir()
>>> import random
>>> song = random.choice(songs)
>>> song
'PythonPygame_2.wmv'
>>> song = random.choice(songs)
>>> song
'Python_IfElse+List.wmv'
>>> song = random.choice(songs)
>>> song
'PythonFunctions_2.wmv'
>>> 
>>> import subprocess
>>> subprocess.call(['open', song])
0
>>> os.chdir('/Users/anmolrajarora/Documents/python-reg-sept-11')     #change directory
>>> os.getcwd()
'/Users/anmolrajarora/Documents/python-reg-sept-11'
>>> os.listdir()
['prime-number.py', 'print-basics.py', 'python-basics.py', 'list_datetime.py', 'string_functions.py', 'turtle-for-if-else-random.py', 'string-turtle-shell-commands.py', 'chatbot.py', 'nested-loops.py', 'lists-basics.py', 'turtle-basics.py', '.idea']
>>> songs = os.listdir()
>>> songs
['prime-number.py', 'print-basics.py', 'python-basics.py', 'list_datetime.py', 'string_functions.py', 'turtle-for-if-else-random.py', 'string-turtle-shell-commands.py', 'chatbot.py', 'nested-loops.py', 'lists-basics.py', 'turtle-basics.py', '.idea']
>>> song = random.choice(songs)
>>> song
'turtle-basics.py'
>>> subprocess.call(['open', song])
0
>>> 
>>> 
>>> a = 10
>>> b = 20
>>> diff = a - b
>>> diff
-10
>>> if a > b:
	pass
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if a > b:
	diff = a - b
else:
	diff = b - a

	
>>> diff
10
>>> a = 80
>>> b = 20
>>> if a > b:
	diff = a - b
else:
	diff = b - a

	
>>> diff
60
>>> 
>>> 
>>> #Inline if-else
>>> 
>>> diff = (a - b) if (a > b) else (b - a)
>>> diff
60
>>> a = 10
>>> b = 20
>>> diff = (a - b) if (a > b) else (b - a)
>>> diff
10
>>> 
>>> 
>>> 
>>> #List Comprehension
>>> 
>>> evenList = []
>>> for i in range(1,101):
	if i % 2 == 0:
		evenList.append(i)

		
>>> evenList
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> for i in range(1,101):
	if i % 2 == 0:
		evenList.append(i)
	else:
		evenList.append('x')

		
>>> evenList
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 'x', 2, 'x', 4, 'x', 6, 'x', 8, 'x', 10, 'x', 12, 'x', 14, 'x', 16, 'x', 18, 'x', 20, 'x', 22, 'x', 24, 'x', 26, 'x', 28, 'x', 30, 'x', 32, 'x', 34, 'x', 36, 'x', 38, 'x', 40, 'x', 42, 'x', 44, 'x', 46, 'x', 48, 'x', 50, 'x', 52, 'x', 54, 'x', 56, 'x', 58, 'x', 60, 'x', 62, 'x', 64, 'x', 66, 'x', 68, 'x', 70, 'x', 72, 'x', 74, 'x', 76, 'x', 78, 'x', 80, 'x', 82, 'x', 84, 'x', 86, 'x', 88, 'x', 90, 'x', 92, 'x', 94, 'x', 96, 'x', 98, 'x', 100]
>>> evenList = []
>>> for i in range(1,101):
	if i % 2 == 0:
		evenList.append(i)
	else:
		evenList.append('x')

		
>>> evenList
['x', 2, 'x', 4, 'x', 6, 'x', 8, 'x', 10, 'x', 12, 'x', 14, 'x', 16, 'x', 18, 'x', 20, 'x', 22, 'x', 24, 'x', 26, 'x', 28, 'x', 30, 'x', 32, 'x', 34, 'x', 36, 'x', 38, 'x', 40, 'x', 42, 'x', 44, 'x', 46, 'x', 48, 'x', 50, 'x', 52, 'x', 54, 'x', 56, 'x', 58, 'x', 60, 'x', 62, 'x', 64, 'x', 66, 'x', 68, 'x', 70, 'x', 72, 'x', 74, 'x', 76, 'x', 78, 'x', 80, 'x', 82, 'x', 84, 'x', 86, 'x', 88, 'x', 90, 'x', 92, 'x', 94, 'x', 96, 'x', 98, 'x', 100]
>>> 
>>> 
>>> evenList = []
>>> evenList = [i for i in range(1,101)]
>>> evenList
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> evenList = [for i in range(1,101)]
SyntaxError: invalid syntax
>>> evenList = [i for i in range(1,101)]
>>> 
>>> 
>>> evenList = [(i / 2) for i in range(1,101)]
>>> evenList
[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0]
>>> evenList = [(i ** 2) for i in range(1,101)]
>>> evenList
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
>>> evenList = [i for i in range(2,101,2)]
>>> evenList
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> evenList = [i for i in range(1,101) if (i % 2 == 0)]
>>> evenList
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> evenList = [i for i in range(1,101) if (i % 2 == 0 or i % 3 == 0)]
>>> evenList
[2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 44, 45, 46, 48, 50, 51, 52, 54, 56, 57, 58, 60, 62, 63, 64, 66, 68, 69, 70, 72, 74, 75, 76, 78, 80, 81, 82, 84, 86, 87, 88, 90, 92, 93, 94, 96, 98, 99, 100]
>>> evenList = [i for i in range(1,101) if (i % 2 == 0 or i % 3 == 0) else 'x']
SyntaxError: invalid syntax
>>> 
>>> 
>>> evenList = [i if (i % 2 == 0 and i % 3 == 0) else 'x' for i in range(1,101)]
>>> evenList
['x', 'x', 'x', 'x', 'x', 6, 'x', 'x', 'x', 'x', 'x', 12, 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 'x', 'x', 'x', 24, 'x', 'x', 'x', 'x', 'x', 30, 'x', 'x', 'x', 'x', 'x', 36, 'x', 'x', 'x', 'x', 'x', 42, 'x', 'x', 'x', 'x', 'x', 48, 'x', 'x', 'x', 'x', 'x', 54, 'x', 'x', 'x', 'x', 'x', 60, 'x', 'x', 'x', 'x', 'x', 66, 'x', 'x', 'x', 'x', 'x', 72, 'x', 'x', 'x', 'x', 'x', 78, 'x', 'x', 'x', 'x', 'x', 84, 'x', 'x', 'x', 'x', 'x', 90, 'x', 'x', 'x', 'x', 'x', 96, 'x', 'x', 'x', 'x']
>>> evenList = [i if (i % 2 == 0 or i % 3 == 0) else 'x' for i in range(1,101)]
>>> evenList
['x', 2, 3, 4, 'x', 6, 'x', 8, 9, 10, 'x', 12, 'x', 14, 15, 16, 'x', 18, 'x', 20, 21, 22, 'x', 24, 'x', 26, 27, 28, 'x', 30, 'x', 32, 33, 34, 'x', 36, 'x', 38, 39, 40, 'x', 42, 'x', 44, 45, 46, 'x', 48, 'x', 50, 51, 52, 'x', 54, 'x', 56, 57, 58, 'x', 60, 'x', 62, 63, 64, 'x', 66, 'x', 68, 69, 70, 'x', 72, 'x', 74, 75, 76, 'x', 78, 'x', 80, 81, 82, 'x', 84, 'x', 86, 87, 88, 'x', 90, 'x', 92, 93, 94, 'x', 96, 'x', 98, 99, 100]
>>> 
>>> 
>>> #   what to append in list - can be an expression (can include inline if-else)  for loop   if condition (optional)
