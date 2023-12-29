from random import randint

prime = 23
primitive_root = 9

bob_private_key = randint(1, prime - 1)
alice_private_key = randint(1, prime -1 )

print("bob_private_key: ", bob_private_key)
print("alice_private_key: ", alice_private_key)

bob_public_key = pow(primitive_root, bob_private_key, prime)
alice_public_key = pow(primitive_root, alice_private_key, prime)

shared_secret_key_bob = pow(alice_public_key, bob_private_key, prime)
shared_secret_key_alice = pow(bob_public_key, alice_private_key, prime)

if (shared_secret_key_bob == shared_secret_key_alice):
    print("Secret keys match!")
else:
    print("Secret keys do not match")
