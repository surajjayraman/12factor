import random
from math import sqrt

my_name = "Robb"
my_age = 28

my_list = [1, 2, 'Text']

my_dict = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

print(my_dict["C"])
print(my_name[0].isupper())
print(my_name[0].islower())

# define a function
def add_numbers(number1, number2):
    return number1 + number2

number1 = 6
number2 = 9

results = add_numbers(number1, number2)
print(results)

sqrt_results = sqrt(16);
print(sqrt_results)
