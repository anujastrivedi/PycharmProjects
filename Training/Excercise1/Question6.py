# Write a program to make a new string with all the consonants deleted from the string "Hello, have a good day".


def find_vowels_in_string(strs):
    vowels = "AaEeIiOoUu"
    vowels_string = ""

    vowels_list = [word for word in strs if word in vowels]
    vowels_string = vowels_string.join(vowels_list)
    return vowels_string


if __name__ == "__main__":
    while True:
        string = input("Enter a string: ")

        if string == "q":
            break
        else:
            vowels_string = find_vowels_in_string(string)
            print(f"Vowels in the \'{string}\' : {vowels_string}")
