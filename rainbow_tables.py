import hashlib

rainbow_table = {}

common_passwords = ['password', 'admin', 'letmein', '123456','test']

for password in common_passwords:

    hashvalue =  hashlib.sha256(password.encode()).hexdigest()
    rainbow_table[hashvalue] = password

print(rainbow_table)

# crack input password
password_to_crack = input("Please enter the password you wish to crack: ")
hashed_password = hashlib.sha256(password_to_crack.encode()).hexdigest()

if hashed_password in rainbow_table:
    print("Password found for hash")
else:
    print("Password not found in hash")
