'''
1. Try - all you logic or fn calls go here
2. Except - exception handling code goes here
3. Finally - put important things that should always run
4. Else - either except will run or i will run

User-generated exceptions
'''

# def divide(x,y):
#     print(x / y)

# while True:
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         divide(num1,num2)
#     except ZeroDivisionError:
#         print("Please do not enter zero as second number!")
#     except ValueError:
#         print("Please enter only integers")
#     # except TypeError:
#     #     print("Some error occured!")
#     except BaseException as error:
#         print("error occured...",error)

# import csv,io

# try:
#     with open('users.csv', 'r') as file:
#         data = csv.reader(file)
#         writer = csv.writer(file)
#         for row in data:
#             print(row)
#             writer.writerow(row)
# except FileNotFoundError:
#     print("File doesn't exist!!")
# except io.UnsupportedOperation:
#     print("Please check the file modes!")
# except BaseException as error:
#     print(error)
# else:
#     print("Else ran!!!")
# finally:
#     print("Finally ran!!")
#     file.close()



def atm():
    balance = 10000
    withdrawAmount = int(input("Enter amount to withdraw : "))
    if withdrawAmount <= balance:
        balance = balance - withdrawAmount
        print("Current balance is",balance)
    else:
        raise ValueError('Insufficient balance!')

try:
    atm()
except ValueError as error:
    print(error)
except BaseException as error:
    print(error)