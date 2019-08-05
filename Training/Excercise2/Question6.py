# 6. Write a Python class to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number. - Go to the editor
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4


class Elements:
    def __init__(self, lst, target):
        self.lst = lst
        self.target = target

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[item]

    def find_elements(self):
        lst_len = self.__len__()
        i = 0
        while i < lst_len - 1:
            sum_ele = self.__getitem__(i) + self.__getitem__(i+1)
            if sum_ele == self.target:
                print(f"{i+1}, {i+2}")
            i += 1


while True:
    num = ""
    target = ""
    try:
        nums = input("Enter an array of numbers separated by \',\' : ")
        lst = list(int(num) for num in nums.split(","))
    except ValueError as e:
        print("Invalid number array..")
        continue

    try:
        target = int(input("Enter a target number : "))
    except ValueError as ve:
        print("Invalid target number..")
        continue

    elements = Elements(lst, target)
    elements.find_elements()
    break

