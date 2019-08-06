# Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also,
# 1! = 1
# 0! = 0 Write a program to calculate factorial of a number.


def find_factorial(num):
    i = num
    mul = 1
    fact = ""

    if num == 0 or num == 1:
        print(f"{num}! = {num}")
    else:
        while i >= 1:
            mul = mul * i
            fact = str(i) if fact == "" else fact + " * " + str(i)
            i -= 1

        print(f"{num}! = {fact} = {mul}")


if __name__ == "__main__":
    while True:
        num = input("Enter the number to find factorial or q to quit : ")
        if num == "q":
            break
        elif num.isnumeric():
            find_factorial(int(num))
        else:
            print("Unknown command..")
