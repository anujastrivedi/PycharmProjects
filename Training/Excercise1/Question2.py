# Write a program to find the length of the string "refrigerator" without using the len function.


def count_length_of_string(strs):
    l1 = 0
    for s in strs:
        l1 += 1
    return l1


if __name__ == "__main__":
    while True:
        string = input("Enter a String or \'q\' to exit : ")
        if string == "q":
            break
        else:
            length = count_length_of_string(string)
            print(f"Length of the string \'{string}\' : {length}")
