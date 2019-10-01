
'''list1 = [11,22,33,44,55, ['anmol', 'ram', 'shyam'], [99,88,77,66] ]

length = len(list1)
#print(length)
for index in range(length):    #using indexes   -   range accepts only integer so we give length of list
    if type( list1[ index ] ) == int:
        print( list1[ index ] )
        continue
    for x in range( len( list1[index] ) ):
        print( list1[index][x]  )'''

'''for item in list1:    #using elements directly
    if type(item) == int:
        print(item)
        #break
        continue
    for j in item:
        print(j)'''

newList = [  11,22,33,44,55, [12,22,32,42,52], [19,29,39,49,59]  ]

#print(newList.count(22))

numberFound = False

number = int(input("Enter a number to check if it is present in list or not: "))

if number in newList:
    print("Number found!")
    numberFound = True
else:
    for item in newList:
        if type(item) == list:
            if number in item:
                print("Number found")
                numberFound = True
                break

if (not numberFound):
    print("Number not found")

'''else:
    print("Number not found")'''