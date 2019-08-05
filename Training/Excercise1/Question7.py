# Take 10 integers from the keyboard using a loop and print their average value on the screen.


def find_average(numbers):
    i = len(numbers)
    summetion = 0
    while i > 0:
        i -= 1
        summetion += int(numbers[i])
    average = summetion/len(numbers)
    return average


if __name__ == "__main__":
    numbers = []
    while True:
        number = input("Enter a number or \'a\' to calculate average or \'q\' to exit : ")
        if number == "q":
            break
        elif number == "a":
            average = find_average(numbers)
            print(f"Average: {average}")
            numbers.clear()
        else:
            if number.isnumeric():
                numbers.append(number)
            else:
                print("Unknown command..")

