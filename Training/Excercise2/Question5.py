# Write a Python class to reverse a string word by word. - Go to the editor
# Input string : 'hello .py'
# Expected Output : '.py hello'


class ReverseString:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        reversed_str = " ".join((self.string).split(" ")[::-1])
        print(reversed_str)


string = input("Enter a string : ")
string1 = ReverseString(string)
string1.reverse()
