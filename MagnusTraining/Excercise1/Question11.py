# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.


def find_factors(number):
    i = 1
    factor = []
    if number == 0:
        factor.append(0)
    else:
        while i <= number:
            if number % i == 0:
                factor.append(i)
            i += 1
    return factor


def find_highest_common_factor(f1, f2):
    common_factors = list(set(f1).intersection(set(f2)))
    hfc = 0 if len(common_factors) == 0 else max(common_factors)
    #print(f"Common factors of {number1} and {number2} : {common_factors}")
    return hfc


if __name__ == "__main__":
    while True:
        number1 = input("Enter number1 : ")
        number2 = input("Enter number2 : ")
        if number1 == "q" and number2 == "q":
            break
        elif number1.isnumeric() and number2.isnumeric():
            factor1 = find_factors(int(number1))
            factor2 = find_factors(int(number2))
            print(f"Factors of {number1} : {factor1}")
            print(f"Factors of {number2} : {factor2}")

            HCF = find_highest_common_factor(factor1, factor2)
            print(f"Highest Common factors of {number1} and {number2} : {HCF}")
        else:
            print("Unknown command..")
