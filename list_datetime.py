Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [54,65,34,23,32,23,31,67,87,45,654,56,454,34,23]
>>> list1.sort()
>>> list1
[23, 23, 23, 31, 32, 34, 34, 45, 54, 56, 65, 67, 87, 454, 654]
>>> list1.sort(reverse=True)
>>> list1
[654, 454, 87, 67, 65, 56, 54, 45, 34, 34, 32, 31, 23, 23, 23]
>>> #list1.sort()  #ascending
>>> #list1.sort(reverse=True)  #descending
>>> 
>>> 
>>> list1 = [54,65,34,23,32,23,31,67,87,45,654,56,454,34,23]
>>> list1.reverse()
>>> list1
[23, 34, 454, 56, 654, 45, 87, 67, 31, 23, 32, 23, 34, 65, 54]
>>> 
>>> 
>>> list1.append('anmol')
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> list1
[23, 23, 23, 31, 32, 34, 34, 45, 54, 56, 65, 67, 87, 454, 654, 'anmol']
>>> 
>>> 
>>> list1 = ['54','65','34','23','32','23','31','67','87','45','654','56','454','34','23', 'anmol']
>>> list1.sort()
>>> list1 = ['54','65','34','23','32','23','31','67','87','45','654','56','454','34','23', 'anmol', 99]
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> 
>>> 
>>> 
>>> list1 = ['54','65','34','23','32','23','31','67','87','45','654','56','454','34','23', 'anmol']
>>> list1.sort()
>>> list1
['23', '23', '23', '31', '32', '34', '34', '45', '454', '54', '56', '65', '654', '67', '87', 'anmol']
>>> list1.sort(reverse=True)
>>> list1
['anmol', '87', '67', '654', '65', '56', '54', '454', '45', '34', '34', '32', '31', '23', '23', '23']
>>> 
>>> #for string, sorting will be based on ascii values starting from first character itself
>>> #for numbers, they are directly compared with each other
>>> 
>>> 
>>> list1 = [  [ 101, 'anmol' ],  [ 103, 'ram' ],  [ 102, 'shyam']   ]
>>> list1.sort()
>>> list1 = [  [ 101, 'anmol' ],  [ 103, 'ram' ],  [ 102, 'shyam'] , 99  ]
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'int' and 'list'
>>> 
>>> 
>>> 
>>> list1 = [  [ 101, 'anmol' ],  [ 103, 'ram' ],  [ 102, 'shyam']   ]
>>> list1.sort()
>>> list1
[[101, 'anmol'], [102, 'shyam'], [103, 'ram']]
>>> list1 = [  [ 101, 'anmol' ],  [ 103, 'ram' ],  [ 103, 'shyam'] , [ 102, 'z']  ]
>>> list1.sort()
>>> list1
[[101, 'anmol'], [102, 'z'], [103, 'ram'], [103, 'shyam']]
>>> list1 = [  [ 101, 'anmol' ],  [ 103, 'ram' ],  [ 103, 'shyam'] , [ 102, 'z'] , [103, 'annie'] ]
>>> list1.sort()
>>> list1
[[101, 'anmol'], [102, 'z'], [103, 'annie'], [103, 'ram'], [103, 'shyam']]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2019, 9, 27, 12, 11, 33, 951251)
>>> print(datetime.datetime.now())
2019-09-27 12:11:51.951336
>>> 
>>> 
>>> 
>>> from datetime import *
>>> datetime.now()
datetime.datetime(2019, 9, 27, 12, 13, 0, 108180)
>>> date.today()
datetime.date(2019, 9, 27)
>>> 
>>> now = datetime.now()
>>> print(now)
2019-09-27 12:14:28.378952
>>> print(now)
2019-09-27 12:14:28.378952
>>> now = datetime.now()
>>> print(now)
2019-09-27 12:15:08.113271
>>> 
>>> 
>>> 
>>> now.strftime("%y %Y")    #string format for time
'19 2019'
>>> now.strftime("%d")
'27'
>>> now.strftime("%D")
'09/27/19'
>>> now.strftime("%a")
'Fri'
>>> now.strftime("%A")
'Friday'
>>> now.strftime("%b")
'Sep'
>>> now.strftime("%B")
'September'
>>> now.strftime("%c")
'Fri Sep 27 12:15:08 2019'
>>> now.strftime("%a %b %d %Y %H:%M:%S %P")
'Fri Sep 27 2019 12:15:08 P'
>>> now.strftime("%a %b %d %Y %H:%M:%S %p")
'Fri Sep 27 2019 12:15:08 PM'
>>> now.strftime("%s")
'1569566708'
>>> 
>>> 
>>> 
>>> 
>>> list1 = [1,2,3,4,5]
>>> 
>>> for item in list1:
	print(item)

	
1
2
3
4
5
>>> 
>>> 
>>> 
>>> 
>>> 5 in list1
True
>>> 50 in list1
False
>>> 5 not in list1
False
>>> 50 not in list1
True
>>> 
>>> 
>>> 
>>> a = 10
>>> b = 20
>>> if a > b:
	print('a is greater')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
