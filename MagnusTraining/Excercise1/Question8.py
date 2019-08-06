# a.
# *
# **
# ***
# ****


def pattern_a():
    i = 1
    while i < 5:
        j = 1
        while j <= i:
            print("*", end='')
            j += 1
        print("")
        i += 1


# b.
#   *
#  ***
# *****
#  ***
#   *


def pattern_b():
    i = 1
    k = 2
    while i < 7 | i > 0:
        j = 1
        s = 0
        while s < 2 - (i/2):
            print(" ", end='')
            s += 1

        while j <= i:
            print("*", end='')
            j += 1
        print("")
        if i >= 5:
            k = k * -1

        i += k


# c.
# 1010101
# 10101
# 101
# 1


def pattern_c():
    i = 7
    while i > 0:
        j = 1
        while j <= i:
            print("0" if j % 2 == 0 else "1", end='')
            j += 1
        print("")
        i -= 2


if __name__ == "__main__":
    pattern_a()
    pattern_b()
    pattern_c()
