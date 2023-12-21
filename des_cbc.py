from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes

def DES_CBC_encrypt(plaintext, DES_key, initialization_vector):

    DES_CBC_cipher = DES.new(DES_key, DES.MODE_CBC, iv=initialization_vector)
    ciphertext = DES_CBC_cipher.encrypt((pad(plaintext, DES.block_size)))
    return ciphertext

def DES_CBC_decrypt(ciphertext, DES_key, initialization_vector):

    DES_CBC_cipher = DES.new(DES_key, DES.MODE_CBC, iv=initialization_vector)
    decrypted_plaintext = unpad(DES_CBC_cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_plaintext

