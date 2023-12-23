from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes

def DES3_CBC_encrypt(plaintext, DES3_key, initialization_vector):

    DES3_CBC_cipher = DES3.new(DES3_key, DES3.MODE_CBC, iv=initialization_vector)
    ciphertext = DES3_CBC_cipher.encrypt((pad(plaintext, DES3.block_size)))

    return ciphertext

def DES3_CBC_decrypt(ciphertext, DES3_key, initialization_vector):

    DES3_CBC_cipher = DES3.new(DES3_key, DES3.MODE_CBC, iv=initialization_vector)
    decrypted_plaintext = unpad(DES3_CBC_cipher.decrypt(ciphertext), DES3.block_size)
    
    return decrypted_plaintext