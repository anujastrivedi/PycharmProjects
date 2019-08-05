# Write a program that takes your full name as input and displays the abbreviations of the first and middle names
# except for the last name which is displayed as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.


def get_name_abbreviation(full_name):
    abbreviations = ""
    word_count = len(full_name.split(' '))
    for name in full_name.split(' '):
        word_count -= 1
        abbreviations += name.capitalize() if (word_count == 0) else name[0].capitalize() + "."
    return abbreviations


if __name__ == "__main__":
    while True:
        full_name = input("Enter your full name: ")

        if full_name == "q":
            break
        elif full_name == "":
            True
        else:
            abbreviations = get_name_abbreviation(full_name)
            print(abbreviations)
