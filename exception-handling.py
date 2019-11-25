'''
1. Try - all you logic or fn calls go here
2. Except - exception handling code goes here
3. Finally - put important things that should always run
4. Else
'''

# def divide(x,y):
#     print(x/y)
#     return None

# try:
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))
#     divide(num1,num2)
# except ZeroDivisionError as error:
#     print("Please don't give zero as second argument")
# except ValueError as error:
#     print("Please use numbers only for input")
# # except TypeError:
# #     print("Some error occured..")
# except BaseException as error:
#     print("Some error occured..", error)

# import csv,io,os

# path = "users2.csv"
# try:
#     with open(path, 'r') as file:
#         writer = csv.writer(file)
#         writer.writerow((101, "Ram"))
#         # print(data)
# except FileNotFoundError as error:
#     print("File not found!")
# except io.UnsupportedOperation as error:
#     print("Please check file modes again!")
# except BaseException as error:
#     print(error)
# finally:
#     print("Finally ran")
#     if os.path.exists(path):
#         file.close()


def withdraw():
    print("Withdraw called..")
    # raise TypeError("Pin incorrect")

def checkBalance():
    print("checkBalance called..")
    

try:
    withdraw()
    checkBalance()
except BaseException as error:
    print(error)
else:
    print("thanks for visiting..")