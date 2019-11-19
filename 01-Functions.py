# #function - reusable code

# x = 10   #global variables
# y = 20

# #    *args -> multiple arguments
# #    **kwargs -> keyword arguments

# def my_function( x=0 , y=0, *other, **keyValuePairs ):   #function definition  #default arguments  #dynamic arguments
#     #x = 10   #local variables
#     #y = 20
#     print(f"Sum of {x} and {y} is {x+y}")
#     print(f"Other is {other}")
#     print(f"** is {keyValuePairs}")

# print("Before calling fn")
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# my_function( 100,200,300,z=num1 )     #function call

# print("After calling fn")
# print(f"X is {x}")

def employee( id, name, salary=0, address=None, *otherDetails, **someOtherDetails):
    print(f"Id is {id}")
    print(f"Name is {name}")
    print(f"Salary is {salary}")
    print(f"Address is {address}")
    print(f"Other details are {otherDetails}")
    print(f"Some more details are {someOtherDetails}")



print(employee)
employee(101, "Ram", 10000, 'Rohini', 'twenty five', age=35, contact='1234556789')