def calc(x=0,y=0,*args,**kwargs):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    rem = x % y
    # result = [add,sub]
    # return result
    # return sub
    return add,sub,mul,div,rem  #packing

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# result = calc( num1, num2 )
# print(result)
# print(f"Sum of {num1} and {num2} is {result[0]}")
# print(f"Diff of {num1} and {num2} is {result[1]}")
# print(f"Product of {num1} and {num2} is {result[2]}")
# print(f"Division of {num1} and {num2} is {result[3]}")

a,b,*c = calc(num1,num2)   #unpacking
print(a,b,c)
# print(f"Sum of {num1} and {num2} is {a}")
# print(f"Diff of {num1} and {num2} is {b}")
# print(f"Product of {num1} and {num2} is {c}")
# print(f"Division of {num1} and {num2} is {d}")

# a = (10,20)