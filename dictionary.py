Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list [] mutable
>>> #tuple () immutable
>>> #set {} mutable random-hashing - no indexing - no key value pair
>>> #frozen set {} immutable
>>> set1 = {1,2,3,4,5}
>>> set1
{1, 2, 3, 4, 5}
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set1.add(6)
>>> set1
{1, 2, 3, 4, 5, 6}
>>> frozenset(set1)
frozenset({1, 2, 3, 4, 5, 6})
>>> f_set_1 = frozenset(set1)
>>> type(f_set_1)
<class 'frozenset'>
>>> f_set_1.add(7)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    f_set_1.add(7)
AttributeError: 'frozenset' object has no attribute 'add'
>>> dir(frozenset)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> 
>>> 
>>> 
>>> 
>>> #dict {} -> key value pairs
>>> 
>>> employee = {
	'id
	
SyntaxError: EOL while scanning string literal
>>> employee = {
	'id' : 101,
	'name' : 'Sid',
	'job' : 'Govt.',
	'salary' : 50000,
	'contact' : '1234',
	'address' : 'rohini'
	}
>>> 
>>> type(employee)
<class 'dict'>
>>> 
>>> employee
{'id': 101, 'name': 'Sid', 'job': 'Govt.', 'salary': 50000, 'contact': '1234', 'address': 'rohini'}
>>> 
>>> employee['id']
101
>>> employee['name']
'Sid'
>>> employee['salary']
50000
>>> employee = {
	'id' : 101,
	'name' : 'Sid',
	'job' : 'Govt.',
	'salary' : 50000,
	'contact' : '1234',
	'perm_address' : 'rohini',
	'temp_address' : 'pitampura'
	}
>>> 
>>> 
>>> employee2 = {
	'id' : 101,
	'name' : 'Sid',
	'job' : 'Govt.',
	'salary' : 50000,
	'contact' : '1234',
	'perm_address' : 'rohini'
	}
>>> 
>>> employee['temp_address']
'pitampura'
>>> employee2['temp_address']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    employee2['temp_address']
KeyError: 'temp_address'
>>> 
>>> employee = {
	'id' : 101,
	'name' : 'Sid',
	'job' : 'Govt.',
	'salary' : 50000,
	'contact' : ['1234', '4567']
	'address' : {
		'perm_address' : 'Rohini',
		'temp_address' : 'Pitampura'
		}
	}
SyntaxError: invalid syntax
>>> 
>>> employee = {
	'id' : 101,
	'name' : 'Sid',
	'job' : 'Govt.',
	'salary' : 50000,
	'contact' : ['1234', '4567'],
	'address' : {
		'perm_address' : 'Rohini',
		'temp_address' : 'Pitampura'
		}
	}
>>> 
>>> employee
{'id': 101, 'name': 'Sid', 'job': 'Govt.', 'salary': 50000, 'contact': ['1234', '4567'], 'address': {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}}
>>> 
>>> 
>>> employee[contact]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    employee[contact]
NameError: name 'contact' is not defined
>>> employee['contact']
['1234', '4567']
>>> employee['contact'][0]
'1234'
>>> 
>>> employee['address']
{'perm_address': 'Rohini', 'temp_address': 'Pitampura'}
>>> employee['address']['temp_address']
'Pitampura'
>>> 
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> employee.get('address')
{'perm_address': 'Rohini', 'temp_address': 'Pitampura'}
>>> employee.items()
dict_items([('id', 101), ('name', 'Sid'), ('job', 'Govt.'), ('salary', 50000), ('contact', ['1234', '4567']), ('address', {'perm_address': 'Rohini', 'temp_address': 'Pitampura'})])
>>> 
>>> employee.keys()
dict_keys(['id', 'name', 'job', 'salary', 'contact', 'address'])
>>> employee.values()
dict_values([101, 'Sid', 'Govt.', 50000, ['1234', '4567'], {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}])
>>> 
>>> employee.pop()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    employee.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> employee.pop('job')
'Govt.'
>>> employee
{'id': 101, 'name': 'Sid', 'salary': 50000, 'contact': ['1234', '4567'], 'address': {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}}
>>> employee.popitem()
('address', {'perm_address': 'Rohini', 'temp_address': 'Pitampura'})
>>> 
>>> employee
{'id': 101, 'name': 'Sid', 'salary': 50000, 'contact': ['1234', '4567']}
>>> 
>>> employee['address'] = {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}
>>> employee
{'id': 101, 'name': 'Sid', 'salary': 50000, 'contact': ['1234', '4567'], 'address': {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}}
>>> 
>>> help(dict.setdefault)
Help on method_descriptor:

setdefault(self, key, default=None, /)
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> 
>>> 
>>> employee
{'id': 101, 'name': 'Sid', 'salary': 50000, 'contact': ['1234', '4567'], 'address': {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}}
>>> employee.setdefault('job', 'Govt.')
'Govt.'
>>> employee
{'id': 101, 'name': 'Sid', 'salary': 50000, 'contact': ['1234', '4567'], 'address': {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}, 'job': 'Govt.'}
>>> employee.setdefault('job', 'Pvt.')
'Govt.'
>>> employe
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    employe
NameError: name 'employe' is not defined
>>> employee
{'id': 101, 'name': 'Sid', 'salary': 50000, 'contact': ['1234', '4567'], 'address': {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}, 'job': 'Govt.'}
>>> carDetails_employee1 = {
	'brand' : 'Suzuki',
	'model' : 'swift',
	'make' : 2019,
	'color' : 'grey'
	}
>>> 
>>> 
>>> employee.update(carDetails_employee1)
>>> employee
{'id': 101, 'name': 'Sid', 'salary': 50000, 'contact': ['1234', '4567'], 'address': {'perm_address': 'Rohini', 'temp_address': 'Pitampura'}, 'job': 'Govt.', 'brand': 'Suzuki', 'model': 'swift', 'make': 2019, 'color': 'grey'}
>>> help(dict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> 
>>> keys = {'id', 'name', 'address', 'contact', 'salary', 'job'}
>>> 
>>> dict.fromkeys(keys, 'None')
{'address': 'None', 'salary': 'None', 'contact': 'None', 'id': 'None', 'name': 'None', 'job': 'None'}
>>> employee = dict.fromkeys(keys, 'None')
>>> user = dict.fromkeys(keys, 'None')
>>> user['name'] = 'Ram'
>>> user['job'] = 'Pvt.'
>>> #user['id'] = generated_id
