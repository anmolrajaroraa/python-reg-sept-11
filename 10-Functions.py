# def temp_convert(c):
#     return 9/5 * c + 32

# temp = 36

# f_temp = temp_convert(temp)
# print(f_temp)

# temp = 0
# while True:
#     if temp_convert(temp) == temp:
#         print(temp)
#         break
#     temp = temp - 1

# temp_list = [5,10,15,20,25,30,35,40,45,50]

# f_temp_list = []

# for temp in temp_list:
#     f_temp_list.append(temp_convert(temp))

# f_temp_list = [temp_convert(temp) for temp in temp_list]
# f_temp_list = list(map(temp_convert, temp_list))

# print(f_temp_list)



def even(num):
    return num % 2 == 0

# print(even(10))

numbers = [i for i in range(1,101)]

new_list = list(map(even, numbers))
print(new_list)

# even_list = list(filter(even, numbers))
# print(even_list)

even_list = []

for number in numbers:
    if even(number):
        even_list.append(number)