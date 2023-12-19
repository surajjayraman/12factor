# more modern mode of operations for stream ciphers
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def AES_GCM_encrypt(plaintext, AES_key, nonce):

    AES_GCM_cipher =  AES.new(AES_key, AES.MODE_GCM, nonce=nonce)
    