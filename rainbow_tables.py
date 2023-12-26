import hashlib

rainbow_table = {}

common_passwords = ['password', 'admin', 'letmein', '123456','test']

for password in common_passwords:

    hashvalue =  hashlib.sha256(password.encode()).hexdigest()
    rainbow_table[hashvalue] = password

print(rainbow_table)
