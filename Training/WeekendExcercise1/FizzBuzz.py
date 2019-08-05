# Make sure your program prints from 1 to 100, both inclusive!


def fizz_buzz_challenge(nums):

    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


if __name__ == "__main__":
    numbers = list(range(1, 101))
    fizz_buzz_challenge(numbers)
