import operator

def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
def errorHandler(*args):
    quit()

while True:
    print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    ''')

    choice = int(input("Enter your choice: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # options = {1: add, 2: subtract, 3: multiply, 4: divide,5: errorHandler}
    # print(options)
    options = {1: operator.add, 2: operator.sub, 3: operator.mul, 4: operator.truediv, 5: errorHandler}

    print(options[choice](num1,num2))

    # if choice == 1:
    #     add(num1,num2)
    # elif choice == 2:
    #     subtract(num1,num2)
    # elif choice == 3:
    #     multiply(num1,num2)
    # elif choice == 4:
    #     divide(num1,num2)
    # else:
    #     quit()





    #map,filter,reduce(functools),accumulate(itertools),lambda,zip,enumerate