# Print multiplication table of 24, 50 and 29 using loop


def print_table(table):
    i = 1
    while i <= 10:
        mul = table * i
        print(f"{table} * {i} = {mul}")
        i += 1


if __name__ == "__main__":
    while True:
        table = input("Enter number to print the table or \'q\' to exit : ")
        if table == "q":
            break
        elif table.isnumeric():
            print_table(int(table))
        else:
            print("Unknown command..")
