# Write a program to print every character of a string entered by the user in a new line using a loop.


def print_characters_of_string(strs):
    # while True:
    #     string = input("Enter String: ")
    #     if string == "q":
    #         break
    #     else:
    for s in strs:
        print(s)


if __name__ == "__main__":
    while True:
        string = input("Enter a String or \'q\' to exit : ")
        if string == "q":
            break
        else:
            print_characters_of_string(string)
