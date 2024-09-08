
num = int(input("Enter a number"))

for i in range(2, num):
    if num % i == 0:
        print("The number is not a prime number")
        break;
    else:
        print("Prime number it is")
        