x = 10   #global variables
y = 20 

# def add():
#     print(f"{x} + {y} is {x+y}")

# def sub(x,y):
#     print(f"{x} - {y} is {x - y}")

# def mul(x=0, y=0):     #default arguments
#     print(f"{x} * {y} is {x * y}")

# def divide(x=1,y=1,*args):
#     print("X is ",x)
#     print("Y is", y)
#     print("*args is",args )
#     print(f"{x} / {y} is {x/y}")

# Dynamic arguments
# 1. Default arguments
# Provide some default value to the arguments, if some new value is provided during fn call, default value is not used.
# But if no value is received as argument in fn call then default value will be used

# 2. Extra arguments - *args, **kwargs

# *args -> I will accept all the extra positional arguments provided to the function and will store them in a tuple
# **kwargs (keyword arguments) -> I will accept all the extra keyword arguments (arguments that are using some key during fn call) and will store them in a dictionary

# add()

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sub(num1,num2)

# mul(num1,num2)    #positional arguments

# divide(num1,num2,10,20,30)

def createEmployeeProfile(id,name,dept=None,project=None,salary=None,**otherDetails):
    print(f"Id is {id}")
    print(f"Name is {name}")
    print(f"Dept is {dept}")
    print(f"Project is {project}")
    print(f"Salary is {salary}")
    print(f"Other details are {otherDetails}")

# createEmployeeProfile(101,'Ram','IT','Phoenix',10000)

createEmployeeProfile(101,'Ram',salary=10000,dept='IT',project='Star',age=25,leavesLeft=10)