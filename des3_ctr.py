from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def DES3_CTR_encrypt(plaintext, DES3_key, nonce):

    DES3_CTR_cipher =  DES3.new(DES3_key, DES.MODE_CTR, nonce=nonce)
    ciphertext = DES3_CTR_cipher.encrypt(plaintext)

    return ciphertext