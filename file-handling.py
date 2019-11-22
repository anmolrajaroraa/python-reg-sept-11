# file = open('file-handling.txt')
# data = file.read(50)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# data = file.read()
# print(data)
# file.seek(0)
# data = file.readlines()
# print(data)

# file = open('file2.txt', 'w')
# file.write('abcd')

# file = open('file2.txt', 'a+')
# file.write('efgh')
# file.seek(0)
# data = file.read()
# print("data is " + data)
# file.close()

# file = open('image.jpg', 'rb')
# data = file.read()
# # print(data)
# file2 = open('copiedImage.jpg', 'wb')
# file2.write(data)
# file2.close()

users = [
    {
        'name' : 'ram',
        'email' : 'ram@gmail.com',
        'password' : '1234'
    },
    {
        'name' : 'shyam',
        'email' : 'shyam@gmail.com',
        'password' : '123456'
    }
]

import csv
# with open('users.csv', 'w') as file:
#     writer = csv.writer(file)   #file creation
#     for user in users:
#         # print(user.values())
#         writer.writerow(user.values())

with open('users.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row[0], row[1], row[2])