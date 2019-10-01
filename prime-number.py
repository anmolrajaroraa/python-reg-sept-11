number = int(input("Enter a number to check if it is prime or not: "))

numberIsPrime = True

if number <= 1:
    print("Invalid number!")
    numberIsPrime = False
else:
    for i in range(  2  ,  ((number // 2) + 1)   ):
        if number % i == 0:    #   % is used for checking remainder
            print("Number is not prime!!")
            numberIsPrime = False
            break

if numberIsPrime:
    print("Number is prime!!")