# def calc(x=0,y=0,*args):
#     yield x + y
#     yield x - y

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = calc(num1,num2)
# print(result)
# print(result.__next__())
# print(result.__next__())

def calc(x=0,y=0,*args):
    return x+y, x-y, x*y, x/y, x%y, x**y    #packing -> creates a tuple

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = calc(num1,num2)
print(result)    #unpacking -> receives a tuple

a,b,c,*d = calc(num1,num2)
print("A is ",a)
print("B is ",b)
print("C is ",c)
print("D is ",d)