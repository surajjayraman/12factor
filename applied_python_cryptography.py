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


# The Caesar Cipher encryption and decryption
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

def decrypt(ciphertext, shift_key):

    decrypted_plaintext = ""

    for char in ciphertext:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_unshifted = (char_index  - shift_key) % 26 + ord("A")
            char_decrypted = chr(char_unshifted)
            decrypted_plaintext += char_decrypted
        elif char.islower():
            char_index = ord(char) - ord("a")
            char_unshifted = (char_index - shift_key) % 26 + ord("a")
            char_decrypted = chr(char_unshifted)
            decrypted_plaintext += char_decrypted
        else :
            decrypted_plaintext += char

    return decrypted_plaintext

# user input for cipher 

plaintext = input ("Enter plaintext: ")
shift_key=10
ciphertext = encrypt(plaintext, shift_key)
decrypted_cipher = decrypt(ciphertext, shift_key)
print(ciphertext)
print(str(shift_key))
print(decrypted_cipher)

# try cracking by bruteforce

ciphertext = "rovvy, cebkt, ryg kbo, iye?"

def caesar_bruteforce(ciphertext):

    for shift_key in range(0, 25):
        decrypted_plaintext = ""
        for char in ciphertext:
            if char.islower():
                char_index = ord(char) - ord("a")
                char_unshifted = (char_index - shift_key) % 26 + ord("a")
                char_decrypted = chr(char_unshifted)
                decrypted_plaintext += char_decrypted
            else :
                decrypted_plaintext += char
        print("with a shift of" + str(shift_key) + "the decrypted text is: " + decrypted_plaintext)

caesar_bruteforce(ciphertext)






