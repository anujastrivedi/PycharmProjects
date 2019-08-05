# Write a program to check if the letter 'e' is present in the word 'Umbrella'.


def find_occurence_of_letter(strs, lett):
    return strs.count(lett)


if __name__ == "__main__":
    while True:
        string = input("Enter a String or \'q\' to exit : ")
        letter = input("Enter a Letter or \'q\' to exit : ")
        if string == "q" and letter == "q":
            break
        else:
            c = find_occurence_of_letter(string, letter)
            print(f"\'{letter}\' is present {c} times in the word \'{string}\'")
