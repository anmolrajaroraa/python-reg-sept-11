x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print("X in inner() is", x)
    print("X in outer() is", x)
    # inner()
    # print(inner)
    return inner
print("Global x is", x)
result = outer()
print(result)
result()