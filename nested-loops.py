#pending - count() using nested loops

list1 = [11,22,33,44,55, ['anmol', 'ram', 'shyam'], [99,88,77,66] ]

length = len(list1)
#print(length)
for index in range(length):    #using indexes   -   range accepts only integer so we give length of list
    if type( list1[ index ] ) == int:
        print( list1[ index ] )
        continue
    for x in range( len( list1[index] ) ):
        print( list1[index][x]  )

'''for item in list1:    #using elements directly
    if type(item) == int:
        print(item)
        #break
        continue
    for j in item:
        print(j)'''