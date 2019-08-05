# . Create a Temperature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


class Temperature:

    @classmethod
    def convert_fahrenheit_to_celsius(cls, fahrenheit):
        celsius = int(round(((fahrenheit - 32) * (5/9))))
        print(f"Conversion of {fahrenheit} to  : {celsius}" + u"\u2103")

    @classmethod
    def convert_celsius_to_fahrenheit(cls, celsius):
        fahrenheit = int(round((celsius * (9 / 5)) + 32))
        print(f"Conversion of {celsius} to  : {fahrenheit}" + u"\u2109")


temp = Temperature()
temp.convert_fahrenheit_to_celsius(100)
temp.convert_celsius_to_fahrenheit(38)

