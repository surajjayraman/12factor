from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes

def AES_CBC_encrypt(plaintext, AES_key, initialization_vector):

    AES_CBC_cipher = AES.new(AES_key, AES.MODE_CBC, iv=initialization_vector)
    ciphertext = AES_CBC_cipher.encrypt((pad(plaintext, AES.block_size)))
    return ciphertext

#def AES_CBC_decrypt(ciphertext, AES_key, initialization_vector)