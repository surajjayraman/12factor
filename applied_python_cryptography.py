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

start = 1
end = 10

for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, " is odd")


# The Caesar Cipher
def encrypt (plaintext, shift_key):
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_shifted = (char_index + shift_key) % 26 + ord("A")
            char_encrypted = chr(char_shifted)
            ciphertext += char_encrypted
        elif char.islower():
            char_index = ord(char) - ord("a")
            char_shifted = (char_index + shift_key) % 26 + ord("a")
            char_encrypted = chr(char_shifted)
            ciphertext += char_encrypted
        else :
            ciphertext += char

    return ciphertext    

