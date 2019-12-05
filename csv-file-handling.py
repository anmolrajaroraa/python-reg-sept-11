import csv

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    with open('users.csv', 'r') as file:
        data = csv.reader(file)
        for row in data:
            print(row)
            if email == row[1] and password == row[2]:
                print("Login successful")
                break
        else:
            print("Invalid userid / password")

def register():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # file = open('users.csv', 'w')

    # import urllib.request as req

    with open('users.csv', 'a') as file:
        writer = csv.writer(file)
        row = username,email,password
        writer.writerow(row)


print('''
1. Login
2. Register
''')

choice = int(input("Enter your choice: "))

options = {1: login, 2: register}

options[choice]()