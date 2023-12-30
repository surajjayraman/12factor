from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

def encrypt_symmetric_key(symmetric_key, public_key):

    RSA_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_symmetric_key = RSA_cipher.encrypt(symmetric_key)

    return encrypted_symmetric_key


def decrypt_symmetric_key(encrypted_symmetric_key, private_key):

    RSA_cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted_symmetric_key = RSA_cipher.decrypt(encrypted_symmetric_key)

    return decrypted_symmetric_key
