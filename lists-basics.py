Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [54,65,34,23,32,23,31,67,87,45,654,56,454,34,23]
>>> len(list1)
15
>>> list1[0]
54
>>> str1 = 'hello'
>>> str1 = ['h','e','l','l','o']
>>> str1[0]
'h'
>>> str1 = 'hello'
>>> str1[0]
'h'
>>> list1[0]
54
>>> list1[1]
65
>>> list1[14]
23
>>> list1[15]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list1[15]
IndexError: list index out of range
>>> list1[-1]
23
>>> list1[-2]
34
>>> list1[-3]
454
>>> list1[0:10]
[54, 65, 34, 23, 32, 23, 31, 67, 87, 45]
>>> list1[0:14]
[54, 65, 34, 23, 32, 23, 31, 67, 87, 45, 654, 56, 454, 34]
>>> list1[0:15]
[54, 65, 34, 23, 32, 23, 31, 67, 87, 45, 654, 56, 454, 34, 23]
>>> list1[0:25]
[54, 65, 34, 23, 32, 23, 31, 67, 87, 45, 654, 56, 454, 34, 23]
>>> list1[25:35]
[]
>>> list1[25]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list1[25]
IndexError: list index out of range
>>> list1[0:10]  #string or list slicing
[54, 65, 34, 23, 32, 23, 31, 67, 87, 45]
>>> list1[1] #indexing of list or string
65
>>> list1[-1,-10]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list1[-1,-10]
TypeError: list indices must be integers or slices, not tuple
>>> list1[-1:-10]
[]
>>> list1[1:10:1]  #starting index, stopping index, step
[65, 34, 23, 32, 23, 31, 67, 87, 45]
>>> list1[1:10:2]
[65, 23, 23, 67, 45]
>>> list1[1:10:3]
[65, 32, 67]
>>> list1[1:10:-1]
[]
>>> list1[10:1:-1]
[654, 45, 87, 67, 31, 23, 32, 23, 34]
>>> list1[-1:-10:-1]
[23, 34, 454, 56, 654, 45, 87, 67, 31]
>>> list1[-15]
54
>>> list1[-1:-15:-1]
[23, 34, 454, 56, 654, 45, 87, 67, 31, 23, 32, 23, 34, 65]
>>> list1[-1:-16:-1]
[23, 34, 454, 56, 654, 45, 87, 67, 31, 23, 32, 23, 34, 65, 54]
>>> list1[-1::-1]
[23, 34, 454, 56, 654, 45, 87, 67, 31, 23, 32, 23, 34, 65, 54]
>>> list1[::-1]
[23, 34, 454, 56, 654, 45, 87, 67, 31, 23, 32, 23, 34, 65, 54]
>>> list1[:]
[54, 65, 34, 23, 32, 23, 31, 67, 87, 45, 654, 56, 454, 34, 23]
>>> list1[:10]
[54, 65, 34, 23, 32, 23, 31, 67, 87, 45]
>>> list1[10:]
[654, 56, 454, 34, 23]
>>> list1[10::-1]
[654, 45, 87, 67, 31, 23, 32, 23, 34, 65, 54]
>>> 
>>> 
>>> 
>>> 
>>> list1 = [   [54,65,34]    ,    [23,32,23,31]   ,   [67,87,45,654,56]  ,  454  ,  34  ,  23   ]
>>> 
>>> list1[0]
[54, 65, 34]
>>> list1[1]
[23, 32, 23, 31]
>>> list1[2]
[67, 87, 45, 654, 56]
>>> list1[3]
454
>>> list1[2][3]
654
>>> #nested lists
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> #append vs extend
>>> 
>>> list1.append(100)
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100]
>>> list1.extend(100)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    list1.extend(100)
TypeError: 'int' object is not iterable
>>> list1.extend([100])
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100]
>>> 
>>> list1.append(200,300)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list1.append(200,300)
TypeError: append() takes exactly one argument (2 given)
>>> 
>>> for i in range(3):
	number = input("Enter the number to insert in list: ")
	list1.append(number)

	
Enter the number to insert in list: 200
Enter the number to insert in list: 300
Enter the number to insert in list: 400
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', '400']
>>> list1.append('ram')
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', '400', 'ram']
>>> list1[-2] = int(list1[-2])
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram']
>>> 
>>> 
>>> list1.extend(111,222,333)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    list1.extend(111,222,333)
TypeError: extend() takes exactly one argument (3 given)
>>> list1.extend([111,222,333])
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333]
>>> list1.extend('anmol')
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l']
>>> list1.append([111,222,333])
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333]]
>>> 
>>> 
>>> #append takes object as an argument - object means anything - number, string, list, tuple
>>> #append will add the object at the end of the list as it is
>>> 
>>> #extend takes iterable as an argument - iterable means list, tuple, dict, sets ,string(it is treated as a list of characters
>>> #extend extracts the value out of our iterable one by one and insert that value in the list
>>> 
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333]]
>>> list2 = list1
>>> list2
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333]]
>>> hex(id(list1))
'0x10aa18fc8'
>>> hex(id(list2))
'0x10aa18fc8'
>>> list3 = list1.copy()
>>> list3
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333]]
>>> hex(id(list3))
'0x10aa24888'
>>> list1.append('anmol')
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333], 'anmol']
>>> list2
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333], 'anmol']
>>> list3
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333]]
>>> list3[-1].append(444)
>>> list3
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444]]
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444], 'anmol']
>>> list3 = list1.copy()
>>> #shallow copy
>>> 
>>> 
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> list4
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444], 'anmol']
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444], 'anmol']
>>> list4[-2].append(555)
>>> list4
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444, 555], 'anmol']
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444], 'anmol']
>>> list1.count
<built-in method count of list object at 0x10aa18fc8>
>>> list1.count(34)
1
>>> list1.count(444)
0
>>> list1.count([111, 222, 333, 444])
1
>>> list1.count('ram')
1
>>> list1.count(100)
2
>>> list1[-2].count(444)
1
>>> list1.index(100)
6
>>> list1.index(100,7)
7
>>> list1.index(100,7)  #what to find, where to start
7

>>> list1.rindex(100)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    list1.rindex(100)
AttributeError: 'list' object has no attribute 'rindex'
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 100, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444], 'anmol']
>>> list1[6] = 999
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 999, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444], 'anmol']
>>> list1.insert(6, 888)
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 888, 999, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444], 'anmol']
>>> #list1[6] = 999    #will overwrite the existing value
>>> #list1.insert(6, 888)   #will push the other values ahead instead of overwriting
>>> list1.pop()
'anmol'
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 888, 999, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444]]
>>> list1.pop(6)
888
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 999, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', 'l', [111, 222, 333, 444]]
>>> list1.remove('l')
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 999, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', [111, 222, 333, 444]]
>>> #list1.pop()   will delete from the end
>>> #list1.pop(6)   will delete from 6th index
>>> #list1.remove('l')   will delete the first occurence specific value from list
>>> 
>>> 
>>> 
>>> list1.append(100)
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 999, 100, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', [111, 222, 333, 444], 100]
>>> list1.remove(100)
>>> list1
[[54, 65, 34], [23, 32, 23, 31], [67, 87, 45, 654, 56], 454, 34, 23, 999, '200', '300', 400, 'ram', 111, 222, 333, 'a', 'n', 'm', 'o', [111, 222, 333, 444], 100]
>>> list1.reverse()
>>> list1
[100, [111, 222, 333, 444], 'o', 'm', 'n', 'a', 333, 222, 111, 'ram', 400, '300', '200', 999, 23, 34, 454, [67, 87, 45, 654, 56], [23, 32, 23, 31], [54, 65, 34]]
>>> 
