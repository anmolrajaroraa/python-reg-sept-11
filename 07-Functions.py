x = 100
y = 200
def outer():
    print("Outer fn called..")
    x = 10
    print("X is ",x)
    def inner():   #local fn
        global y
        x = 1
        y = 2
        print("Inner fn called..")
        print("X is ",x)
        print("Y is ",y)
    # inner()
    return inner

returnedItem = outer()
print("Y is ", y)
print("Returned item is",returnedItem)
returnedItem()