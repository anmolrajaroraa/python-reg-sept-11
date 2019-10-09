Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple1 = (10,20, (102,103,104), [101,201,301] )
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> tuple1.count(10)
1
>>> 
>>> tuple1.count()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple1.count()
TypeError: count() takes exactly one argument (0 given)
>>> tuple1.count((102,103,104))
1
>>> 
>>> tuple1.index((102,103,104))
2
>>> #immutable - cannot be changed
>>> tuple1[2] = (10,20,30)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tuple1[2] = (10,20,30)
TypeError: 'tuple' object does not support item assignment
>>> 
>>> tuple1[-1]
[101, 201, 301]
>>> tuple1[-1][0] = 'hello'
>>> tuple1
(10, 20, (102, 103, 104), ['hello', 201, 301])
>>> 
>>> tuple1[-1].clear()
>>> tuple1
(10, 20, (102, 103, 104), [])
>>> hex(id(tuple1[-1]))
'0x1109aab88'
>>> tuple1[-1].append(101)
>>> tuple1
(10, 20, (102, 103, 104), [101])
>>> hex(id(tuple1[-1]))
'0x1109aab88'
>>> 
>>> 
>>> set1 = {1,2,3,4,5,6,1,3,4,5}
>>> set1
{1, 2, 3, 4, 5, 6}
>>> 
>>> set1 = {1,2,3,4,5,6,1,3,4,5, 'hello}
	
SyntaxError: EOL while scanning string literal
>>> set1 = {1,2,3,4,5,6,1,3,4,5, 'hello', 'anmol', 'siddharth', 'python', True}
>>> set1
{1, 2, 3, 4, 5, 6, 'siddharth', 'hello', 'anmol', 'python'}
>>> set1 = {1,2,3,4,5,6,1,3,4,5, 'hello', 'anmol', 'siddharth', 'python', True, False}
>>> 
>>> set1
{False, 1, 2, 3, 4, 5, 6, 'siddharth', 'hello', 'anmol', 'python'}
>>> 
>>> 
>>> int(True)
1
>>> set1 = {1,2,3,4,5,6,1,3,4,5, 'hello', 'anmol', 'siddharth', 'python', True, False, 0}
>>> set1
{False, 1, 2, 3, 4, 5, 6, 'siddharth', 'hello', 'anmol', 'python'}
>>> 
>>> 
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

>>> 
>>> 
>>> set1[0]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    set1[0]
TypeError: 'set' object is not subscriptable
>>> set1[1]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    set1[1]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> for item in set1:
	print(item)

	
False
1
2
3
4
5
6
siddharth
hello
anmol
python
>>> 
>>> 
>>> set1.pop()
False
>>> set1.pop()
1
>>> set1.pop()
2
>>> set1.pop()
3
>>> set1.pop()
4
>>> set1
{5, 6, 'siddharth', 'hello', 'anmol', 'python'}
>>> 
>>> set1.add(100)
>>> set1.add('js')
>>> 
>>> set1
{'js', 100, 5, 6, 'siddharth', 'hello', 'anmol', 'python'}
>>> set1.add('java')
>>> 
>>> set1
{'js', 100, 5, 6, 'siddharth', 'hello', 'anmol', 'python', 'java'}
>>> 
>>> #set1 - set2  ->  all the elements present in set1 that are not present in set2  (difference)
>>> 
>>> set2 = {100, 'java', 'js'}
>>> 
>>> 
>>> set1 - set2
{'siddharth', 5, 6, 'hello', 'anmol', 'python'}
>>> set1
{'js', 100, 5, 6, 'siddharth', 'hello', 'anmol', 'python', 'java'}
>>> set1.difference(set2)   #set1 - set2
{'siddharth', 5, 6, 'hello', 'anmol', 'python'}
>>> 
>>> 
>>> set1
{'js', 100, 5, 6, 'siddharth', 'hello', 'anmol', 'python', 'java'}
>>> set1.difference_update(set2)
>>> set1
{5, 6, 'siddharth', 'hello', 'anmol', 'python'}
>>> 
>>> 
>>> set1.intersection(set2)
set()
>>> set1 = {'js', 100, 5, 6, 'siddharth', 'hello', 'anmol', 'python', 'java'}
>>> set1.intersection(set2)
{'js', 100, 'java'}
>>> set1.union(set2)
{'js', 100, 'siddharth', 5, 6, 'hello', 'anmol', 'python', 'java'}
>>> 
>>> 
>>> set1.isdisjoint(set2)
False
>>> 
>>> 
>>> set1.difference_update(set2)
>>> set1
{'siddharth', 5, 6, 'hello', 'anmol', 'python'}
>>> set2
{'js', 100, 'java'}
>>> set1.isdisjoint(set2)
True
>>> 
>>> set1 = {'js', 100, 5, 6, 'siddharth', 'hello', 'anmol', 'python', 'java'}
>>> 
>>> set1
{'js', 100, 'siddharth', 5, 6, 'hello', 'anmol', 'python', 'java'}
>>> set2
{'js', 100, 'java'}
>>> 
>>> 
>>> set2.issubset(set1)
True
>>> set1.issuperset(set2)
True
>>> 
>>> set1
{'js', 100, 'siddharth', 5, 6, 'hello', 'anmol', 'python', 'java'}
>>> set1.discard('java')
>>> set1
{'js', 100, 'siddharth', 5, 6, 'hello', 'anmol', 'python'}
>>> set1.discard('java')
>>> set1.pop('js')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    set1.pop('js')
TypeError: pop() takes no arguments (1 given)
>>> set1.remove('js')
>>> set1
{100, 'siddharth', 5, 6, 'hello', 'anmol', 'python'}
>>> set1.remove('js')
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    set1.remove('js')
KeyError: 'js'
>>> 
>>> 
>>> 
>>> set1.symmetric_difference(set2)
{'js', 5, 'siddharth', 6, 'hello', 'anmol', 'python', 'java'}
>>> 
>>> 
>>> set1 - set2
{5, 'siddharth', 6, 'hello', 'anmol', 'python'}
>>> set2 - set1
{'js', 'java'}
>>> (set1 - set2).union(set2 - set1)
{'python', 'js', 5, 'siddharth', 6, 'hello', 'anmol', 'java'}
>>> 
