# file = open('file2.txt', 'r')
# data = file.read()
# print(data)
# data = file.read(50)
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
# print(data)
# data = file.readlines()
# print(data)


# file = open("file3.txt", 'a')
# file.write("\nI'm writing for the fourth time")

# file = open('file3.txt', 'a+')
# file.write('Using a+ mode')
# file.read()
# file.close()

file = open('image.jpg', 'rb')
data = file.read()
file.close()

file = open('copy_image.jpg', 'wb')
file.write(data)
file.close()