list1 = ['Ram', 'Shyam', 'Mohan']
list2 = [10000,15000,20000]

# for name in list1:
#     print(name)

# for i in range(len(list1)):
#     print(i+1,list1[i])

# for i,name in enumerate(list1,start=1):
#     print(i,name)

# a,b = (10,20)
# (1,Ram)
# (2,Shyam)

# print(list(enumerate(list1, start=1)))

# for i in range(len(list1)):
#     print(list1[i],list2[i])

print(list(zip(list1,list2)))

for name,salary in zip(list1,list2):
    print(name,salary)