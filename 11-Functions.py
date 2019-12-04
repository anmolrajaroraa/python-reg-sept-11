import functools, itertools, operator

list1 = [6,2,3,4,5]

'''
1 + 2 -> [3,3,4,5]
3 + 3 -> [6,4,5]
6 + 4 -> [10,5]
10+5 -> 15
'''

# print(functools.reduce(operator.add, list1))

def add(a,b):
    print(f"{a} +{b} -> {a**b}")
    return a**b

print(functools.reduce(add, list1))
print(list(itertools.accumulate(list1, add)))