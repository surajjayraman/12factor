from random import randint

prime = 23
primitive_root = 9

bob_private_key = randint(1, prime - 1)
alice_private_key = randint(1, prime -1 )

print("bob_private_key: ", bob_private_key)
print("alice_private_key: ", alice_private_key)