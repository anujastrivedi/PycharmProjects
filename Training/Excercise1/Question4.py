# Write a program to check if the word 'orange' is present in the "This is orange juice".


def find_occurence_of_word(strs, word):
    if strs.find(word) != -1:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        string = input("Enter a String or \'q\' to exit : ")
        word = input("Enter a Word or \'q\' to exit : ")
        if string == "q" and word == "q":
            break
        else:
            c = find_occurence_of_word(string, word)
            if c:
                print(f"\'{word}\' is present in the word \'{string}\'")
            else:
                print(f"\'{word}\' is not present in the word \'{string}\'")
