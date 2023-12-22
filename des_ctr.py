from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def DES_CTR_encrypt(plaintext, DES_key, nonce):

    DES_CTR_cipher =  DES.new(DES_key, DES.MODE_CTR, nonce=nonce)
    ciphertext = DES_CTR_cipher.encrypt(plaintext)

    return ciphertext

def DES_CTR_decrypt(ciphertext, DES_key, nonce):

    DES_CTR_cipher =  DES.new(DES_key, DES.MODE_CTR, nonce=nonce)
    decrypted_plaintext = DES_CTR_cipher.decrypt(ciphertext)
    
    return decrypted_plaintext